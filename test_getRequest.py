import pytest
import requests
import json


def test_101_get_status_code():
    resp = requests.get("https://dummy.restapiexample.com/api/v1/employees")
    print(resp.headers)
    print(type(resp.text))
    a = resp.status_code
    assert a == 200, "Request was not successful and the status code was {}".format(a)

def test_101_get_emp_ids():
    resp = requests.get("https://dummy.restapiexample.com/api/v1/employees")
    print(resp)
    resp_json = resp.json()
    print(resp_json['status'])

#test_101_get_emp_ids()
#test_101_get_status_code()
