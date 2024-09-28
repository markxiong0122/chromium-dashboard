# coding: utf-8

"""
    chomestatus API

    The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chromestatus_openapi.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_add_feature_comment(self) -> None:
        """Test case for add_feature_comment

        Add a comment to a feature
        """
        pass

    def test_add_gate_comment(self) -> None:
        """Test case for add_gate_comment

        Add a comment to a specific gate
        """
        pass

    def test_add_user_to_component(self) -> None:
        """Test case for add_user_to_component

        Add a user to a component
        """
        pass

    def test_add_xfn_gates_to_stage(self) -> None:
        """Test case for add_xfn_gates_to_stage

        Add a full set of cross-functional gates to a stage.
        """
        pass

    def test_authenticate_user(self) -> None:
        """Test case for authenticate_user

        Authenticate user with Google Sign-In
        """
        pass

    def test_create_account(self) -> None:
        """Test case for create_account

        Create a new account
        """
        pass

    def test_create_origin_trial(self) -> None:
        """Test case for create_origin_trial

        Create a new origin trial
        """
        pass

    def test_delete_account(self) -> None:
        """Test case for delete_account

        Delete an account
        """
        pass

    def test_dismiss_cue(self) -> None:
        """Test case for dismiss_cue

        Dismiss a cue card for the signed-in user
        """
        pass

    def test_extend_origin_trial(self) -> None:
        """Test case for extend_origin_trial

        Extend an existing origin trial
        """
        pass

    def test_get_dismissed_cues(self) -> None:
        """Test case for get_dismissed_cues

        Get dismissed cues for the current user
        """
        pass

    def test_get_feature_comments(self) -> None:
        """Test case for get_feature_comments

        Get all comments for a given feature
        """
        pass

    def test_get_feature_links(self) -> None:
        """Test case for get_feature_links

        Get feature links by feature_id
        """
        pass

    def test_get_feature_links_samples(self) -> None:
        """Test case for get_feature_links_samples

        Get feature links samples
        """
        pass

    def test_get_feature_links_summary(self) -> None:
        """Test case for get_feature_links_summary

        Get feature links summary
        """
        pass

    def test_get_gate_comments(self) -> None:
        """Test case for get_gate_comments

        Get all comments for a given gate
        """
        pass

    def test_get_gates_for_feature(self) -> None:
        """Test case for get_gates_for_feature

        Get all gates for a feature
        """
        pass

    def test_get_intent_body(self) -> None:
        """Test case for get_intent_body

        Get the HTML body of an intent draft
        """
        pass

    def test_get_origin_trials(self) -> None:
        """Test case for get_origin_trials

        Get origin trials
        """
        pass

    def test_get_pending_gates(self) -> None:
        """Test case for get_pending_gates

        Get all pending gates
        """
        pass

    def test_get_process(self) -> None:
        """Test case for get_process

        Get the process for a feature
        """
        pass

    def test_get_progress(self) -> None:
        """Test case for get_progress

        Get the progress for a feature
        """
        pass

    def test_get_stars(self) -> None:
        """Test case for get_stars

        Get a list of all starred feature IDs for the signed-in user
        """
        pass

    def test_get_user_permissions(self) -> None:
        """Test case for get_user_permissions

        Get the permissions and email of the user
        """
        pass

    def test_get_user_settings(self) -> None:
        """Test case for get_user_settings

        Get user settings
        """
        pass

    def test_get_votes_for_feature(self) -> None:
        """Test case for get_votes_for_feature

        Get votes for a feature
        """
        pass

    def test_get_votes_for_feature_and_gate(self) -> None:
        """Test case for get_votes_for_feature_and_gate

        Get votes for a feature and gate
        """
        pass

    def test_list_component_users(self) -> None:
        """Test case for list_component_users

        List all components and possible users
        """
        pass

    def test_list_external_reviews(self) -> None:
        """Test case for list_external_reviews

        List features whose external reviews are incomplete
        """
        pass

    def test_list_feature_latency(self) -> None:
        """Test case for list_feature_latency

        List how long each feature took to launch
        """
        pass

    def test_list_reviews_with_latency(self) -> None:
        """Test case for list_reviews_with_latency

        List recently reviewed features and their review latency
        """
        pass

    def test_list_spec_mentors(self) -> None:
        """Test case for list_spec_mentors

        List spec mentors and their activity
        """
        pass

    def test_logout_user(self) -> None:
        """Test case for logout_user

        Log out the current user
        """
        pass

    def test_post_intent_to_blink_dev(self) -> None:
        """Test case for post_intent_to_blink_dev

        Submit an intent to be posted on blink-dev
        """
        pass

    def test_refresh_token(self) -> None:
        """Test case for refresh_token

        Refresh the XSRF token
        """
        pass

    def test_reject_get_requests_login(self) -> None:
        """Test case for reject_get_requests_login

        reject unneeded GET request without triggering Error Reporting
        """
        pass

    def test_reject_get_requests_logout(self) -> None:
        """Test case for reject_get_requests_logout

        reject unneeded GET request without triggering Error Reporting
        """
        pass

    def test_remove_user_from_component(self) -> None:
        """Test case for remove_user_from_component

        Remove a user from a component
        """
        pass

    def test_set_assignees_for_gate(self) -> None:
        """Test case for set_assignees_for_gate

        Set the assignees for a gate.
        """
        pass

    def test_set_star(self) -> None:
        """Test case for set_star

        Set or clear a star on the specified feature
        """
        pass

    def test_set_user_settings(self) -> None:
        """Test case for set_user_settings

        Set the user settings (currently only the notify_as_starrer)
        """
        pass

    def test_set_vote_for_feature_and_gate(self) -> None:
        """Test case for set_vote_for_feature_and_gate

        Set a user's vote value for the specific feature and gate.
        """
        pass

    def test_update_feature_comment(self) -> None:
        """Test case for update_feature_comment

        Update a comment on a feature
        """
        pass


if __name__ == '__main__':
    unittest.main()