from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi import util


class ProcessStageProgressItemsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, _field=None):  # noqa: E501
        """ProcessStageProgressItemsInner - a model defined in OpenAPI

        :param name: The name of this ProcessStageProgressItemsInner.  # noqa: E501
        :type name: str
        :param _field: The _field of this ProcessStageProgressItemsInner.  # noqa: E501
        :type _field: str
        """
        self.openapi_types = {
            'name': str,
            '_field': str
        }

        self.attribute_map = {
            'name': 'name',
            '_field': 'field'
        }

        self._name = name
        self.__field = _field

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessStageProgressItemsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProcessStage_progress_items_inner of this ProcessStageProgressItemsInner.  # noqa: E501
        :rtype: ProcessStageProgressItemsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ProcessStageProgressItemsInner.


        :return: The name of this ProcessStageProgressItemsInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProcessStageProgressItemsInner.


        :param name: The name of this ProcessStageProgressItemsInner.
        :type name: str
        """

        self._name = name

    @property
    def _field(self) -> str:
        """Gets the _field of this ProcessStageProgressItemsInner.


        :return: The _field of this ProcessStageProgressItemsInner.
        :rtype: str
        """
        return self.__field

    @_field.setter
    def _field(self, _field: str):
        """Sets the _field of this ProcessStageProgressItemsInner.


        :param _field: The _field of this ProcessStageProgressItemsInner.
        :type _field: str
        """

        self.__field = _field
