# coding: utf-8

"""
    chomestatus API

    The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from chromestatus_openapi.models.link_preview_open_graph_all_of_information import LinkPreviewOpenGraphAllOfInformation
from typing import Optional, Set
from typing_extensions import Self

class LinkPreviewWebkitBug(BaseModel):
    """
    LinkPreviewWebkitBug
    """ # noqa: E501
    url: StrictStr
    type: StrictStr
    information: LinkPreviewOpenGraphAllOfInformation
    http_error_code: StrictInt
    __properties: ClassVar[List[str]] = ["url", "type", "information", "http_error_code"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LinkPreviewWebkitBug from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of information
        if self.information:
            _dict['information'] = self.information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LinkPreviewWebkitBug from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "type": obj.get("type"),
            "information": LinkPreviewOpenGraphAllOfInformation.from_dict(obj["information"]) if obj.get("information") is not None else None,
            "http_error_code": obj.get("http_error_code")
        })
        return _obj


<<<<<<< HEAD
        :return: The url of this LinkPreviewWebkitBug.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this LinkPreviewWebkitBug.


        :param url: The url of this LinkPreviewWebkitBug.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def type(self) -> str:
        """Gets the type of this LinkPreviewWebkitBug.


        :return: The type of this LinkPreviewWebkitBug.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this LinkPreviewWebkitBug.


        :param type: The type of this LinkPreviewWebkitBug.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def information(self) -> LinkPreviewOpenGraphAllOfInformation:
        """Gets the information of this LinkPreviewWebkitBug.


        :return: The information of this LinkPreviewWebkitBug.
        :rtype: LinkPreviewOpenGraphAllOfInformation
        """
        return self._information

    @information.setter
    def information(self, information: LinkPreviewOpenGraphAllOfInformation):
        """Sets the information of this LinkPreviewWebkitBug.


        :param information: The information of this LinkPreviewWebkitBug.
        :type information: LinkPreviewOpenGraphAllOfInformation
        """

        self._information = information

    @property
    def http_error_code(self) -> int:
        """Gets the http_error_code of this LinkPreviewWebkitBug.


        :return: The http_error_code of this LinkPreviewWebkitBug.
        :rtype: int
        """
        return self._http_error_code

    @http_error_code.setter
    def http_error_code(self, http_error_code: int):
        """Sets the http_error_code of this LinkPreviewWebkitBug.


        :param http_error_code: The http_error_code of this LinkPreviewWebkitBug.
        :type http_error_code: int
        """

        self._http_error_code = http_error_code
||||||| 76d0ce7e
        :return: The url of this LinkPreviewWebkitBug.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this LinkPreviewWebkitBug.


        :param url: The url of this LinkPreviewWebkitBug.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def type(self) -> str:
        """Gets the type of this LinkPreviewWebkitBug.


        :return: The type of this LinkPreviewWebkitBug.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this LinkPreviewWebkitBug.


        :param type: The type of this LinkPreviewWebkitBug.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def information(self) -> LinkPreviewOpenGraphAllOfInformation:
        """Gets the information of this LinkPreviewWebkitBug.


        :return: The information of this LinkPreviewWebkitBug.
        :rtype: LinkPreviewOpenGraphAllOfInformation
        """
        return self._information

    @information.setter
    def information(self, information: LinkPreviewOpenGraphAllOfInformation):
        """Sets the information of this LinkPreviewWebkitBug.


        :param information: The information of this LinkPreviewWebkitBug.
        :type information: LinkPreviewOpenGraphAllOfInformation
        """
        if information is None:
            raise ValueError("Invalid value for `information`, must not be `None`")  # noqa: E501

        self._information = information

    @property
    def http_error_code(self) -> int:
        """Gets the http_error_code of this LinkPreviewWebkitBug.


        :return: The http_error_code of this LinkPreviewWebkitBug.
        :rtype: int
        """
        return self._http_error_code

    @http_error_code.setter
    def http_error_code(self, http_error_code: int):
        """Sets the http_error_code of this LinkPreviewWebkitBug.


        :param http_error_code: The http_error_code of this LinkPreviewWebkitBug.
        :type http_error_code: int
        """
        if http_error_code is None:
            raise ValueError("Invalid value for `http_error_code`, must not be `None`")  # noqa: E501

        self._http_error_code = http_error_code
=======
>>>>>>> 9fcb27fe87d90d342617429deb845522889ce21d
