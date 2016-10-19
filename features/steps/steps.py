# -*- coding: utf-8 -*-
from behave import given, when, then
from nose.tools import assert_in, assert_equals
from assertions import assert_in_equals

import json
import re
import requests


@given(u'I define that {variable} is {value}')
def define_variable(context, variable, value):
    context.s[variable] = json.loads(value)


@when(u'I make a {method} request to :{path}')
def make_request(context, method, path):
    path = re.sub('\[(\w+)\]', lambda m: context.s[m.group(1)], path)
    request = getattr(requests, method.lower())
    context.r = request("%s/%s" % (context.root, path))


@then(u'I have a {content_type} response')
def validate_response_type(context, content_type):
    assert_in(content_type.lower(), context.r.headers['Content-Type'].lower())
    if content_type == "JSON":
        context.response = context.r.json()


@then(u'I have {count} results')
def validate_results_count(context, count):
    assert_equals(len(context.response), int(count))


@then(u'{variable} is {value} for a result')
def validate_variable_value(context, variable, value):
    assert_in_equals(context.response, variable, json.loads(value))
