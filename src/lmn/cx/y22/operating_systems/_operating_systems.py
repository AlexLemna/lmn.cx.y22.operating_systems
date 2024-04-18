# SPDX-FileCopyrightText: 2024 Alex Lemna
#
# SPDX-License-Identifier: 0BSD OR MIT OR Apache-2.0


import importlib.metadata
from dataclasses import dataclass
from enum import EnumType
from typing import Any, Final

__all__ = ["OperatingSystem", "OS"]
try:
    __version__ = importlib.metadata.version("lmn.cx.y22.operating_systems")
except importlib.metadata.PackageNotFoundError:
    __version__ = "UNKNOWN"


class OperatingSystemMeta(type):
    def __call__(self, *args: Any, **kwds: Any) -> Any:

        if (
            "xdg" not in kwds.keys()
            and "unix_like" in kwds.keys()
            and kwds["unix_like"] is True
        ):
            kwds["xdg"] = True

        return super().__call__(*args, **kwds)


@dataclass(frozen=True)
class OperatingSystem(metaclass=OperatingSystemMeta):
    name: str
    unix_like: bool = False
    xdg: bool = False


class OS(EnumType, OperatingSystem):
    ANDROID: Final = OperatingSystem("Android")
    FREEBSD: Final = OperatingSystem("FreeBSD", unix_like=True)
    iOS: Final = OperatingSystem("iOS")
    LINUX: Final = OperatingSystem("Linux", unix_like=True)
    MAC: Final = OperatingSystem("macOS", unix_like=True, xdg=False)
    NETBSD: Final = OperatingSystem("NetBSD", unix_like=True)
    OPENBSD: Final = OperatingSystem("OpenBSD", unix_like=True)
    UNKNOWN: Final = OperatingSystem("UNKNOWN")
    WINDOWS: Final = OperatingSystem("Windows")
