# coding: utf-8

"""
    chomestatus API

    The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chromestatus_openapi.models.link_preview_google_docs import LinkPreviewGoogleDocs

class TestLinkPreviewGoogleDocs(unittest.TestCase):
    """LinkPreviewGoogleDocs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkPreviewGoogleDocs:
        """Test LinkPreviewGoogleDocs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkPreviewGoogleDocs`
        """
        model = LinkPreviewGoogleDocs()
        if include_optional:
            return LinkPreviewGoogleDocs(
                url = '',
                type = '',
                information = chromestatus_openapi.models.link_preview_open_graph_all_of_information.LinkPreviewOpenGraph_allOf_information(
                    title = '', 
                    description = '', ),
                http_error_code = 56
            )
        else:
            return LinkPreviewGoogleDocs(
                url = '',
                type = '',
                information = chromestatus_openapi.models.link_preview_open_graph_all_of_information.LinkPreviewOpenGraph_allOf_information(
                    title = '', 
                    description = '', ),
                http_error_code = 56,
        )
        """

    def testLinkPreviewGoogleDocs(self):
        """Test LinkPreviewGoogleDocs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
