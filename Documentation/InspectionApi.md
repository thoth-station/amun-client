# amun.swagger_client.InspectionApi

All URIs are relative to */api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inspection_build_log**](InspectionApi.md#get_inspection_build_log) | **GET** /inspect/{inspection_id}/build/log | Get log for a specific inspection build.
[**get_inspection_job_log**](InspectionApi.md#get_inspection_job_log) | **GET** /inspect/{inspection_id}/job/log | Get log for a specific inspection run.
[**get_inspection_specification**](InspectionApi.md#get_inspection_specification) | **GET** /inspect/{inspection_id}/specification | Get specification of the given inspection.
[**get_inspection_status**](InspectionApi.md#get_inspection_status) | **GET** /inspect/{inspection_id}/status | Get status of an inspection.
[**post_inspection**](InspectionApi.md#post_inspection) | **POST** /inspect | Inspect the given application stack.

# **get_inspection_build_log**
> InspectionBuildLogResponse get_inspection_build_log(inspection_id)

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
    api_response = api_instance.get_inspection_build_log(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspection_build_log: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspection_job_log**
> InspectionJobLogResponse get_inspection_job_log(inspection_id)

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
    api_response = api_instance.get_inspection_job_log(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspection_job_log: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspection_specification**
> InspectionSpecificationResponse get_inspection_specification(inspection_id)

Get specification of the given inspection.

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
    # Get specification of the given inspection.
    api_response = api_instance.get_inspection_specification(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspection_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_id** | **str**| Id of inspection run. | 

### Return type

[**InspectionSpecificationResponse**](InspectionSpecificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inspection_status**
> InspectionStatusResponse get_inspection_status(inspection_id)

Get status of an inspection.

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
    # Get status of an inspection.
    api_response = api_instance.get_inspection_status(inspection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->get_inspection_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inspection_id** | **str**| Id of inspection run. | 

### Return type

[**InspectionStatusResponse**](InspectionStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_inspection**
> InspectionResponse post_inspection(body)

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
body = NULL # dict(str, object) | Base image to be used for runtime environment.

try:
    # Inspect the given application stack.
    api_response = api_instance.post_inspection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionApi->post_inspection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| Base image to be used for runtime environment. | 

### Return type

[**InspectionResponse**](InspectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

