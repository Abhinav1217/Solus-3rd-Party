#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"],
IgnoreAutodep = True

# Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf zoom_amd64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
