# coding: utf-8

"""
    chomestatus API

    The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chromestatus_openapi.models.feature_dict_inner_view_info import FeatureDictInnerViewInfo

class TestFeatureDictInnerViewInfo(unittest.TestCase):
    """FeatureDictInnerViewInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeatureDictInnerViewInfo:
        """Test FeatureDictInnerViewInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeatureDictInnerViewInfo`
        """
        model = FeatureDictInnerViewInfo()
        if include_optional:
            return FeatureDictInnerViewInfo(
                text = '',
                val = 56,
                url = '',
                notes = ''
            )
        else:
            return FeatureDictInnerViewInfo(
        )
        """

    def testFeatureDictInnerViewInfo(self):
        """Test FeatureDictInnerViewInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
