from database import connection
import yaml


with open("config.yml", 'r') as config_file:
    cfg = yaml.load(config_file)


def before_all(context):
    context.root = cfg['app']['root']
    context.c = connection


def before_scenario(context, scenario):
    context.s = {}
