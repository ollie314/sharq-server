# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE.txt for details.
# A WSGI application driver to deploy Sharq Server using other
# application servers like uWSGI, etc.

import os
from sharq_server import setup_server

# read path from variable / default to current working directory
sharq_config_path = os.environ.get('SHARQ_CONFIG', './sharq.conf')
sharq_config_path = os.path.abspath(sharq_config_path)
server = setup_server(sharq_config_path)
app = server.app


if __name__ == '__main__':
    app.run()
