#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""
from fabric.api import local, run, lcd, cd, env
env.hosts = ['34.229.69.44', '100.26.9.101']


def do_clean(number=0):
    """
    That deletes out-of-date archives
    """
    num = 1
    if int(number) > 1:
        num += int(number)
    else:
        num = 2

    try:
        with lcd("versions"):
            local(f"ls -rt | tail -n +{num} | xargs rm")

        with cd("/data/web_static/releases/"):
            run(f"ls -rt web* | tail -n +{num} | xargs rm -rf")
    except Exception:
        return False
