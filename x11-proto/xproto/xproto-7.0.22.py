metadata = """
summary @ X11 core wire protocol and auxiliary headers
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.gz
arch @ ~x86
options @ doc
"""

depends = """
runtime @ x11-misc/util-macros
"""

opt_runtime = """
doc @ app-text/xmlto
"""

def configure():
    conf(
    config_enable("doc", "xmlto"),
    config_enable("doc", "specs"),
    "--without-fop")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")