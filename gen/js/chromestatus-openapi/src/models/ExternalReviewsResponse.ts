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

import { exists, mapValues } from '../runtime';
import type { LinkPreview } from './LinkPreview';
import {
    LinkPreviewFromJSON,
    LinkPreviewFromJSONTyped,
    LinkPreviewToJSON,
} from './LinkPreview';
import type { OutstandingReview } from './OutstandingReview';
import {
    OutstandingReviewFromJSON,
    OutstandingReviewFromJSONTyped,
    OutstandingReviewToJSON,
} from './OutstandingReview';

/**
 * 
 * @export
 * @interface ExternalReviewsResponse
 */
export interface ExternalReviewsResponse {
    /**
     * 
     * @type {Array<OutstandingReview>}
     * @memberof ExternalReviewsResponse
     */
    reviews: Array<OutstandingReview>;
    /**
     * 
     * @type {Array<LinkPreview>}
     * @memberof ExternalReviewsResponse
     */
    link_previews: Array<LinkPreview>;
}

/**
 * Check if a given object implements the ExternalReviewsResponse interface.
 */
export function instanceOfExternalReviewsResponse(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "reviews" in value;
    isInstance = isInstance && "link_previews" in value;

    return isInstance;
}

export function ExternalReviewsResponseFromJSON(json: any): ExternalReviewsResponse {
    return ExternalReviewsResponseFromJSONTyped(json, false);
}

export function ExternalReviewsResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): ExternalReviewsResponse {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'reviews': ((json['reviews'] as Array<any>).map(OutstandingReviewFromJSON)),
        'link_previews': ((json['link_previews'] as Array<any>).map(LinkPreviewFromJSON)),
    };
}

export function ExternalReviewsResponseToJSON(value?: ExternalReviewsResponse | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'reviews': ((value.reviews as Array<any>).map(OutstandingReviewToJSON)),
        'link_previews': ((value.link_previews as Array<any>).map(LinkPreviewToJSON)),
    };
}

