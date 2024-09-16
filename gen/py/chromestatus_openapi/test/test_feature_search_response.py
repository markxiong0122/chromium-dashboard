# coding: utf-8

"""
    chomestatus API

    The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chromestatus_openapi.models.feature_search_response import FeatureSearchResponse

class TestFeatureSearchResponse(unittest.TestCase):
    """FeatureSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeatureSearchResponse:
        """Test FeatureSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeatureSearchResponse`
        """
        model = FeatureSearchResponse()
        if include_optional:
            return FeatureSearchResponse(
                total_count = 56,
                features = [
                    chromestatus_openapi.models.verbose_feature_dict.VerboseFeatureDict(
                        id = 56, 
                        created = chromestatus_openapi.models.feature_dict_inner_user_edit_info.FeatureDictInnerUserEditInfo(
                            by = '', 
                            when = '', ), 
                        updated = chromestatus_openapi.models.feature_dict_inner_user_edit_info.FeatureDictInnerUserEditInfo(
                            by = '', 
                            when = '', ), 
                        accurate_as_of = '', 
                        creator_email = '', 
                        updater_email = '', 
                        owner_emails = [
                            ''
                            ], 
                        editor_emails = [
                            ''
                            ], 
                        cc_emails = [
                            ''
                            ], 
                        spec_mentor_emails = [
                            ''
                            ], 
                        unlisted = True, 
                        deleted = True, 
                        editors = [
                            ''
                            ], 
                        cc_recipients = [
                            ''
                            ], 
                        spec_mentors = [
                            ''
                            ], 
                        creator = '', 
                        name = '', 
                        summary = '', 
                        category = '', 
                        category_int = 56, 
                        blink_components = [
                            ''
                            ], 
                        star_count = 56, 
                        search_tags = [
                            ''
                            ], 
                        feature_notes = '', 
                        enterprise_feature_categories = [
                            ''
                            ], 
                        feature_type = '', 
                        feature_type_int = 56, 
                        intent_stage = '', 
                        intent_stage_int = 56, 
                        active_stage_id = 56, 
                        bug_url = '', 
                        launch_bug_url = '', 
                        screenshot_links = [
                            ''
                            ], 
                        first_enterprise_notification_milestone = 56, 
                        breaking_change = True, 
                        enterprise_impact = 56, 
                        flag_name = '', 
                        finch_name = '', 
                        non_finch_justification = '', 
                        ongoing_constraints = '', 
                        motivation = '', 
                        devtrial_instructions = '', 
                        activation_risks = '', 
                        measurement = '', 
                        availability_expectation = '', 
                        adoption_expectation = '', 
                        adoption_plan = '', 
                        initial_public_proposal_url = '', 
                        explainer_links = [
                            ''
                            ], 
                        requires_embedder_support = True, 
                        spec_link = '', 
                        api_spec = '', 
                        prefixed = True, 
                        interop_compat_risks = '', 
                        all_platforms = True, 
                        all_platforms_descr = True, 
                        tag_review = '', 
                        non_oss_deps = '', 
                        anticipated_spec_changes = '', 
                        security_risks = '', 
                        tags = [
                            ''
                            ], 
                        tag_review_status = '', 
                        tag_review_status_int = 56, 
                        security_review_status = '', 
                        security_review_status_int = 56, 
                        privacy_review_status = '', 
                        privacy_review_status_int = 56, 
                        ergonomics_risks = '', 
                        wpt = True, 
                        wpt_descr = '', 
                        webview_risks = '', 
                        devrel_emails = [
                            ''
                            ], 
                        debuggability = '', 
                        doc_links = [
                            ''
                            ], 
                        sample_links = [
                            ''
                            ], 
                        stages = [
                            chromestatus_openapi.models.stage_dict.StageDict(
                                id = 56, 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                feature_id = 56, 
                                stage_type = 56, 
                                display_name = '', 
                                intent_stage = 56, 
                                intent_thread_url = '', 
                                announcement_url = '', 
                                origin_trial_id = '', 
                                experiment_goals = '', 
                                experiment_risks = '', 
                                extensions = [
                                    chromestatus_openapi.models.stage_dict_extension.StageDictExtension(
                                        id = 56, 
                                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        feature_id = 56, 
                                        stage_type = 56, 
                                        display_name = '', 
                                        intent_stage = 56, 
                                        intent_thread_url = '', 
                                        announcement_url = '', 
                                        origin_trial_id = '', 
                                        experiment_goals = '', 
                                        experiment_risks = '', 
                                        origin_trial_feedback_url = '', 
                                        ot_action_requested = True, 
                                        ot_activation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        ot_approval_buganizer_component = 56, 
                                        ot_approval_buganizer_custom_field_id = 56, 
                                        ot_approval_criteria_url = '', 
                                        ot_approval_group_email = '', 
                                        ot_chromium_trial_name = '', 
                                        ot_description = '', 
                                        ot_display_name = '', 
                                        ot_documentation_url = '', 
                                        ot_emails = [
                                            ''
                                            ], 
                                        ot_feedback_submission_url = '', 
                                        ot_has_third_party_support = True, 
                                        ot_is_critical_trial = True, 
                                        ot_is_deprecation_trial = True, 
                                        ot_owner_email = '', 
                                        ot_require_approvals = True, 
                                        ot_setup_status = 56, 
                                        ot_webfeature_use_counter = '', 
                                        ot_request_note = '', 
                                        ot_stage_id = 56, 
                                        experiment_extension_reason = '', 
                                        finch_url = '', 
                                        rollout_details = '', 
                                        rollout_impact = 56, 
                                        rollout_milestone = 56, 
                                        rollout_platforms = [
                                            ''
                                            ], 
                                        enterprise_policies = [
                                            ''
                                            ], 
                                        pm_emails = [
                                            ''
                                            ], 
                                        tl_emails = [
                                            ''
                                            ], 
                                        ux_emails = [
                                            ''
                                            ], 
                                        te_emails = [
                                            ''
                                            ], )
                                    ], 
                                origin_trial_feedback_url = '', 
                                ot_action_requested = True, 
                                ot_activation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                ot_approval_buganizer_component = 56, 
                                ot_approval_buganizer_custom_field_id = 56, 
                                ot_approval_criteria_url = '', 
                                ot_approval_group_email = '', 
                                ot_chromium_trial_name = '', 
                                ot_description = '', 
                                ot_display_name = '', 
                                ot_documentation_url = '', 
                                ot_emails = [
                                    ''
                                    ], 
                                ot_feedback_submission_url = '', 
                                ot_has_third_party_support = True, 
                                ot_is_critical_trial = True, 
                                ot_is_deprecation_trial = True, 
                                ot_owner_email = '', 
                                ot_require_approvals = True, 
                                ot_setup_status = 56, 
                                ot_webfeature_use_counter = '', 
                                ot_request_note = '', 
                                ot_stage_id = 56, 
                                experiment_extension_reason = '', 
                                finch_url = '', 
                                rollout_details = '', 
                                rollout_impact = 56, 
                                rollout_milestone = 56, 
                                rollout_platforms = [
                                    ''
                                    ], 
                                enterprise_policies = [
                                    ''
                                    ], 
                                pm_emails = [
                                    ''
                                    ], 
                                tl_emails = [
                                    ''
                                    ], 
                                ux_emails = [
                                    ''
                                    ], 
                                te_emails = [
                                    ''
                                    ], )
                            ], 
                        experiment_timeline = '', 
                        resources = chromestatus_openapi.models.feature_dict_inner_resource_info.FeatureDictInnerResourceInfo(
                            samples = [
                                ''
                                ], 
                            docs = [
                                ''
                                ], ), 
                        comments = '', 
                        ff_views = 56, 
                        safari_views = 56, 
                        web_dev_views = 56, 
                        browsers = chromestatus_openapi.models.feature_browsers_info.FeatureBrowsersInfo(
                            chrome = chromestatus_openapi.models.feature_dict_inner_chrome_browser_info.FeatureDictInnerChromeBrowserInfo(
                                bug = '', 
                                devrel = [
                                    ''
                                    ], 
                                owners = [
                                    ''
                                    ], 
                                origintrial = True, 
                                intervention = True, 
                                prefixed = True, 
                                flag = '', 
                                status = chromestatus_openapi.models.feature_dict_inner_browser_status.FeatureDictInnerBrowserStatus(
                                    text = '', 
                                    val = 56, 
                                    milestone_str = '', ), 
                                desktop = 56, 
                                android = 56, 
                                webview = 56, 
                                ios = 56, ), 
                            ff = chromestatus_openapi.models.feature_dict_inner_single_browser_info.FeatureDictInnerSingleBrowserInfo(
                                view = chromestatus_openapi.models.feature_dict_inner_view_info.FeatureDictInnerViewInfo(
                                    text = '', 
                                    val = 56, 
                                    url = '', 
                                    notes = '', ), ), 
                            safari = chromestatus_openapi.models.feature_dict_inner_single_browser_info.FeatureDictInnerSingleBrowserInfo(), 
                            webdev = , 
                            other = , ), 
                        standards = chromestatus_openapi.models.feature_dict_inner_standards_info.FeatureDictInnerStandardsInfo(
                            spec = '', 
                            maturity = chromestatus_openapi.models.feature_dict_inner_maturity_info.FeatureDictInnerMaturityInfo(
                                text = '', 
                                short_text = '', 
                                val = 56, ), ), 
                        is_released = True, 
                        is_enterprise_feature = True, 
                        updated_display = '', 
                        new_crbug_url = '', )
                    ]
            )
        else:
            return FeatureSearchResponse(
        )
        """

    def testFeatureSearchResponse(self):
        """Test FeatureSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
