from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class FieldInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, form_field_name=None, value=None):  # noqa: E501
        """FieldInfo - a model defined in OpenAPI

        :param form_field_name: The form_field_name of this FieldInfo.  # noqa: E501
        :type form_field_name: str
        :param value: The value of this FieldInfo.  # noqa: E501
        :type value: object
        """
        self.openapi_types = {
            'form_field_name': str,
            'value': object
        }

        self.attribute_map = {
            'form_field_name': 'form_field_name',
            'value': 'value'
        }

        self._form_field_name = form_field_name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'FieldInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FieldInfo of this FieldInfo.  # noqa: E501
        :rtype: FieldInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def form_field_name(self) -> str:
        """Gets the form_field_name of this FieldInfo.


        :return: The form_field_name of this FieldInfo.
        :rtype: str
        """
        return self._form_field_name

    @form_field_name.setter
    def form_field_name(self, form_field_name: str):
        """Sets the form_field_name of this FieldInfo.


        :param form_field_name: The form_field_name of this FieldInfo.
        :type form_field_name: str
        """

        self._form_field_name = form_field_name

    @property
    def value(self) -> object:
        """Gets the value of this FieldInfo.


        :return: The value of this FieldInfo.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value: object):
        """Sets the value of this FieldInfo.


        :param value: The value of this FieldInfo.
        :type value: object
        """

        self._value = value
