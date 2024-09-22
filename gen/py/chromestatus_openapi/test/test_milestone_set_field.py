# coding: utf-8

"""
    chomestatus API

    The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chromestatus_openapi.models.milestone_set_field import MilestoneSetField

class TestMilestoneSetField(unittest.TestCase):
    """MilestoneSetField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MilestoneSetField:
        """Test MilestoneSetField
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MilestoneSetField`
        """
        model = MilestoneSetField()
        if include_optional:
            return MilestoneSetField(
                desktop_first = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                desktop_last = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                android_first = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                android_last = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                ios_first = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                ios_last = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                webview_first = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, ),
                webview_last = chromestatus_openapi.models.field_info.FieldInfo(
                    form_field_name = '', 
                    value = null, )
            )
        else:
            return MilestoneSetField(
        )
        """

    def testMilestoneSetField(self):
        """Test MilestoneSetField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
