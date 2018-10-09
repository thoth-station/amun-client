# coding: utf-8

"""
    Amun API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InspectionGenerateDockerfileResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dockerfile': 'str',
        'parameters': 'object'
    }

    attribute_map = {
        'dockerfile': 'dockerfile',
        'parameters': 'parameters'
    }

    def __init__(self, dockerfile=None, parameters=None):  # noqa: E501
        """InspectionGenerateDockerfileResponse - a model defined in Swagger"""  # noqa: E501

        self._dockerfile = None
        self._parameters = None
        self.discriminator = None

        self.dockerfile = dockerfile
        self.parameters = parameters

    @property
    def dockerfile(self):
        """Gets the dockerfile of this InspectionGenerateDockerfileResponse.  # noqa: E501

        Generated Dockerfile as a string.  # noqa: E501

        :return: The dockerfile of this InspectionGenerateDockerfileResponse.  # noqa: E501
        :rtype: str
        """
        return self._dockerfile

    @dockerfile.setter
    def dockerfile(self, dockerfile):
        """Sets the dockerfile of this InspectionGenerateDockerfileResponse.

        Generated Dockerfile as a string.  # noqa: E501

        :param dockerfile: The dockerfile of this InspectionGenerateDockerfileResponse.  # noqa: E501
        :type: str
        """
        if dockerfile is None:
            raise ValueError("Invalid value for `dockerfile`, must not be `None`")  # noqa: E501

        self._dockerfile = dockerfile

    @property
    def parameters(self):
        """Gets the parameters of this InspectionGenerateDockerfileResponse.  # noqa: E501

        Parameters echoed back to user (with default parameters if omitted).   # noqa: E501

        :return: The parameters of this InspectionGenerateDockerfileResponse.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InspectionGenerateDockerfileResponse.

        Parameters echoed back to user (with default parameters if omitted).   # noqa: E501

        :param parameters: The parameters of this InspectionGenerateDockerfileResponse.  # noqa: E501
        :type: object
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InspectionGenerateDockerfileResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionGenerateDockerfileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
