# amun.swagger_client.ServiceApi

All URIs are relative to *http://amun-api-thoth-test-core.apps.ocp.prod.psi.redhat.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](ServiceApi.md#get_version) | **GET** /version | Get Amun API version.


# **get_version**
> VersionResponse get_version()

Get Amun API version.

### Example

```python
from __future__ import print_function
import time
import amun.swagger_client
from amun.swagger_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = amun.swagger_client.ServiceApi()

try:
    # Get Amun API version.
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with service version identifier. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

