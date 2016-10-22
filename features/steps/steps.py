# -*- coding: utf-8 -*-
from behave import given, when, then
from nose.tools import assert_in, assert_equals
from assertions import assert_somewhere_in, assert_somewhere_equals

import types
import json
import re
import requests

from tools import get_data


@given(u'I define that {variable} is {value}')
def define_variable(context, variable, value):
    context.s[variable] = json.loads(value)


@then(u'I define that {variable} is {path} from a result')
def define_variable_from_result(context, variable, path):
    context.s[variable] = get_data(context.response, path)


@when(u'I make a {method} request to :{path}')
def make_request(context, method, path):
    path = re.sub(r'\[(\w+)\]', lambda m: str(context.s[m.group(1)]), path)
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


@then(u'I have a {result_type} result')
def validate_result_type(context, result_type):
    assert_equals(type(context.response), getattr(types, result_type))


@then(u'{variable} is in a result')
def validate_variable_in(context, variable):
    assert_in(context.response, json.loads(variable))


@then(u'{variable} is somewhere in a result')
def validate_variable_in_somewhere(context, variable):
    assert_somewhere_in(context.response, json.loads(variable))


@then(u'{variable} equals {value} somewhere in a result')
def validate_variable_value_in_somewhere(context, variable, value):
    assert_somewhere_equals(context.response, variable, json.loads(value))


@then(u'{path} equals {value} in a result')
def validate_variable_value(context, path, value):
    assert_equals(get_data(context.response, path), json.loads(value))


@then(u'{path}/* contains {value} in a result')
def validate_variable_content_multilevel(context, path, value):
    assert_somewhere_in(json.loads(value), get_data(context.response, path))


@then(u'{path} contains {value} in a result')
def validate_variable_content(context, path, value):
    assert_in(json.loads(value), get_data(context.response, path))
