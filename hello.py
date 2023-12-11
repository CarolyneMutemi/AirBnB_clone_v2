#!/usr/bin/env python3
from fabric.api import *
def hello(who="world"):
    print("Hello {who}!".format(who=who))
