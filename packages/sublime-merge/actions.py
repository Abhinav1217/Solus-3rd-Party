#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil

def setup():
    shelltools.system("tar xf sublime_merge_build_%s_x64.tar.xz" % (get.srcVERSION()))

def install():
    pisitools.insinto("/opt/sublime_merge", "sublime_merge/*")
    pisitools.dosym("/opt/sublime_merge/sublime_merge", "/usr/bin/sublime_merge")
