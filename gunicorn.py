#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set fileencoding=utf-8:

import multiprocessing

# Server Socket
bind = 'unix:/tmp/gunicorn_my_app.sock'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 30
keepalive = 2
debug = False
spew = False

# Logging
logfile = '/var/www/apps/sampleapp/app.log'
loglevel = 'info'
logconfig = None

# Process Name
proc_name = 'gunicorn_my_app'
