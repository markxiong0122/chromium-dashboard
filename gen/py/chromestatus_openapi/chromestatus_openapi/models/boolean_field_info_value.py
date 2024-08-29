from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class BooleanFieldInfoValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, form_field_name=None, value_type=None, value=None):  # noqa: E501
        """BooleanFieldInfoValue - a model defined in OpenAPI

        :param form_field_name: The form_field_name of this BooleanFieldInfoValue.  # noqa: E501
        :type form_field_name: str
        :param value_type: The value_type of this BooleanFieldInfoValue.  # noqa: E501
        :type value_type: str
        :param value: The value of this BooleanFieldInfoValue.  # noqa: E501
        :type value: bool
        """
        self.openapi_types = {
            'form_field_name': str,
            'value_type': str,
            'value': bool
        }

        self.attribute_map = {
            'form_field_name': 'form_field_name',
            'value_type': 'value_type',
            'value': 'value'
        }

        self._form_field_name = form_field_name
        self._value_type = value_type
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'BooleanFieldInfoValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BooleanFieldInfoValue of this BooleanFieldInfoValue.  # noqa: E501
        :rtype: BooleanFieldInfoValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def form_field_name(self) -> str:
        """Gets the form_field_name of this BooleanFieldInfoValue.


        :return: The form_field_name of this BooleanFieldInfoValue.
        :rtype: str
        """
        return self._form_field_name

    @form_field_name.setter
    def form_field_name(self, form_field_name: str):
        """Sets the form_field_name of this BooleanFieldInfoValue.


        :param form_field_name: The form_field_name of this BooleanFieldInfoValue.
        :type form_field_name: str
        """

        self._form_field_name = form_field_name

    @property
    def value_type(self) -> str:
        """Gets the value_type of this BooleanFieldInfoValue.


        :return: The value_type of this BooleanFieldInfoValue.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type: str):
        """Sets the value_type of this BooleanFieldInfoValue.


        :param value_type: The value_type of this BooleanFieldInfoValue.
        :type value_type: str
        """

        self._value_type = value_type

    @property
    def value(self) -> bool:
        """Gets the value of this BooleanFieldInfoValue.


        :return: The value of this BooleanFieldInfoValue.
        :rtype: bool
        """
        return self._value

    @value.setter
    def value(self, value: bool):
        """Sets the value of this BooleanFieldInfoValue.


        :param value: The value of this BooleanFieldInfoValue.
        :type value: bool
        """

        self._value = value