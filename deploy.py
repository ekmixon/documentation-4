#!/usr/bin/env python3
#### THIS FILE IS OUTDATED ###

import subprocess

web_server_host = "cdn1.tn.ixsystems.com"
web_server_dir = "/zdata/docs"

rsync_target = f"{username}@{web_server_host}:{web_server_dir}"

rsync_command = ['rsync', '-avz', '--delete', 'public/', rsync_target]
hugo_command = ['hugo', '-t', 'docsy', '-d', 'public', '--gc', '--minify', '--cleanDestinationDir']


# Conditional to check if user is allowed to run command
if username.lower() in allowed_users:
    subprocess.run(hugo_command)
    subprocess.run(rsync_command)
else:
    print('You do not have permission to run this script.')
