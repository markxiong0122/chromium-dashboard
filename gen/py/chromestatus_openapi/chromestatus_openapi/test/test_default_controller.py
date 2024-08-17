import unittest

from flask import json

from chromestatus_openapi.models.account_response import AccountResponse  # noqa: E501
from chromestatus_openapi.models.component_users_request import ComponentUsersRequest  # noqa: E501
from chromestatus_openapi.models.components_users_response import ComponentsUsersResponse  # noqa: E501
from chromestatus_openapi.models.create_account_request import CreateAccountRequest  # noqa: E501
from chromestatus_openapi.models.delete_account200_response import DeleteAccount200Response  # noqa: E501
from chromestatus_openapi.models.dismiss_cue_request import DismissCueRequest  # noqa: E501
from chromestatus_openapi.models.error_message import ErrorMessage  # noqa: E501
from chromestatus_openapi.models.external_reviews_response import ExternalReviewsResponse  # noqa: E501
from chromestatus_openapi.models.feature_latency import FeatureLatency  # noqa: E501
from chromestatus_openapi.models.feature_links_response import FeatureLinksResponse  # noqa: E501
from chromestatus_openapi.models.feature_links_sample import FeatureLinksSample  # noqa: E501
from chromestatus_openapi.models.feature_links_summary_response import FeatureLinksSummaryResponse  # noqa: E501
from chromestatus_openapi.models.get_dismissed_cues400_response import GetDismissedCues400Response  # noqa: E501
from chromestatus_openapi.models.get_gate_response import GetGateResponse  # noqa: E501
from chromestatus_openapi.models.get_intent_response import GetIntentResponse  # noqa: E501
from chromestatus_openapi.models.get_votes_response import GetVotesResponse  # noqa: E501
from chromestatus_openapi.models.message_response import MessageResponse  # noqa: E501
from chromestatus_openapi.models.permissions_response import PermissionsResponse  # noqa: E501
from chromestatus_openapi.models.post_gate_request import PostGateRequest  # noqa: E501
from chromestatus_openapi.models.post_intent_request import PostIntentRequest  # noqa: E501
from chromestatus_openapi.models.post_vote_request import PostVoteRequest  # noqa: E501
from chromestatus_openapi.models.process import Process  # noqa: E501
from chromestatus_openapi.models.review_latency import ReviewLatency  # noqa: E501
from chromestatus_openapi.models.spec_mentor import SpecMentor  # noqa: E501
from chromestatus_openapi.models.success_message import SuccessMessage  # noqa: E501
from chromestatus_openapi.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_user_to_component(self):
        """Test case for add_user_to_component

        Add a user to a component
        """
        component_users_request = {"owner":True}
        headers = {
            'Content-Type': 'application/json',
            'XsrfToken': 'special-key',
        }
        response = self.client.open(
            '/api/v0/components/{component_id}/users/{user_id}'.format(component_id=56, user_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(component_users_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_xfn_gates_to_stage(self):
        """Test case for add_xfn_gates_to_stage

        Add a full set of cross-functional gates to a stage.
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/stages/{stage_id}/addXfnGates'.format(feature_id=56, stage_id=56),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_account(self):
        """Test case for create_account

        Create a new account
        """
        create_account_request = {"isSiteEditor":True,"isAdmin":True,"email":"email"}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/accounts',
            method='POST',
            headers=headers,
            data=json.dumps(create_account_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_account(self):
        """Test case for delete_account

        Delete an account
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/accounts/{account_id}'.format(account_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dismiss_cue(self):
        """Test case for dismiss_cue

        Dismiss a cue card for the signed-in user
        """
        dismiss_cue_request = {"cue":"progress-checkmarks"}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/currentuser/cues',
            method='POST',
            headers=headers,
            data=json.dumps(dismiss_cue_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dismissed_cues(self):
        """Test case for get_dismissed_cues

        Get dismissed cues for the current user
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/currentuser/cues',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_feature_links(self):
        """Test case for get_feature_links

        Get feature links by feature_id
        """
        query_string = [('feature_id', 56),
                        ('update_stale_links', True)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/feature_links',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_feature_links_samples(self):
        """Test case for get_feature_links_samples

        Get feature links samples
        """
        query_string = [('domain', 'domain_example'),
                        ('type', 'type_example'),
                        ('is_error', True)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/feature_links_samples',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_feature_links_summary(self):
        """Test case for get_feature_links_summary

        Get feature links summary
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/feature_links_summary',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_gates_for_feature(self):
        """Test case for get_gates_for_feature

        Get all gates for a feature
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/gates'.format(feature_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intent_body(self):
        """Test case for get_intent_body

        Get the HTML body of an intent draft
        """
        headers = {
            'Accept': 'application/json:',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/{stage_id}/{gate_id}/intent'.format(feature_id=56, stage_id=56, gate_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pending_gates(self):
        """Test case for get_pending_gates

        Get all pending gates
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/gates/pending',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_process(self):
        """Test case for get_process

        Get the process for a feature
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/process'.format(feature_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_progress(self):
        """Test case for get_progress

        Get the progress for a feature
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/progress'.format(feature_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_permissions(self):
        """Test case for get_user_permissions

        Get the permissions and email of the user
        """
        query_string = [('returnPairedUser', True)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/currentuser/permissions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_votes_for_feature(self):
        """Test case for get_votes_for_feature

        Get votes for a feature
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/votes'.format(feature_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_votes_for_feature_and_gate(self):
        """Test case for get_votes_for_feature_and_gate

        Get votes for a feature and gate
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/votes/{gate_id}'.format(feature_id=56, gate_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
    def test_list_component_users(self):
        """Test case for list_component_users

        List all components and possible users
        """
        headers = {
            'Accept': 'application/json',
            'XsrfToken': 'special-key',
        }
        response = self.client.open(
            '/api/v0/componentsusers',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_external_reviews(self):
        """Test case for list_external_reviews

        List features whose external reviews are incomplete
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/external_reviews/{review_group}'.format(review_group='review_group_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_feature_latency(self):
        """Test case for list_feature_latency

        List how long each feature took to launch
        """
        query_string = [('startAt', '2013-10-20'),
                        ('endAt', '2013-10-20')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/feature-latency',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_reviews_with_latency(self):
        """Test case for list_reviews_with_latency

        List recently reviewed features and their review latency
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/review-latency',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_spec_mentors(self):
        """Test case for list_spec_mentors

        List spec mentors and their activity
        """
        query_string = [('after', '2013-10-20')]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v0/spec_mentors',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_intent_to_blink_dev(self):
        """Test case for post_intent_to_blink_dev

        Submit an intent to be posted on blink-dev
        """
        post_intent_request = {"intent_cc_emails":["intent_cc_emails","intent_cc_emails"],"gate_id":0}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/{stage_id}/{gate_id}/intent'.format(feature_id=56, stage_id=56, gate_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(post_intent_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_user_from_component(self):
        """Test case for remove_user_from_component

        Remove a user from a component
        """
        component_users_request = {"owner":True}
        headers = {
            'Content-Type': 'application/json',
            'XsrfToken': 'special-key',
        }
        response = self.client.open(
            '/api/v0/components/{component_id}/users/{user_id}'.format(component_id=56, user_id=56),
            method='DELETE',
            headers=headers,
            data=json.dumps(component_users_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_assignees_for_gate(self):
        """Test case for set_assignees_for_gate

        Set the assignees for a gate.
        """
        post_gate_request = {"assignees":["assignees","assignees"]}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/gates/{gate_id}'.format(feature_id=56, gate_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(post_gate_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_vote_for_feature_and_gate(self):
        """Test case for set_vote_for_feature_and_gate

        Set a user's vote value for the specific feature and gate.
        """
        post_vote_request = {"state":0}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v0/features/{feature_id}/votes/{gate_id}'.format(feature_id=56, gate_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(post_vote_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
