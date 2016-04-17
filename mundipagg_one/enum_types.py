# -*- coding: utf-8 -*-

from enum import Enum


class HttpContentType(Enum):
    xml = 1
    json = 2


class ManageOperation(Enum):
    Capture = 1
    Cancel = 2


class PlatformEnvironment(Enum):
    sandbox = 1
    production = 2

