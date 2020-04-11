#!/usr/bin/python3
"""Module that packs files to be passed to a server using tar"""

from fabric.api import *
from os.path import exists, isdir
from datetime import datetime


def do_pack():
    """Packs all files in the web_static directory using tar"""
    print("Packing web_static to versions/web_static_20170314233357.tgz")
    if not exists('versions') or (exists('versions') and not isdir('versions')):
        local('mkdir -p versions')
    date = datetime.now()
    command = 'tar -cvzf versions/web_static_'
    command += '{:4}{:02}{:02}'.format(date.year, date.month, date.day)
    command += '{:02}{:02}{:02}'.format(date.hour, date.minute, date.second)
    command += '.tgz web_static'
    try:
        local(command)
    except:
        return None
