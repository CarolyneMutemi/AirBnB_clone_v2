#!/usr/bin/python3
"""
Fabric script based on the 1-pack_web_static.py
that distributes an rchive to the web servers.
"""

import os
from fabric.api import put, env, run

env.hosts = ['34.229.69.44', '100.26.9.101']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        new_dir = archive_path.strip('.tgzversions/')
        new = f'/data/web_static/releases/{new_dir}'
        run(f"mkdir -p {new}")
        run(f"tar -xzf /tmp/{new_dir}.tgz -C {new} --strip-components=1")
        run(f"rm /tmp/{new_dir}.tgz")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {new} /data/web_static/current")
        print('New version deployed!')
        return True
    except Exception:
        return False
