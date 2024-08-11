from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.internal_registration_config import InternalRegistrationConfig
from chromestatus_openapi.models.request_trial import RequestTrial
from chromestatus_openapi import util

from chromestatus_openapi.models.internal_registration_config import InternalRegistrationConfig  # noqa: E501
from chromestatus_openapi.models.request_trial import RequestTrial  # noqa: E501

class CreateOriginTrialRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, trial=None, registration_config=None, trial_contacts=None):  # noqa: E501
        """CreateOriginTrialRequest - a model defined in OpenAPI

        :param trial: The trial of this CreateOriginTrialRequest.  # noqa: E501
        :type trial: RequestTrial
        :param registration_config: The registration_config of this CreateOriginTrialRequest.  # noqa: E501
        :type registration_config: InternalRegistrationConfig
        :param trial_contacts: The trial_contacts of this CreateOriginTrialRequest.  # noqa: E501
        :type trial_contacts: List[str]
        """
        self.openapi_types = {
            'trial': RequestTrial,
            'registration_config': InternalRegistrationConfig,
            'trial_contacts': List[str]
        }

        self.attribute_map = {
            'trial': 'trial',
            'registration_config': 'registration_config',
            'trial_contacts': 'trial_contacts'
        }

        self._trial = trial
        self._registration_config = registration_config
        self._trial_contacts = trial_contacts

    @classmethod
    def from_dict(cls, dikt) -> 'CreateOriginTrialRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateOriginTrialRequest of this CreateOriginTrialRequest.  # noqa: E501
        :rtype: CreateOriginTrialRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def trial(self) -> RequestTrial:
        """Gets the trial of this CreateOriginTrialRequest.


        :return: The trial of this CreateOriginTrialRequest.
        :rtype: RequestTrial
        """
        return self._trial

    @trial.setter
    def trial(self, trial: RequestTrial):
        """Sets the trial of this CreateOriginTrialRequest.


        :param trial: The trial of this CreateOriginTrialRequest.
        :type trial: RequestTrial
        """

        self._trial = trial

    @property
    def registration_config(self) -> InternalRegistrationConfig:
        """Gets the registration_config of this CreateOriginTrialRequest.


        :return: The registration_config of this CreateOriginTrialRequest.
        :rtype: InternalRegistrationConfig
        """
        return self._registration_config

    @registration_config.setter
    def registration_config(self, registration_config: InternalRegistrationConfig):
        """Sets the registration_config of this CreateOriginTrialRequest.


        :param registration_config: The registration_config of this CreateOriginTrialRequest.
        :type registration_config: InternalRegistrationConfig
        """

        self._registration_config = registration_config

    @property
    def trial_contacts(self) -> List[str]:
        """Gets the trial_contacts of this CreateOriginTrialRequest.


        :return: The trial_contacts of this CreateOriginTrialRequest.
        :rtype: List[str]
        """
        return self._trial_contacts

    @trial_contacts.setter
    def trial_contacts(self, trial_contacts: List[str]):
        """Sets the trial_contacts of this CreateOriginTrialRequest.


        :param trial_contacts: The trial_contacts of this CreateOriginTrialRequest.
        :type trial_contacts: List[str]
        """

        self._trial_contacts = trial_contacts
