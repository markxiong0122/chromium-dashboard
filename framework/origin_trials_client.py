# Copyright 2023 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.auth
from google.auth.transport.requests import Request

from dataclasses import asdict
from datetime import datetime
import logging
from typing import Any
import requests

from framework import secrets
from internals.data_types import OriginTrialInfo
import settings


CHROMIUM_SCHEDULE_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'


def get_trials_list() -> list[dict[str, Any]]:
  """Get a list of all origin trials.
  
  Returns:
    A list of data on all public origin trials.

  Raises:
    requests.exceptions.RequestException: If the request fails to connect or
      the HTTP status code is not successful.
    KeyError: If the response from the OT API is not in the expected format.
  """
  key = secrets.get_ot_api_key()
  # Return an empty list if no API key is found.
  if key == None:
    return []

  try:
    response = requests.get(
        f'{settings.OT_API_URL}/v1/trials',
        params={'prettyPrint': 'false', 'key': key})
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    logging.exception('Failed to get response from origin trials API.')
    raise e

  response_json = response.json()

  trials_list = [asdict(OriginTrialInfo(api_trial))
                 for api_trial in response_json['trials']
                 if api_trial['isPublic']]
  return trials_list


def _get_trial_end_time(end_milestone: str) -> int:
  """Get the end time of the origin trial based on end milestone.

  Returns:
    The end time of the origin trial, represented in seconds since epoch.

  Raises:
    requests.exceptions.RequestException: If the request fails to connect or
      the HTTP status code is not successful.
  """
  milestone_plus_two = int(end_milestone) + 2
  try:
    response = requests.get('https://chromiumdash.appspot.com/fetch_milestone_schedule'
                f'?mstone={milestone_plus_two}')
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    logging.exception('Failed to get response from Chromium Schedule API.')
    raise e
  response_json = response.json()

  date = datetime.strptime(
      response_json['late_stable_date'], CHROMIUM_SCHEDULE_DATE_FORMAT)
  return int(date.strftime('%s'))


def _get_ot_access_token() -> str:
  """Obtain the service account credentials to be used in the request
  using the origin trials auth scope
  
  Returns:
    The access token to be used for origin trials requests.
  """
  credentials, _ = google.auth.default(scopes=[
      'https://www.googleapis.com/auth/chromeorigintrials'])
  credentials.refresh(Request())
  if credentials.token is None:
    return ''
  return credentials.token


def extend_origin_trial(trial_id: str, end_milestone: str, intent_url: str):
  """Extend an existing origin trial.

  Raises:
    requests.exceptions.RequestException: If the request fails to connect or
      the HTTP status code is not successful.
  """
  key = secrets.get_ot_api_key()
  # Return False if no API key is found.
  if key == None:
    return False

  access_token = _get_ot_access_token()
  url = (f'{settings.OT_API_URL}/v1/trials/{trial_id}:add_extension'
         f'key={key}')
  headers = {'Authorization': f'Bearer {access_token}'}
  end_seconds = _get_trial_end_time(end_milestone)
  json = {
    'trial_id': trial_id,
    'end_date': {
      'seconds': end_seconds
    },
    'milestone_end': end_milestone,
    'extension_intent_url': intent_url,
  }

  try:
    response = requests.post(url, headers=headers, json=json)
    response.raise_for_status()
  except requests.exceptions.RequestException as e:
    logging.exception('Failed to get response from origin trials API.')
    raise e
