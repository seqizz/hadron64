metadata = """
summary @ Session manager of the LXDE Desktop (light version)
homepage @ http://lxde.org/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/sourceforge/lxde/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-apps/dbus x11-libs/gtk+
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)