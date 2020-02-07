# InspectionWorkflowParameters

Inspection Workflow parameters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dockerfile** | **str** | Dockerfile. | 
**inspection_id** | **str** | ID of the inspection. | 
**specification** | **str** | Inspection specification. | 
**batch_size** | **str** | Size of the batch. | [optional] [default to '1']
**batch_name** | **str** | Name of the batch. | [optional] 
**allowed_failures** | **str** | Number of allowed failures. | [optional] [default to '1']
**parallelism** | **str** | Number of inspection that can run in parallel. | [optional] [default to '1']
**cpu** | **str** | CPU cores requested for the build. | [optional] 
**cpu_family** | **int** | Family number of CPU. | [optional] 
**cpu_model** | **int** | Modelnumber of CPU. | [optional] 
**memory** | **str** | Memory requested for build. | [optional] 
**physical_cpus** | **int** | Number of physical CPUs. | [optional] 
**processor** | **str** | Name of processor. | [optional] 
**registry** | **str** | Registry server from where Image is to be pulled. | [optional] [default to 'docker-registry.default.svc:5000']
**thoth_infra_namespace** | **str** | Project where ImageStream is present. | [optional] 
**target** | **str** |  | [optional] [default to 'inspection-result']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


