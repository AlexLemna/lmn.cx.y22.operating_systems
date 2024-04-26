# SPDX-FileCopyrightText: 2024 Alex Lemna
# SPDX-License-Identifier: 0BSD OR MIT OR Apache-2.0
#
# This source code is available to you under your choice of any
# of the following licenses:
#   - The BSD Zero Clause License (or `0BSD`)
#   - The MIT License (or `MIT`)
#   - The Apache License 2.0 (or `Apache-2.0`)
# For more information, see the COPYING file or the LICENSES
# directory at the root of this repository.
#

import importlib.metadata
from dataclasses import dataclass
from enum import Enum
from typing import Any, Final

__all__ = ["determine_os", "OperatingSystem", "OS"]
try:
    __version__ = importlib.metadata.version("lmn.cx.y22.operating_systems")
except importlib.metadata.PackageNotFoundError:
    __version__ = "UNKNOWN"


@dataclass(frozen=True)
class OperatingSystem:
    """A dataclass representing an operating system. Its properties:
    - os_name (str): The name of the operating system.
    - unix_like (bool): Whether or not the operating system is 'Unix-like',
    in my arbitrary opinion.
    - xdg (bool): Whether or not an application running on this operating
    system should follow the XDG Base Directory Specification."""

    os_name: str
    unix_like: bool = False
    xdg: bool | None = None

    def __post_init__(self):
        if self.xdg is None:
            object.__setattr__(self, "xdg", True if self.unix_like else False)


class OS(OperatingSystem, Enum):
    ANDROID: Final = "Android"
    FREEBSD: Final = "FreeBSD", True  # ("FreeBSD", unix_like=True)
    iOS: Final = "iOS"
    LINUX: Final = "Linux", True  # ("Linux", unix_like=True)
    MAC: Final = "macOS", True, False  # ("macOS", unix_like=True, xdg=False)
    NETBSD: Final = "NetBSD", True  # ("NetBSD", unix_like=True)
    OPENBSD: Final = "OpenBSD", True  # ("OpenBSD", unix_like=True)
    UNKNOWN: Final = "UNKNOWN"
    WINDOWS: Final = "Windows"


def determine_os() -> OS:
    """Determines the operating system this script is running on.
    Returns a value in the `OS` enum.

    In order to return `OS.iOS`, requires Python 3.13 or higher."""
    # fmt: off
    try:
        from sys import getandroidapilevel  # type: ignore
        return OS.ANDROID
    except ImportError:
        import sys
    # fmt: on

    if sys.platform.startswith("freebsd"):
        return OS.FREEBSD

    # requires Python 3.13
    #   see: https://peps.python.org/pep-0730/#platform-identification
    if sys.platform == "ios":
        return OS.iOS

    if sys.platform == "linux":
        return OS.LINUX

    if sys.platform == "darwin":
        return OS.MAC

    if sys.platform.startswith("netbsd"):
        return OS.NETBSD

    if sys.platform.startswith("openbsd"):
        return OS.OPENBSD

    if sys.platform == "win32":
        return OS.WINDOWS

    return OS.UNKNOWN
