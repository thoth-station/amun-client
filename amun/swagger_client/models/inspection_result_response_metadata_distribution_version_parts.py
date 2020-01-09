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


class InspectionResultResponseMetadataDistributionVersionParts(object):
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
        'build_number': 'str',
        'major': 'str',
        'minor': 'str'
    }

    attribute_map = {
        'build_number': 'build_number',
        'major': 'major',
        'minor': 'minor'
    }

    def __init__(self, build_number=None, major=None, minor=None):  # noqa: E501
        """InspectionResultResponseMetadataDistributionVersionParts - a model defined in OpenAPI"""  # noqa: E501

        self._build_number = None
        self._major = None
        self._minor = None
        self.discriminator = None

        self.build_number = build_number
        self.major = major
        self.minor = minor

    @property
    def build_number(self):
        """Gets the build_number of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501


        :return: The build_number of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this InspectionResultResponseMetadataDistributionVersionParts.


        :param build_number: The build_number of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :type: str
        """
        if build_number is None:
            raise ValueError("Invalid value for `build_number`, must not be `None`")  # noqa: E501

        self._build_number = build_number

    @property
    def major(self):
        """Gets the major of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501


        :return: The major of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :rtype: str
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this InspectionResultResponseMetadataDistributionVersionParts.


        :param major: The major of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :type: str
        """
        if major is None:
            raise ValueError("Invalid value for `major`, must not be `None`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501


        :return: The minor of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this InspectionResultResponseMetadataDistributionVersionParts.


        :param minor: The minor of this InspectionResultResponseMetadataDistributionVersionParts.  # noqa: E501
        :type: str
        """
        if minor is None:
            raise ValueError("Invalid value for `minor`, must not be `None`")  # noqa: E501

        self._minor = minor

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
        if not isinstance(other, InspectionResultResponseMetadataDistributionVersionParts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
