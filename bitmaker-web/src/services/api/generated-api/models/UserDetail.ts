/* tslint:disable */
/* eslint-disable */
/**
 * Bitmaker API v1.0 Documentation
 * Bitmaker API Swagger Specification
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
 * 
 * @export
 * @interface UserDetail
 */
export interface UserDetail {
    /**
     * Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
     * @type {string}
     * @memberof UserDetail
     */
    username: string;
    /**
     * 
     * @type {string}
     * @memberof UserDetail
     */
    email?: string;
}

export function UserDetailFromJSON(json: any): UserDetail {
    return UserDetailFromJSONTyped(json, false);
}

export function UserDetailFromJSONTyped(json: any, ignoreDiscriminator: boolean): UserDetail {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'username': json['username'],
        'email': !exists(json, 'email') ? undefined : json['email'],
    };
}

export function UserDetailToJSON(value?: UserDetail | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'username': value.username,
        'email': value.email,
    };
}

