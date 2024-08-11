from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.request_trial_end_time import RequestTrialEndTime
from chromestatus_openapi import util

from chromestatus_openapi.models.request_trial_end_time import RequestTrialEndTime  # noqa: E501

class RequestTrial(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name=None, start_milestone=None, end_milestone=None, end_time=None, description=None, documentation_url=None, feedback_url=None, intent_to_experiment_url=None, chromestatus_url=None, allow_third_party_origins=None, type=None, origin_trial_feature_name=None):  # noqa: E501
        """RequestTrial - a model defined in OpenAPI

        :param display_name: The display_name of this RequestTrial.  # noqa: E501
        :type display_name: str
        :param start_milestone: The start_milestone of this RequestTrial.  # noqa: E501
        :type start_milestone: str
        :param end_milestone: The end_milestone of this RequestTrial.  # noqa: E501
        :type end_milestone: str
        :param end_time: The end_time of this RequestTrial.  # noqa: E501
        :type end_time: RequestTrialEndTime
        :param description: The description of this RequestTrial.  # noqa: E501
        :type description: str
        :param documentation_url: The documentation_url of this RequestTrial.  # noqa: E501
        :type documentation_url: str
        :param feedback_url: The feedback_url of this RequestTrial.  # noqa: E501
        :type feedback_url: str
        :param intent_to_experiment_url: The intent_to_experiment_url of this RequestTrial.  # noqa: E501
        :type intent_to_experiment_url: str
        :param chromestatus_url: The chromestatus_url of this RequestTrial.  # noqa: E501
        :type chromestatus_url: str
        :param allow_third_party_origins: The allow_third_party_origins of this RequestTrial.  # noqa: E501
        :type allow_third_party_origins: bool
        :param type: The type of this RequestTrial.  # noqa: E501
        :type type: str
        :param origin_trial_feature_name: The origin_trial_feature_name of this RequestTrial.  # noqa: E501
        :type origin_trial_feature_name: str
        """
        self.openapi_types = {
            'display_name': str,
            'start_milestone': str,
            'end_milestone': str,
            'end_time': RequestTrialEndTime,
            'description': str,
            'documentation_url': str,
            'feedback_url': str,
            'intent_to_experiment_url': str,
            'chromestatus_url': str,
            'allow_third_party_origins': bool,
            'type': str,
            'origin_trial_feature_name': str
        }

        self.attribute_map = {
            'display_name': 'display_name',
            'start_milestone': 'start_milestone',
            'end_milestone': 'end_milestone',
            'end_time': 'end_time',
            'description': 'description',
            'documentation_url': 'documentation_url',
            'feedback_url': 'feedback_url',
            'intent_to_experiment_url': 'intent_to_experiment_url',
            'chromestatus_url': 'chromestatus_url',
            'allow_third_party_origins': 'allow_third_party_origins',
            'type': 'type',
            'origin_trial_feature_name': 'origin_trial_feature_name'
        }

        self._display_name = display_name
        self._start_milestone = start_milestone
        self._end_milestone = end_milestone
        self._end_time = end_time
        self._description = description
        self._documentation_url = documentation_url
        self._feedback_url = feedback_url
        self._intent_to_experiment_url = intent_to_experiment_url
        self._chromestatus_url = chromestatus_url
        self._allow_third_party_origins = allow_third_party_origins
        self._type = type
        self._origin_trial_feature_name = origin_trial_feature_name

    @classmethod
    def from_dict(cls, dikt) -> 'RequestTrial':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestTrial of this RequestTrial.  # noqa: E501
        :rtype: RequestTrial
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self) -> str:
        """Gets the display_name of this RequestTrial.


        :return: The display_name of this RequestTrial.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str):
        """Sets the display_name of this RequestTrial.


        :param display_name: The display_name of this RequestTrial.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def start_milestone(self) -> str:
        """Gets the start_milestone of this RequestTrial.


        :return: The start_milestone of this RequestTrial.
        :rtype: str
        """
        return self._start_milestone

    @start_milestone.setter
    def start_milestone(self, start_milestone: str):
        """Sets the start_milestone of this RequestTrial.


        :param start_milestone: The start_milestone of this RequestTrial.
        :type start_milestone: str
        """
        if start_milestone is None:
            raise ValueError("Invalid value for `start_milestone`, must not be `None`")  # noqa: E501

        self._start_milestone = start_milestone

    @property
    def end_milestone(self) -> str:
        """Gets the end_milestone of this RequestTrial.


        :return: The end_milestone of this RequestTrial.
        :rtype: str
        """
        return self._end_milestone

    @end_milestone.setter
    def end_milestone(self, end_milestone: str):
        """Sets the end_milestone of this RequestTrial.


        :param end_milestone: The end_milestone of this RequestTrial.
        :type end_milestone: str
        """
        if end_milestone is None:
            raise ValueError("Invalid value for `end_milestone`, must not be `None`")  # noqa: E501

        self._end_milestone = end_milestone

    @property
    def end_time(self) -> RequestTrialEndTime:
        """Gets the end_time of this RequestTrial.


        :return: The end_time of this RequestTrial.
        :rtype: RequestTrialEndTime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: RequestTrialEndTime):
        """Sets the end_time of this RequestTrial.


        :param end_time: The end_time of this RequestTrial.
        :type end_time: RequestTrialEndTime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def description(self) -> str:
        """Gets the description of this RequestTrial.


        :return: The description of this RequestTrial.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this RequestTrial.


        :param description: The description of this RequestTrial.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def documentation_url(self) -> str:
        """Gets the documentation_url of this RequestTrial.


        :return: The documentation_url of this RequestTrial.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url: str):
        """Sets the documentation_url of this RequestTrial.


        :param documentation_url: The documentation_url of this RequestTrial.
        :type documentation_url: str
        """
        if documentation_url is None:
            raise ValueError("Invalid value for `documentation_url`, must not be `None`")  # noqa: E501

        self._documentation_url = documentation_url

    @property
    def feedback_url(self) -> str:
        """Gets the feedback_url of this RequestTrial.


        :return: The feedback_url of this RequestTrial.
        :rtype: str
        """
        return self._feedback_url

    @feedback_url.setter
    def feedback_url(self, feedback_url: str):
        """Sets the feedback_url of this RequestTrial.


        :param feedback_url: The feedback_url of this RequestTrial.
        :type feedback_url: str
        """
        if feedback_url is None:
            raise ValueError("Invalid value for `feedback_url`, must not be `None`")  # noqa: E501

        self._feedback_url = feedback_url

    @property
    def intent_to_experiment_url(self) -> str:
        """Gets the intent_to_experiment_url of this RequestTrial.


        :return: The intent_to_experiment_url of this RequestTrial.
        :rtype: str
        """
        return self._intent_to_experiment_url

    @intent_to_experiment_url.setter
    def intent_to_experiment_url(self, intent_to_experiment_url: str):
        """Sets the intent_to_experiment_url of this RequestTrial.


        :param intent_to_experiment_url: The intent_to_experiment_url of this RequestTrial.
        :type intent_to_experiment_url: str
        """
        if intent_to_experiment_url is None:
            raise ValueError("Invalid value for `intent_to_experiment_url`, must not be `None`")  # noqa: E501

        self._intent_to_experiment_url = intent_to_experiment_url

    @property
    def chromestatus_url(self) -> str:
        """Gets the chromestatus_url of this RequestTrial.


        :return: The chromestatus_url of this RequestTrial.
        :rtype: str
        """
        return self._chromestatus_url

    @chromestatus_url.setter
    def chromestatus_url(self, chromestatus_url: str):
        """Sets the chromestatus_url of this RequestTrial.


        :param chromestatus_url: The chromestatus_url of this RequestTrial.
        :type chromestatus_url: str
        """
        if chromestatus_url is None:
            raise ValueError("Invalid value for `chromestatus_url`, must not be `None`")  # noqa: E501

        self._chromestatus_url = chromestatus_url

    @property
    def allow_third_party_origins(self) -> bool:
        """Gets the allow_third_party_origins of this RequestTrial.


        :return: The allow_third_party_origins of this RequestTrial.
        :rtype: bool
        """
        return self._allow_third_party_origins

    @allow_third_party_origins.setter
    def allow_third_party_origins(self, allow_third_party_origins: bool):
        """Sets the allow_third_party_origins of this RequestTrial.


        :param allow_third_party_origins: The allow_third_party_origins of this RequestTrial.
        :type allow_third_party_origins: bool
        """
        if allow_third_party_origins is None:
            raise ValueError("Invalid value for `allow_third_party_origins`, must not be `None`")  # noqa: E501

        self._allow_third_party_origins = allow_third_party_origins

    @property
    def type(self) -> str:
        """Gets the type of this RequestTrial.


        :return: The type of this RequestTrial.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RequestTrial.


        :param type: The type of this RequestTrial.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def origin_trial_feature_name(self) -> str:
        """Gets the origin_trial_feature_name of this RequestTrial.


        :return: The origin_trial_feature_name of this RequestTrial.
        :rtype: str
        """
        return self._origin_trial_feature_name

    @origin_trial_feature_name.setter
    def origin_trial_feature_name(self, origin_trial_feature_name: str):
        """Sets the origin_trial_feature_name of this RequestTrial.


        :param origin_trial_feature_name: The origin_trial_feature_name of this RequestTrial.
        :type origin_trial_feature_name: str
        """

        self._origin_trial_feature_name = origin_trial_feature_name
