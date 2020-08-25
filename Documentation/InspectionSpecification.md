# InspectionSpecification

Specification of software stack for inspection.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Base image on which the runtime environment should be based on. | 
**identifier** | **str** | A user-created string which will be inserted into the inspection id to distinguish different inspection runs. | [optional] 
**package_manager** | **str** | Package manager to be used for installing dependencies. | [optional] [default to 'micropipenv']
**batch_size** | **int** | Number of inspection runs | [optional] [default to 1]
**packages** | **list[str]** | A list of native packages that should be installed into the runtime environment. | [optional] 
**python_packages** | **list[str]** | A list of python packages that should be installed into the runtime environment. | [optional] 
**python** | [**InspectionSpecificationPython**](InspectionSpecificationPython.md) |  | [optional] 
**build** | [**InspectionSpecificationBuild**](InspectionSpecificationBuild.md) |  | [optional] 
**run** | [**InspectionSpecificationRun**](InspectionSpecificationRun.md) |  | [optional] 
**files** | [**list[InspectionSpecificationFiles]**](InspectionSpecificationFiles.md) | Files passed to the context. | [optional] 
**environment** | [**list[InspectionSpecificationEnvironment]**](InspectionSpecificationEnvironment.md) | Environment variables supplied into the build process. | [optional] 
**script** | **str** | A script that should be executed in inspection run. | [optional] 
**update** | **bool** | Perform native packages update. | [optional] 
**upgrade_pip** | **bool** | Update pip before installing packages. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


