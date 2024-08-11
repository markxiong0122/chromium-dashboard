/* tslint:disable */
/* eslint-disable */
/**
 * chomestatus API
 * The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
import type { RequestTrialEndTime } from './RequestTrialEndTime';
import {
    RequestTrialEndTimeFromJSON,
    RequestTrialEndTimeFromJSONTyped,
    RequestTrialEndTimeToJSON,
} from './RequestTrialEndTime';

/**
 * 
 * @export
 * @interface RequestTrial
 */
export interface RequestTrial {
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    display_name: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    start_milestone: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    end_milestone: string;
    /**
     * 
     * @type {RequestTrialEndTime}
     * @memberof RequestTrial
     */
    end_time: RequestTrialEndTime;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    description: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    documentation_url: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    feedback_url: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    intent_to_experiment_url: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    chromestatus_url: string;
    /**
     * 
     * @type {boolean}
     * @memberof RequestTrial
     */
    allow_third_party_origins: boolean;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    type: string;
    /**
     * 
     * @type {string}
     * @memberof RequestTrial
     */
    origin_trial_feature_name?: string;
}

/**
 * Check if a given object implements the RequestTrial interface.
 */
export function instanceOfRequestTrial(value: object): value is RequestTrial {
    if (!('display_name' in value) || value['display_name'] === undefined) return false;
    if (!('start_milestone' in value) || value['start_milestone'] === undefined) return false;
    if (!('end_milestone' in value) || value['end_milestone'] === undefined) return false;
    if (!('end_time' in value) || value['end_time'] === undefined) return false;
    if (!('description' in value) || value['description'] === undefined) return false;
    if (!('documentation_url' in value) || value['documentation_url'] === undefined) return false;
    if (!('feedback_url' in value) || value['feedback_url'] === undefined) return false;
    if (!('intent_to_experiment_url' in value) || value['intent_to_experiment_url'] === undefined) return false;
    if (!('chromestatus_url' in value) || value['chromestatus_url'] === undefined) return false;
    if (!('allow_third_party_origins' in value) || value['allow_third_party_origins'] === undefined) return false;
    if (!('type' in value) || value['type'] === undefined) return false;
    return true;
}

export function RequestTrialFromJSON(json: any): RequestTrial {
    return RequestTrialFromJSONTyped(json, false);
}

export function RequestTrialFromJSONTyped(json: any, ignoreDiscriminator: boolean): RequestTrial {
    if (json == null) {
        return json;
    }
    return {
        
        'display_name': json['display_name'],
        'start_milestone': json['start_milestone'],
        'end_milestone': json['end_milestone'],
        'end_time': RequestTrialEndTimeFromJSON(json['end_time']),
        'description': json['description'],
        'documentation_url': json['documentation_url'],
        'feedback_url': json['feedback_url'],
        'intent_to_experiment_url': json['intent_to_experiment_url'],
        'chromestatus_url': json['chromestatus_url'],
        'allow_third_party_origins': json['allow_third_party_origins'],
        'type': json['type'],
        'origin_trial_feature_name': json['origin_trial_feature_name'] == null ? undefined : json['origin_trial_feature_name'],
    };
}

export function RequestTrialToJSON(value?: RequestTrial | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'display_name': value['display_name'],
        'start_milestone': value['start_milestone'],
        'end_milestone': value['end_milestone'],
        'end_time': RequestTrialEndTimeToJSON(value['end_time']),
        'description': value['description'],
        'documentation_url': value['documentation_url'],
        'feedback_url': value['feedback_url'],
        'intent_to_experiment_url': value['intent_to_experiment_url'],
        'chromestatus_url': value['chromestatus_url'],
        'allow_third_party_origins': value['allow_third_party_origins'],
        'type': value['type'],
        'origin_trial_feature_name': value['origin_trial_feature_name'],
    };
}

