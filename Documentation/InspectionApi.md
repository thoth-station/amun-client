# amun.swagger_client.InspectionApi

All URIs are relative to *https://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inspect_build_log**](InspectionApi.md#get_inspect_build_log) | **GET** /inspect/{inspection_id}/build/log | Get log for a specific inspection build.
[**get_inspect_build_status**](InspectionApi.md#get_inspect_build_status) | **GET** /inspect/{inspection_id}/build/status | Get status of a build run.
[**get_inspect_job_log**](InspectionApi.md#get_inspect_job_log) | **GET** /inspect/{inspection_id}/job/log | Get log for a specific inspection run.
[**get_inspect_job_status**](InspectionApi.md#get_inspect_job_status) | **GET** /inspect/{inspection_id}/job/status | Get status of the application run.
[**post_inspect**](InspectionApi.md#post_inspect) | **POST** /inspect | Inspect the given application stack.


# **get_inspect_build_log**
> InspectionBuildLogResponse get_inspect_build_log(inspection_id)

Get log for a specific inspection build.

### Example
```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amun.swagger_client.InspectionApi()
inspection_id = 'inspection_id_example' # str | Id of inspection build.

try:
    # Get log for a specific inspection build.
    api_response = api_instance.get_inspect_build_log(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspect_build_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_id** | **str**| Id of inspection build. | 

### Return type

[**InspectionBuildLogResponse**](InspectionBuildLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspect_build_status**
> InspectionBuildStatusResponse get_inspect_build_status(inspection_id)

Get status of a build run.

### Example
```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amun.swagger_client.InspectionApi()
inspection_id = 'inspection_id_example' # str | Id of inspection run.

try:
    # Get status of a build run.
    api_response = api_instance.get_inspect_build_status(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspect_build_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_id** | **str**| Id of inspection run. | 

### Return type

[**InspectionBuildStatusResponse**](InspectionBuildStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspect_job_log**
> InspectionJobLogResponse get_inspect_job_log(inspection_id)

Get log for a specific inspection run.

### Example
```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amun.swagger_client.InspectionApi()
inspection_id = 'inspection_id_example' # str | Id of inspection run.

try:
    # Get log for a specific inspection run.
    api_response = api_instance.get_inspect_job_log(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspect_job_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_id** | **str**| Id of inspection run. | 

### Return type

[**InspectionJobLogResponse**](InspectionJobLogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspect_job_status**
> InspectionJobStatusResponse get_inspect_job_status(inspection_id)

Get status of the application run.

### Example
```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amun.swagger_client.InspectionApi()
inspection_id = 'inspection_id_example' # str | Id of inspection run.

try:
    # Get status of the application run.
    api_response = api_instance.get_inspect_job_status(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspect_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_id** | **str**| Id of inspection run. | 

### Return type

[**InspectionJobStatusResponse**](InspectionJobStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_inspect**
> InspectionResponse post_inspect(specification)

Inspect the given application stack.

### Example
```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amun.swagger_client.InspectionApi()
specification = amun.swagger_client.InspectionSpecification() # InspectionSpecification | Base image to be used for runtime environment.

try:
    # Inspect the given application stack.
    api_response = api_instance.post_inspect(specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->post_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specification** | [**InspectionSpecification**](InspectionSpecification.md)| Base image to be used for runtime environment. | 

### Return type

[**InspectionResponse**](InspectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

