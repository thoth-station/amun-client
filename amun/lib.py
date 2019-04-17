#!/usr/bin/env python3
# amun
# Copyright(C) 2018, 2019 Fridolin Pokorny
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


def instantiate_inspection_api(amun_api_url: str) -> InspectionApi:
    """Instantiate InspectionApi for communicating with Amun API."""
    # Adjust remote to communicate with:
    configuration = Configuration()
    configuration.host = amun_api_url
    api_client = ApiClient(configuration)

    # Use the customized API client to talk to the remote API with the adjusted host.
    return InspectionApi(api_client)


def get_inspection_status(amun_api_url: str, inspection_id: str) -> dict:
    """Get status dictionary of the given inspection."""
    api_instance = instantiate_inspection_api(amun_api_url)
    api_response = api_instance.get_inspection_status(inspection_id)
    api_response = api_response.to_dict()
    api_response.pop('parameters', None)
    return api_response


def is_inspection_finished(amun_api_url: str, inspection_id: str) -> bool:
    """Check if the given inspection is finished."""
    status = get_inspection_status(amun_api_url, inspection_id)
    build_finished = status['build']['state'] == 'terminated'
    # Inspection is finished if the given job is finished or was not requested to run.
    job_finished = status['job'] is None or status['job']['state'] == 'terminated'
    return build_finished and job_finished


def has_inspection_job(amun_api_url: str, inspection_id: str) -> bool:
    """Check if the given inspection has assigned job."""
    status = get_inspection_status(amun_api_url, inspection_id)
    return status['job'] is not None


def inspect(amun_api_url: str, base: str, *,
            files: typing.List[dict] = None, packages: typing.List[str] = None, python: dict = None,
            build: dict = None, run: dict = None, script: str = None) -> dict:
    """Submit an analysis to the inspection endpoint."""
    api_instance = instantiate_inspection_api(amun_api_url)

    specification = InspectionSpecification(
        base=base,
        packages=packages,
        python=python,
        files=files,
        script=script,
        build=build,
        run=run
    )

    api_response = api_instance.post_inspection(specification)
    return api_response.to_dict()


def get_inspection_build_log(amun_api_url: str, inspection_id: str) -> str:
    """Get log of an inspection build, the inspection has to be successful."""
    api_instance = instantiate_inspection_api(amun_api_url)
    api_response = api_instance.get_inspection_build_log(inspection_id)
    return api_response.to_dict()['log']


def get_inspection_job_log(amun_api_url: str, inspection_id: str) -> dict:
    """Get log of an inspection job, the inspection has to be successful."""
    api_instance = instantiate_inspection_api(amun_api_url)
    api_response = api_instance.get_inspection_job_log(inspection_id)
    return api_response.to_dict()['log']


def get_inspection_specification(amun_api_url: str, inspection_id: str) -> typing.Tuple[dict, str]:
    """Get specification of an inspection, the inspetion has to be successful."""
    api_instance = instantiate_inspection_api(amun_api_url)
    api_response = api_instance.get_inspection_specification(inspection_id)
    api_response = api_response.to_dict()
    return api_response['specification'], api_response['created']
