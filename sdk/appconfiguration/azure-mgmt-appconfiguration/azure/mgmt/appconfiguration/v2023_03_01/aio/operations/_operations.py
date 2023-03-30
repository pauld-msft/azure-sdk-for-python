# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operations import (
    build_check_name_availability_request,
    build_list_request,
    build_regional_check_name_availability_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class Operations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appconfiguration.v2023_03_01.aio.AppConfigurationManagementClient`'s
        :attr:`operations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def check_name_availability(
        self,
        check_name_availability_parameters: _models.CheckNameAvailabilityParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.v2023_03_01.models.CheckNameAvailabilityParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.v2023_03_01.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def check_name_availability(
        self, check_name_availability_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.v2023_03_01.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def check_name_availability(
        self, check_name_availability_parameters: Union[_models.CheckNameAvailabilityParameters, IO], **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request. Is either a CheckNameAvailabilityParameters type or a IO type. Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.v2023_03_01.models.CheckNameAvailabilityParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.v2023_03_01.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.NameAvailabilityStatus] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_parameters, (IO, bytes)):
            _content = check_name_availability_parameters
        else:
            _json = self._serialize.body(check_name_availability_parameters, "CheckNameAvailabilityParameters")

        request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NameAvailabilityStatus", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/checkNameAvailability"
    }

    @distributed_trace
    def list(self, skip_token: Optional[str] = None, **kwargs: Any) -> AsyncIterable["_models.OperationDefinition"]:
        """Lists the operations available from this provider.

        :param skip_token: A skip token is used to continue retrieving items after an operation returns
         a partial result. If a previous response contains a nextLink element, the value of the nextLink
         element will include a skipToken parameter that specifies a starting point to use for
         subsequent calls. Default value is None.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OperationDefinition or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.appconfiguration.v2023_03_01.models.OperationDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01"))
        cls: ClsType[_models.OperationDefinitionListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    skip_token=skip_token,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("OperationDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/providers/Microsoft.AppConfiguration/operations"}

    @overload
    async def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: _models.CheckNameAvailabilityParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.v2023_03_01.models.CheckNameAvailabilityParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.v2023_03_01.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request. Required.
        :type check_name_availability_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.v2023_03_01.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: Union[_models.CheckNameAvailabilityParameters, IO],
        **kwargs: Any
    ) -> _models.NameAvailabilityStatus:
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request. Is either a CheckNameAvailabilityParameters type or a IO type. Required.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.v2023_03_01.models.CheckNameAvailabilityParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.v2023_03_01.models.NameAvailabilityStatus
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.NameAvailabilityStatus] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_parameters, (IO, bytes)):
            _content = check_name_availability_parameters
        else:
            _json = self._serialize.body(check_name_availability_parameters, "CheckNameAvailabilityParameters")

        request = build_regional_check_name_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.regional_check_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("NameAvailabilityStatus", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regional_check_name_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/locations/{location}/checkNameAvailability"
    }