from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from chromestatus_openapi.models.base_model import Model
from chromestatus_openapi.models.link_preview_base import LinkPreviewBase
from chromestatus_openapi import util

from chromestatus_openapi.models.link_preview_base import LinkPreviewBase  # noqa: E501

class FeatureLinksResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None, has_stale_links=None):  # noqa: E501
        """FeatureLinksResponse - a model defined in OpenAPI

        :param data: The data of this FeatureLinksResponse.  # noqa: E501
        :type data: List[LinkPreviewBase]
        :param has_stale_links: The has_stale_links of this FeatureLinksResponse.  # noqa: E501
        :type has_stale_links: bool
        """
        self.openapi_types = {
            'data': List[LinkPreviewBase],
            'has_stale_links': bool
        }

        self.attribute_map = {
            'data': 'data',
            'has_stale_links': 'has_stale_links'
        }

        self._data = data
        self._has_stale_links = has_stale_links

    @classmethod
    def from_dict(cls, dikt) -> 'FeatureLinksResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FeatureLinksResponse of this FeatureLinksResponse.  # noqa: E501
        :rtype: FeatureLinksResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[LinkPreviewBase]:
        """Gets the data of this FeatureLinksResponse.


        :return: The data of this FeatureLinksResponse.
        :rtype: List[LinkPreviewBase]
        """
        return self._data

    @data.setter
    def data(self, data: List[LinkPreviewBase]):
        """Sets the data of this FeatureLinksResponse.


        :param data: The data of this FeatureLinksResponse.
        :type data: List[LinkPreviewBase]
        """

        self._data = data

    @property
    def has_stale_links(self) -> bool:
        """Gets the has_stale_links of this FeatureLinksResponse.


        :return: The has_stale_links of this FeatureLinksResponse.
        :rtype: bool
        """
        return self._has_stale_links

    @has_stale_links.setter
    def has_stale_links(self, has_stale_links: bool):
        """Sets the has_stale_links of this FeatureLinksResponse.


        :param has_stale_links: The has_stale_links of this FeatureLinksResponse.
        :type has_stale_links: bool
        """

        self._has_stale_links = has_stale_links
