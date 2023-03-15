#!/usr/bin/python

# Created For Solus Operating System
# Based on https://github.com/Abhinav1217/Solus-3rd-Party/tree/main/packages/zoom-client

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True
VERSION = get.srcVERSION() + ".jammy"
print VERSION
# Should not change.

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf darling_%s_amd64.deb" % (VERSION))
    shelltools.system("tar  --use-compress-program=unzstd -xvf data.tar.zst")

def install():
    # pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")