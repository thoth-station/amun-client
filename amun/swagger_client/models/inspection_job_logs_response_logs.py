# coding: utf-8

"""
    Amun API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.6.0-dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.configuration import Configuration


class InspectionJobLogsResponseLogs(object):
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
        'exit_code': 'int',
        'hwinfo': 'dict(str, object)',
        'script_sha256': 'str',
        'stderr': 'str',
        'stdout': 'dict(str, object)',
        'usage': 'dict(str, object)',
        'os_release': 'dict(str, object)',
        'runtime_environment': 'dict(str, object)'
    }

    attribute_map = {
        'exit_code': 'exit_code',
        'hwinfo': 'hwinfo',
        'script_sha256': 'script_sha256',
        'stderr': 'stderr',
        'stdout': 'stdout',
        'usage': 'usage',
        'os_release': 'os_release',
        'runtime_environment': 'runtime_environment'
    }

    def __init__(self, exit_code=None, hwinfo=None, script_sha256=None, stderr=None, stdout=None, usage=None, os_release=None, runtime_environment=None, local_vars_configuration=None):  # noqa: E501
        """InspectionJobLogsResponseLogs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exit_code = None
        self._hwinfo = None
        self._script_sha256 = None
        self._stderr = None
        self._stdout = None
        self._usage = None
        self._os_release = None
        self._runtime_environment = None
        self.discriminator = None

        self.exit_code = exit_code
        self.hwinfo = hwinfo
        self.script_sha256 = script_sha256
        self.stderr = stderr
        self.stdout = stdout
        self.usage = usage
        self.os_release = os_release
        self.runtime_environment = runtime_environment

    @property
    def exit_code(self):
        """Gets the exit_code of this InspectionJobLogsResponseLogs.  # noqa: E501

        Exit code of user provided script (matches exit code of the inspect job)  # noqa: E501

        :return: The exit_code of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this InspectionJobLogsResponseLogs.

        Exit code of user provided script (matches exit code of the inspect job)  # noqa: E501

        :param exit_code: The exit_code of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and exit_code is None:  # noqa: E501
            raise ValueError("Invalid value for `exit_code`, must not be `None`")  # noqa: E501

        self._exit_code = exit_code

    @property
    def hwinfo(self):
        """Gets the hwinfo of this InspectionJobLogsResponseLogs.  # noqa: E501

        Hardware information as provided by Amun's hwinfo.  # noqa: E501

        :return: The hwinfo of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._hwinfo

    @hwinfo.setter
    def hwinfo(self, hwinfo):
        """Sets the hwinfo of this InspectionJobLogsResponseLogs.

        Hardware information as provided by Amun's hwinfo.  # noqa: E501

        :param hwinfo: The hwinfo of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and hwinfo is None:  # noqa: E501
            raise ValueError("Invalid value for `hwinfo`, must not be `None`")  # noqa: E501

        self._hwinfo = hwinfo

    @property
    def script_sha256(self):
        """Gets the script_sha256 of this InspectionJobLogsResponseLogs.  # noqa: E501

        SHA 256 digest of user provided script  # noqa: E501

        :return: The script_sha256 of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._script_sha256

    @script_sha256.setter
    def script_sha256(self, script_sha256):
        """Sets the script_sha256 of this InspectionJobLogsResponseLogs.

        SHA 256 digest of user provided script  # noqa: E501

        :param script_sha256: The script_sha256 of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and script_sha256 is None:  # noqa: E501
            raise ValueError("Invalid value for `script_sha256`, must not be `None`")  # noqa: E501

        self._script_sha256 = script_sha256

    @property
    def stderr(self):
        """Gets the stderr of this InspectionJobLogsResponseLogs.  # noqa: E501

        Standard error output produced by user provided script.  # noqa: E501

        :return: The stderr of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        """Sets the stderr of this InspectionJobLogsResponseLogs.

        Standard error output produced by user provided script.  # noqa: E501

        :param stderr: The stderr of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and stderr is None:  # noqa: E501
            raise ValueError("Invalid value for `stderr`, must not be `None`")  # noqa: E501

        self._stderr = stderr

    @property
    def stdout(self):
        """Gets the stdout of this InspectionJobLogsResponseLogs.  # noqa: E501

        Standard output prodiced by user provided script.  # noqa: E501

        :return: The stdout of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this InspectionJobLogsResponseLogs.

        Standard output prodiced by user provided script.  # noqa: E501

        :param stdout: The stdout of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and stdout is None:  # noqa: E501
            raise ValueError("Invalid value for `stdout`, must not be `None`")  # noqa: E501

        self._stdout = stdout

    @property
    def usage(self):
        """Gets the usage of this InspectionJobLogsResponseLogs.  # noqa: E501

        Utilization of resources such as user-space or kernel-space CPU time, context switches, shared memory size or page faults (and others).   # noqa: E501

        :return: The usage of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this InspectionJobLogsResponseLogs.

        Utilization of resources such as user-space or kernel-space CPU time, context switches, shared memory size or page faults (and others).   # noqa: E501

        :param usage: The usage of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and usage is None:  # noqa: E501
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

    @property
    def os_release(self):
        """Gets the os_release of this InspectionJobLogsResponseLogs.  # noqa: E501

        Information about operating system as gathered from /etc/os-release  # noqa: E501

        :return: The os_release of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._os_release

    @os_release.setter
    def os_release(self, os_release):
        """Sets the os_release of this InspectionJobLogsResponseLogs.

        Information about operating system as gathered from /etc/os-release  # noqa: E501

        :param os_release: The os_release of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: dict(str, object)
        """

        self._os_release = os_release

    @property
    def runtime_environment(self):
        """Gets the runtime_environment of this InspectionJobLogsResponseLogs.  # noqa: E501

        Runtime environment information.  # noqa: E501

        :return: The runtime_environment of this InspectionJobLogsResponseLogs.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._runtime_environment

    @runtime_environment.setter
    def runtime_environment(self, runtime_environment):
        """Sets the runtime_environment of this InspectionJobLogsResponseLogs.

        Runtime environment information.  # noqa: E501

        :param runtime_environment: The runtime_environment of this InspectionJobLogsResponseLogs.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and runtime_environment is None:  # noqa: E501
            raise ValueError("Invalid value for `runtime_environment`, must not be `None`")  # noqa: E501

        self._runtime_environment = runtime_environment

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
        if not isinstance(other, InspectionJobLogsResponseLogs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InspectionJobLogsResponseLogs):
            return True

        return self.to_dict() != other.to_dict()