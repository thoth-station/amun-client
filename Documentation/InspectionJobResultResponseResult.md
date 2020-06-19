# InspectionJobResultResponseResult

Inspection job result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exit_code** | **int** | Exit code of user provided script (matches exit code of the inspect job) | 
**hwinfo** | **dict(str, object)** | Hardware information as provided by Amun&#39;s hwinfo. | 
**os_release** | **dict(str, object)** | Information about operating system as gathered from /etc/os-release | 
**runtime_environment** | **dict(str, object)** | Runtime environment information. | 
**script_sha256** | **str** | SHA 256 digest of user provided script | 
**stderr** | **str** | Standard error output produced by user provided script. | 
**stdout** | **dict(str, object)** | Standard output prodiced by user provided script. | 
**usage** | **dict(str, object)** | Utilization of resources such as user-space or kernel-space CPU time, context switches, shared memory size or page faults (and others).  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


