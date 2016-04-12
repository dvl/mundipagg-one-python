# -*- coding: utf-8 -*-

from enum import Enum


class HttpContentTypeEnum(Enum):
    xml = 1,
    json = 2


class ManageOperationEnum(Enum):
    Capture = 1,
    Cancel = 2


class PlatformEnvironment(Enum):
    sandbox = 1,
    production = 2

