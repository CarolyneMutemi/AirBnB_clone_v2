#!/usr/bin/python3
"""
Has the do_pack function.
"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Return:
        archive path or None if an error occurs.
    """
    local("mkdir -p versions")
    now = datetime.now()
    file1 = f"versions/web_static_{now.year}{now.month}"
    file2 = f"{now.month:2d}{now.hour:2d}{now.minute:2d}{now.second:2d}.tgz"
    file_name = file1 + file2
    file = local(f"tar -czvf {file_name} web_static")
    if file.failed:
        return None
    file_size = os.path.getsize(f'{file_name}')
    print(f'web_static packed: {file_name} -> {file_size}Bytes')
