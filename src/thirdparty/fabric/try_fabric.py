#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabricを試してみる
fabコマンドではなくpythonスクリプトとしてインタプリタ〜指定で実行する


expect -c"
set timeout 5000
spawn python try_fabric.py
expect \"No hosts found. Please specify (single) host string for connection:\"
send \"192.168.11.16\r\"
expect \"TryFabricEnd\"
"
"""
from fabric.api import hosts, env, local, run, settings, task
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

env.hosts = [os.environ.get("FABLIC_HOST")]
env.port = 22
env.user = os.environ.get("FABLIC_USER")
env.password = os.environ.get("FABLIC_PASSWORD")
env.key_filename = os.environ.get("FABLIC_KEY_FILE")

@task
def get_date():
    with settings(warn_only=True):
        env.host = 'ip16.localdomain'
    remote_date = run('date')
    local_date = local('date', capture=True)
    print(remote_date)
    print(local_date)

if __name__ == '__main__':
    get_date()
    print("TryFabricEnd")
