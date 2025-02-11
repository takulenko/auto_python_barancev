# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("qwe", "asd", "zxc"))
    app.logout()

def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

