import multiprocessing

command = '/rajabu/env/bin/gunicorn'
pythonpath = '/rajabu/tracking-backend'
bind = '0.0.0.0:8000'
workers = 3
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'tornado'
worker_connections = 1000
timeout = 30
keepalive = 2
