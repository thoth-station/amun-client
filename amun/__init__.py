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

"""A CLI tool and library for interacting with Amun."""

__name__ = 'amun'
__version__ = "0.2.7"
__author__ = 'Fridolin Pokorny <fridolin.pokorny@gmail.com>'

from .lib import inspect
from .lib import instantiate_inspection_api
from .lib import get_inspection_build_log
from .lib import get_inspection_job_log
from .lib import get_inspection_specification
from .lib import get_inspection_status
from .lib import is_inspection_finished
from .lib import has_inspection_job
