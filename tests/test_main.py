from lmn.cx.y22.operating_systems import OS


def test_os():
    assert OS.ANDROID.os_name == "Android"
    assert OS.ANDROID.unix_like is False
    assert OS.ANDROID.xdg is False

    assert OS.FREEBSD.os_name == "FreeBSD"
    assert OS.FREEBSD.unix_like is True
    assert OS.FREEBSD.xdg is True

    assert OS.iOS.os_name == "iOS"
    assert OS.iOS.unix_like is False
    assert OS.iOS.xdg is False

    assert OS.LINUX.os_name == "Linux"
    assert OS.LINUX.unix_like is True
    assert OS.LINUX.xdg is True

    assert OS.MAC.os_name == "macOS"
    assert OS.MAC.unix_like is True
    assert OS.MAC.xdg is False

    assert OS.NETBSD.os_name == "NetBSD"
    assert OS.NETBSD.unix_like is True
    assert OS.NETBSD.xdg is True

    assert OS.OPENBSD.os_name == "OpenBSD"
    assert OS.OPENBSD.unix_like is True
    assert OS.OPENBSD.xdg is True

    assert OS.UNKNOWN.os_name == "UNKNOWN"
    assert OS.UNKNOWN.unix_like is False
    assert OS.UNKNOWN.xdg is False

    assert OS.WINDOWS.os_name == "Windows"
    assert OS.WINDOWS.unix_like is False
    assert OS.WINDOWS.xdg is False


if __name__ == "__main__":
    test_os()
