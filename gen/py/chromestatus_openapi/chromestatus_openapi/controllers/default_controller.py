import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from chromestatus_openapi.models.component_users_request import ComponentUsersRequest  # noqa: E501
from chromestatus_openapi.models.components_users_response import ComponentsUsersResponse  # noqa: E501
from chromestatus_openapi.models.error_message import ErrorMessage  # noqa: E501
from chromestatus_openapi.models.external_reviews_response import ExternalReviewsResponse  # noqa: E501
from chromestatus_openapi.models.feature_latency import FeatureLatency  # noqa: E501
from chromestatus_openapi.models.feature_links_response import FeatureLinksResponse  # noqa: E501
from chromestatus_openapi.models.feature_links_sample import FeatureLinksSample  # noqa: E501
from chromestatus_openapi.models.feature_links_summary_response import FeatureLinksSummaryResponse  # noqa: E501
from chromestatus_openapi.models.get_intent_response import GetIntentResponse  # noqa: E501
from chromestatus_openapi.models.message_response import MessageResponse  # noqa: E501
from chromestatus_openapi.models.post_intent_request import PostIntentRequest  # noqa: E501
from chromestatus_openapi.models.review_latency import ReviewLatency  # noqa: E501
from chromestatus_openapi.models.spec_mentor import SpecMentor  # noqa: E501
from chromestatus_openapi import util


def add_user_to_component(component_id, user_id, component_users_request=None):  # noqa: E501
    """Add a user to a component

     # noqa: E501

    :param component_id: Component ID
    :type component_id: int
    :param user_id: User ID
    :type user_id: int
    :param component_users_request: 
    :type component_users_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        component_users_request = ComponentUsersRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_feature_links(feature_id=None, update_stale_links=None):  # noqa: E501
    """Get feature links by feature_id

     # noqa: E501

    :param feature_id: 
    :type feature_id: int
    :param update_stale_links: 
    :type update_stale_links: bool

    :rtype: Union[FeatureLinksResponse, Tuple[FeatureLinksResponse, int], Tuple[FeatureLinksResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_feature_links_samples(domain=None, type=None, is_error=None):  # noqa: E501
    """Get feature links samples

     # noqa: E501

    :param domain: 
    :type domain: str
    :param type: 
    :type type: str
    :param is_error: 
    :type is_error: bool

    :rtype: Union[FeatureLinksSample, Tuple[FeatureLinksSample, int], Tuple[FeatureLinksSample, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_feature_links_summary():  # noqa: E501
    """Get feature links summary

     # noqa: E501


    :rtype: Union[FeatureLinksSummaryResponse, Tuple[FeatureLinksSummaryResponse, int], Tuple[FeatureLinksSummaryResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_intent_body(feature_id, stage_id, gate_id):  # noqa: E501
    """Get the HTML body of an intent draft

     # noqa: E501

    :param feature_id: Feature ID
    :type feature_id: int
    :param stage_id: Stage ID
    :type stage_id: int
    :param gate_id: Gate ID
    :type gate_id: int

    :rtype: Union[GetIntentResponse, Tuple[GetIntentResponse, int], Tuple[GetIntentResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_component_users():  # noqa: E501
    """List all components and possible users

     # noqa: E501


    :rtype: Union[ComponentsUsersResponse, Tuple[ComponentsUsersResponse, int], Tuple[ComponentsUsersResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_external_reviews(review_group):  # noqa: E501
    """List features whose external reviews are incomplete

     # noqa: E501

    :param review_group: Which review group to focus on:  * &#x60;tag&#x60; - The W3C TAG  * &#x60;gecko&#x60; - The rendering engine that powers Mozilla Firefox  * &#x60;webkit&#x60; - The rendering engine that powers Apple Safari 
    :type review_group: str

    :rtype: Union[ExternalReviewsResponse, Tuple[ExternalReviewsResponse, int], Tuple[ExternalReviewsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_feature_latency(start_at, end_at):  # noqa: E501
    """List how long each feature took to launch

     # noqa: E501

    :param start_at: Start date (RFC 3339, section 5.6, for example, 2017-07-21). The date is inclusive.
    :type start_at: str
    :param end_at: End date (RFC 3339, section 5.6, for example, 2017-07-21). The date is exclusive.
    :type end_at: str

    :rtype: Union[List[FeatureLatency], Tuple[List[FeatureLatency], int], Tuple[List[FeatureLatency], int, Dict[str, str]]
    """
    start_at = util.deserialize_date(start_at)
    end_at = util.deserialize_date(end_at)
    return 'do some magic!'


def list_reviews_with_latency():  # noqa: E501
    """List recently reviewed features and their review latency

     # noqa: E501


    :rtype: Union[List[ReviewLatency], Tuple[List[ReviewLatency], int], Tuple[List[ReviewLatency], int, Dict[str, str]]
    """
    return 'do some magic!'


def list_spec_mentors(after=None):  # noqa: E501
    """List spec mentors and their activity

     # noqa: E501

    :param after: 
    :type after: str

    :rtype: Union[List[SpecMentor], Tuple[List[SpecMentor], int], Tuple[List[SpecMentor], int, Dict[str, str]]
    """
    after = util.deserialize_date(after)
    return 'do some magic!'


def post_intent_to_blink_dev(feature_id, stage_id, gate_id, post_intent_request=None):  # noqa: E501
    """Submit an intent to be posted on blink-dev

     # noqa: E501

    :param feature_id: Feature ID
    :type feature_id: int
    :param stage_id: Stage ID
    :type stage_id: int
    :param gate_id: Gate ID
    :type gate_id: int
    :param post_intent_request: Gate ID and additional users to CC email to.
    :type post_intent_request: dict | bytes

    :rtype: Union[MessageResponse, Tuple[MessageResponse, int], Tuple[MessageResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        post_intent_request = PostIntentRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def remove_user_from_component(component_id, user_id, component_users_request=None):  # noqa: E501
    """Remove a user from a component

     # noqa: E501

    :param component_id: Component ID
    :type component_id: int
    :param user_id: User ID
    :type user_id: int
    :param component_users_request: 
    :type component_users_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        component_users_request = ComponentUsersRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
