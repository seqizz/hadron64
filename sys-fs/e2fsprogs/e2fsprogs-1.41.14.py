metadata = """
summary @ Ext2/3/4 filesystem utilities
homepage @ http://e2fsprogs.sourceforge.net/
license @ MIT + GPL + LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/e2fsprogs/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-apps/util-linux 
build @ sys-apps/util-linux
"""

def configure():
    raw_configure("--enable-elf-shlibs",
            "--disable-fsck", "--disable-uuidd",
            "--disable-libuuid", "--disable-libblkid")

def install():
    raw_install("install install-libs LDCONFIG=/bin/true \
            DESTDIR=%s root_sbindir=/sbin root_libdir=/lib" % install_dir)