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

    comm_1 = put(archive_path, "/tmp/")
    new_dir = archive_path.strip('.tgzversions/')
    new = f'/data/web_static/releases/{new_dir}'
    comm_2 = run(f"mkdir -p {new}")
    comm_3 = run(f"tar -xzf /tmp/{new_dir}.tgz -C {new} --strip-components=1")
    comm_4 = run(f"rm /tmp/{new_dir}.tgz")
    comm_5 = run("rm -rf /data/web_static/current")
    comm_6 = run(f"ln -s {new} /data/web_static/current")

    if comm_1.failed or comm_2.failed or comm_3.failed or \
            comm_4.failed or comm_5.failed or comm_6.failed:
        return False
    print('New version deployed!')
    return True
