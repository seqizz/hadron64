metadata = """
summary @ Panel for the Xfce desktop environment
homepage @ http://www.xfce.org
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/$name/4.8/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/exo xfce-base/garcon xfce-base/libxfce4ui x11-libs/libSM x11-libs/libwnck
          x11-themes/hicolor-icon-theme
build @ dev-util/intltool
"""

def configure():
    conf("--disable-static",
            "--enable-gio-unix",
            "--disable-gtk-doc",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
