#!/usr/bin/python3
from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['34.229.69.44']
def host_type():
    run('uname -s')

def uptime():
    run('uptime')
