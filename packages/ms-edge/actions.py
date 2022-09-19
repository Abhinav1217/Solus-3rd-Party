#!/usr/bin/python

# Created For Solus Operating System
# Based on https://github.com/getsolus/3rd-party/blob/master/network/web/browser/google-chrome-stable/actions.py

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf microsoft-edge-stable_%s%s_amd64.deb" % (get.srcVERSION(), Suffix))
    shelltools.system("tar xvf data.tar.xz")

def install():
    # root owns sandbox as it is setuid
    shelltools.system("chown root:root opt/microsoft/msedge/msedge-sandbox")
    # ensure setuid
    shelltools.system("chmod 4755 opt/microsoft/msedge/msedge-sandbox")

    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")

    for i in ["16", "24", "32", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "opt/microsoft/msedge/product_logo_%s.png" % i, "microsoft-edge.png")
