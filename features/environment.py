import os
import yaml

import xiandb as db


with open(os.path.expanduser('~') + '/xian/config.yml', 'r') as config_file:
    cfg = yaml.load(config_file)


def before_all(context):
    context.root = cfg['app']['root']
    context.db = db


def before_scenario(context, scenario):
    context.s = {}
