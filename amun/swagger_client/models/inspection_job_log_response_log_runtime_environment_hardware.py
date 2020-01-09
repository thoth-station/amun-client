# coding: utf-8

"""
    Amun API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InspectionJobLogResponseLogRuntimeEnvironmentHardware(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cpu_family': 'int',
        'cpu_model': 'int'
    }

    attribute_map = {
        'cpu_family': 'cpu_family',
        'cpu_model': 'cpu_model'
    }

    def __init__(self, cpu_family=None, cpu_model=None):  # noqa: E501
        """InspectionJobLogResponseLogRuntimeEnvironmentHardware - a model defined in OpenAPI"""  # noqa: E501

        self._cpu_family = None
        self._cpu_model = None
        self.discriminator = None

        if cpu_family is not None:
            self.cpu_family = cpu_family
        if cpu_model is not None:
            self.cpu_model = cpu_model

    @property
    def cpu_family(self):
        """Gets the cpu_family of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.  # noqa: E501


        :return: The cpu_family of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.  # noqa: E501
        :rtype: int
        """
        return self._cpu_family

    @cpu_family.setter
    def cpu_family(self, cpu_family):
        """Sets the cpu_family of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.


        :param cpu_family: The cpu_family of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.  # noqa: E501
        :type: int
        """

        self._cpu_family = cpu_family

    @property
    def cpu_model(self):
        """Gets the cpu_model of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.  # noqa: E501


        :return: The cpu_model of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.  # noqa: E501
        :rtype: int
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.


        :param cpu_model: The cpu_model of this InspectionJobLogResponseLogRuntimeEnvironmentHardware.  # noqa: E501
        :type: int
        """

        self._cpu_model = cpu_model

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionJobLogResponseLogRuntimeEnvironmentHardware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
