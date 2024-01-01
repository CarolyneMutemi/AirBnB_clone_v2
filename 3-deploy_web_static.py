#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive
to the web servers
"""
from fabric.api import env

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy
#env.hosts = ['localhost', '34.229.69.44', '100.26.9.101']


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive = do_pack()
    if not archive:
        print('what?')
        return False
    print(archive)
    return do_deploy(archive)
