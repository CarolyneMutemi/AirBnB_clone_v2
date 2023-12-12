#!/usr/bin/python3
"""
Has the do_deploy function.
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
        run(f"tar -xzf /tmp/{new_dir}.tgz -C {new}")
        run(f"mv {new}/web_static/* {new}/")
        run(f"rm -rf {new}/web_static")
        run(f"rm /tmp/{new_dir}.tgz")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {new} /data/web_static/current")
        print('New version deployed!')
        return True
    except:
        return False
