metadata = """
summary @ A C library that implements an SQL database engine
homepage @ http://www.sqlite.org
license @ as-is
src_url @ http://www.sqlite.org/sqlite-autoconf-3070900.tar.gz
arch @ ~x86
"""
srcdir="sqlite-autoconf-3070900"

depends = """
build @ sys-libs/readline
"""

def configure():
    append_cflags("-DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_SECURE_DELETE")
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s install" % install_dir)