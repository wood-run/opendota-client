# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.  You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.  **Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more.   # noqa: E501

    OpenAPI spec version: 18.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from opendota_client.api_client import ApiClient


class RequestApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def request_job_id_get(self, job_id, **kwargs):  # noqa: E501
        """GET /request/{jobId}  # noqa: E501

        Get parse request state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_job_id_get(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID to query. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_job_id_get_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.request_job_id_get_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def request_job_id_get_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """GET /request/{jobId}  # noqa: E501

        Get parse request state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_job_id_get_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID to query. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_job_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `request_job_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/request/{jobId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_match_id_post(self, match_id, **kwargs):  # noqa: E501
        """POST /request/{match_id}  # noqa: E501

        Submit a new parse request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_match_id_post(match_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int match_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_match_id_post_with_http_info(match_id, **kwargs)  # noqa: E501
        else:
            (data) = self.request_match_id_post_with_http_info(match_id, **kwargs)  # noqa: E501
            return data

    def request_match_id_post_with_http_info(self, match_id, **kwargs):  # noqa: E501
        """POST /request/{match_id}  # noqa: E501

        Submit a new parse request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_match_id_post_with_http_info(match_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int match_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_match_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if ('match_id' not in params or
                params['match_id'] is None):
            raise ValueError("Missing the required parameter `match_id` when calling `request_match_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['match_id'] = params['match_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/request/{match_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
