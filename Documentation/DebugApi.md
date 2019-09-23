# amun.swagger_client.DebugApi

All URIs are relative to */api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_generate_dockerfile**](DebugApi.md#post_generate_dockerfile) | **POST** /_debug/generate-dockerfile | Generate Dockerfile as it would be generated internally for inspections. 

# **post_generate_dockerfile**
> InspectionGenerateDockerfileResponse post_generate_dockerfile(body)

Generate Dockerfile as it would be generated internally for inspections. 

### Example
```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amun.swagger_client.DebugApi()
body = NULL # dict(str, object) | Specification of the software stack that should be created and verified.

try:
    # Generate Dockerfile as it would be generated internally for inspections. 
    api_response = api_instance.post_generate_dockerfile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->post_generate_dockerfile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| Specification of the software stack that should be created and verified. | 

### Return type

[**InspectionGenerateDockerfileResponse**](InspectionGenerateDockerfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

