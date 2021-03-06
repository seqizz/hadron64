metadata = """
summary @ X.Org Autotools macros
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://www.x.org/releases/individual/util/$fullname.tar.bz2
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makedirs("/usr/lib")

    move("%s/usr/share/pkgconfig" % install_dir, "/usr/lib")
