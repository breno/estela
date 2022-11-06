/* tslint:disable */
/* eslint-disable */
/**
 * estela API v1.0 Documentation
 * estela API Swagger Specification
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * Cron job tags.
 * @export
 * @interface SpiderJobTag
 */
export interface SpiderJobTag {
    /**
     * Tag name.
     * @type {string}
     * @memberof SpiderJobTag
     */
    name: string;
}

export function SpiderJobTagFromJSON(json: any): SpiderJobTag {
    return SpiderJobTagFromJSONTyped(json, false);
}

export function SpiderJobTagFromJSONTyped(json: any, ignoreDiscriminator: boolean): SpiderJobTag {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': json['name'],
    };
}

export function SpiderJobTagToJSON(value?: SpiderJobTag | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
    };
}


