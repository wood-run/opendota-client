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


class ScenariosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def scenarios_item_timings_get(self, **kwargs):  # noqa: E501
        """GET /scenarios/itemTimings  # noqa: E501

        Win rates for certain item timings on a hero for items that cost at least 1400 gold  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenarios_item_timings_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str item: Filter by item name e.g. \"spirit_vessel\"
        :param int hero_id: Hero ID
        :return: list[InlineResponse20034]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenarios_item_timings_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scenarios_item_timings_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def scenarios_item_timings_get_with_http_info(self, **kwargs):  # noqa: E501
        """GET /scenarios/itemTimings  # noqa: E501

        Win rates for certain item timings on a hero for items that cost at least 1400 gold  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenarios_item_timings_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str item: Filter by item name e.g. \"spirit_vessel\"
        :param int hero_id: Hero ID
        :return: list[InlineResponse20034]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item', 'hero_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenarios_item_timings_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'item' in params:
            query_params.append(('item', params['item']))  # noqa: E501
        if 'hero_id' in params:
            query_params.append(('hero_id', params['hero_id']))  # noqa: E501

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
            '/scenarios/itemTimings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20034]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scenarios_lane_roles_get(self, **kwargs):  # noqa: E501
        """GET /scenarios/laneRoles  # noqa: E501

        Win rates for heroes in certain lane roles  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenarios_lane_roles_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lane_role: Filter by lane role 1-4 (Safe, Mid, Off, Jungle)
        :param int hero_id: Hero ID
        :return: list[InlineResponse20035]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenarios_lane_roles_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scenarios_lane_roles_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def scenarios_lane_roles_get_with_http_info(self, **kwargs):  # noqa: E501
        """GET /scenarios/laneRoles  # noqa: E501

        Win rates for heroes in certain lane roles  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenarios_lane_roles_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str lane_role: Filter by lane role 1-4 (Safe, Mid, Off, Jungle)
        :param int hero_id: Hero ID
        :return: list[InlineResponse20035]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lane_role', 'hero_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenarios_lane_roles_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'lane_role' in params:
            query_params.append(('lane_role', params['lane_role']))  # noqa: E501
        if 'hero_id' in params:
            query_params.append(('hero_id', params['hero_id']))  # noqa: E501

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
            '/scenarios/laneRoles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20035]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def scenarios_misc_get(self, **kwargs):  # noqa: E501
        """GET /scenarios/misc  # noqa: E501

        Miscellaneous team scenarios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenarios_misc_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scenario: pos_chat_1min,neg_chat_1min,courier_kill,first_blood
        :return: list[InlineResponse20036]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.scenarios_misc_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.scenarios_misc_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def scenarios_misc_get_with_http_info(self, **kwargs):  # noqa: E501
        """GET /scenarios/misc  # noqa: E501

        Miscellaneous team scenarios  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.scenarios_misc_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str scenario: pos_chat_1min,neg_chat_1min,courier_kill,first_blood
        :return: list[InlineResponse20036]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scenario']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scenarios_misc_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scenario' in params:
            query_params.append(('scenario', params['scenario']))  # noqa: E501

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
            '/scenarios/misc', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20036]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)