#!/usr/bin/python3
"""
Has the do_pack function.
"""

import os
from datetime import datetime
from fabric.api import local, hide


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Return:
        archive path or None if an error occurs.
    """
    with hide('commands'):
        local("mkdir -p versions")
    now = datetime.now()
    file1 = f"versions/web_static_{now.year}{now.month:02d}"
    file2 = f"{now.day:02d}{now.hour:02d}{now.minute:02d}{now.second:02d}.tgz"
    file_name = file1 + file2
    print(f"Packing web_static to {file_name}")
    try:
        local(f"tar -czvf {file_name} web_static")
        file_size = os.path.getsize(f'{file_name}')
        print(f'web_static packed: {file_name} -> {file_size}Bytes')
        return file_name
    except Exception:
        return None
