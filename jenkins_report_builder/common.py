"""Copyright 2016 Anna Eilering."""

import os


JRB_ROOT_DIR = os.path.expanduser('~/.jrb')
JRB_LOG_DIR = os.path.join(JRB_ROOT_DIR, 'logs')
JRB_CONFIG_DIR = os.path.join(JRB_ROOT_DIR, 'configs')
JRB_ENGINE_CONFIG_NAME = 'jrb_engine.config'
JRB_ENGINE_PATH = os.path.join(JRB_ROOT_DIR, JRB_ENGINE_CONFIG_NAME)
