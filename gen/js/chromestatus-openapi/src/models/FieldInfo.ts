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
import type { FieldInfoValue } from './FieldInfoValue';
import {
    FieldInfoValueFromJSON,
    FieldInfoValueFromJSONTyped,
    FieldInfoValueToJSON,
} from './FieldInfoValue';

/**
 * 
 * @export
 * @interface FieldInfo
 */
export interface FieldInfo {
    /**
     * 
     * @type {string}
     * @memberof FieldInfo
     */
    form_field_name?: string;
    /**
     * 
     * @type {FieldInfoValue}
     * @memberof FieldInfo
     */
    value?: FieldInfoValue;
}

/**
 * Check if a given object implements the FieldInfo interface.
 */
export function instanceOfFieldInfo(value: object): value is FieldInfo {
    return true;
}

export function FieldInfoFromJSON(json: any): FieldInfo {
    return FieldInfoFromJSONTyped(json, false);
}

export function FieldInfoFromJSONTyped(json: any, ignoreDiscriminator: boolean): FieldInfo {
    if (json == null) {
        return json;
    }
    return {
        
        'form_field_name': json['form_field_name'] == null ? undefined : json['form_field_name'],
        'value': json['value'] == null ? undefined : FieldInfoValueFromJSON(json['value']),
    };
}

export function FieldInfoToJSON(value?: FieldInfo | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'form_field_name': value['form_field_name'],
        'value': FieldInfoValueToJSON(value['value']),
    };
}
