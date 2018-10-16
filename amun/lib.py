#!/usr/bin/env python3
# amun
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A simple wrapper around models to simplify inspection submission."""


import typing

from .swagger_client import InspectionApi
from .swagger_client import InspectionSpecification
from .swagger_client import Configuration
from .swagger_client import ApiClient


def inspect(host: str, base: str, *,
            files: typing.List[dict] = None, packages: typing.List[str] = None, python: dict = None,
            script: str = None):
    """Submit an analysis to the inspection endpoint."""
    # Adjust remote to communicate with:
    configuration = Configuration()
    configuration.host = host
    api_client = ApiClient(configuration)

    # Use the customized API client to talk to the remote API with the adjusted host.
    api_instance = InspectionApi(api_client)
    specification = InspectionSpecification(
        base=base,
        packages=packages,
        python=python,
        files=files,
        script=script
    )

    api_response = api_instance.post_inspection(specification)
    return api_response.to_dict()
