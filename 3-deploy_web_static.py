#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive
to the web servers
"""

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
