from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class FieldInfoValue(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, string_value=None, integer_value=None, boolean_value=None, array_value=None):  # noqa: E501
        """FieldInfoValue - a model defined in OpenAPI

        :param string_value: The string_value of this FieldInfoValue.  # noqa: E501
        :type string_value: str
        :param integer_value: The integer_value of this FieldInfoValue.  # noqa: E501
        :type integer_value: int
        :param boolean_value: The boolean_value of this FieldInfoValue.  # noqa: E501
        :type boolean_value: bool
        :param array_value: The array_value of this FieldInfoValue.  # noqa: E501
        :type array_value: List[str]
        """
        self.openapi_types = {
            'string_value': str,
            'integer_value': int,
            'boolean_value': bool,
            'array_value': List[str]
        }

        self.attribute_map = {
            'string_value': 'string_value',
            'integer_value': 'integer_value',
            'boolean_value': 'boolean_value',
            'array_value': 'array_value'
        }

        self._string_value = string_value
        self._integer_value = integer_value
        self._boolean_value = boolean_value
        self._array_value = array_value

    @classmethod
    def from_dict(cls, dikt) -> 'FieldInfoValue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FieldInfoValue of this FieldInfoValue.  # noqa: E501
        :rtype: FieldInfoValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def string_value(self) -> str:
        """Gets the string_value of this FieldInfoValue.


        :return: The string_value of this FieldInfoValue.
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value: str):
        """Sets the string_value of this FieldInfoValue.


        :param string_value: The string_value of this FieldInfoValue.
        :type string_value: str
        """

        self._string_value = string_value

    @property
    def integer_value(self) -> int:
        """Gets the integer_value of this FieldInfoValue.


        :return: The integer_value of this FieldInfoValue.
        :rtype: int
        """
        return self._integer_value

    @integer_value.setter
    def integer_value(self, integer_value: int):
        """Sets the integer_value of this FieldInfoValue.


        :param integer_value: The integer_value of this FieldInfoValue.
        :type integer_value: int
        """

        self._integer_value = integer_value

    @property
    def boolean_value(self) -> bool:
        """Gets the boolean_value of this FieldInfoValue.


        :return: The boolean_value of this FieldInfoValue.
        :rtype: bool
        """
        return self._boolean_value

    @boolean_value.setter
    def boolean_value(self, boolean_value: bool):
        """Sets the boolean_value of this FieldInfoValue.


        :param boolean_value: The boolean_value of this FieldInfoValue.
        :type boolean_value: bool
        """

        self._boolean_value = boolean_value

    @property
    def array_value(self) -> List[str]:
        """Gets the array_value of this FieldInfoValue.


        :return: The array_value of this FieldInfoValue.
        :rtype: List[str]
        """
        return self._array_value

    @array_value.setter
    def array_value(self, array_value: List[str]):
        """Sets the array_value of this FieldInfoValue.


        :param array_value: The array_value of this FieldInfoValue.
        :type array_value: List[str]
        """

        self._array_value = array_value
