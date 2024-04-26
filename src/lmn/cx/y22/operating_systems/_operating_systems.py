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
from typing import Final

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
    """The name of the operating system."""

    unix_like: bool = False
    """Whether or not the operating system is 'Unix-like'. This comes down
    to my arbitrary decision, which generally boils down to, 'Should an
    application running on this OS assume it can access a filesystem with
    a FHS-like layout?'"""

    xdg: bool | None = None
    """Whether or not an application running on this operating system
    should follow the XDG Base Directory Specification."""

    def __post_init__(self):
        if self.xdg is None:
            object.__setattr__(self, "xdg", True if self.unix_like else False)


class OS(OperatingSystem, Enum):

    ANDROID: Final = "Android"
    """The Android operating system is a mobile operating system with
    a free, open-source core, running the Linux kernel. Almost all 
    consumer devices running Android run Google's proprietary version
    of Android, but other Android forks include Amazon's Fire OS and
    the community-based LineageOS. Applications on it should not 
    follow the XDG.

    See [the Android Open Source Project website](https://source.android.com/)."""

    FREEBSD: Final = "FreeBSD", True  # ("FreeBSD", unix_like=True)
    """FreeBSD is a free, open-source, Unix-like operating system
    known for its use of the ZFS file system and high-performance
    networking stack. It excels when used as a web server, but
    especially as a file server. It was the operating system
    behind the PlayStation 3 and PlayStation 4. 
    
    See [the FreeBSD website](https://www.freebsd.org/)."""

    iOS: Final = "iOS"
    """Apple's iOS is a mostly closed-source mobile operating
    system, based on its macOS desktop operating system. Apple's
    iPhones run iOS, and it's also the basis for Apple's tvOS, iPadOS,
    and watchOS. Applications on it should not follow the XDG.
    
    See [the iOS website](https://www.apple.com/ios/)."""

    LINUX: Final = "Linux", True  # ("Linux", unix_like=True)
    """Linux is a family of open-source, Unix-like operating systems
    based around the Linux kernel. Popular distributions include
    Ubuntu, Debian, and Fedora.
    
    See [the Linux kernel website](https://kernel.org/)."""

    MAC: Final = "macOS", True, False  # ("macOS", unix_like=True, xdg=False)
    """Apple macOS is a mostly closed-source operating system that
    runs on Apple's desktops and laptops. The core of the operating 
    system remains open-sourced as the 'Darwin' operating system.
    Applications on it should not follow the XDG.
    
    See [the macOS website](https://apple.com/macos)."""

    NETBSD: Final = "NetBSD", True  # ("NetBSD", unix_like=True)
    """NetBSD is a free, open-source, portability-focused Unix-like
    operating system that supports a large number of hardware
    platforms. 
    
    See [the NetBSD website](https://netbsd.org/)."""

    OPENBSD: Final = "OpenBSD", True  # ("OpenBSD", unix_like=True)
    """OpenBSD is a free, open-source, security-focused Unix-like
    operating system with strengths in cryptography, simplicity, and
    useful documentation. It excels when used as a firewall or router,
    or as a server for core network services like DNS and NTP.
    
    See [the OpenBSD website](https://www.openbsd.org/)."""

    UNKNOWN: Final = "UNKNOWN"
    """Any operating system not specified here."""

    WINDOWS: Final = "Windows"
    """Microsoft Windows is a closed-source operating system often
    used on desktops and laptops, and on enterprise servers. It's the
    most-used operating system in the world for laptops and desktops.
    Applications on it should not follow the XDG.
    
    See [the Windows website](https://windows.com/)."""


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
