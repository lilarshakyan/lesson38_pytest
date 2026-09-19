import sys
import os
import pytest
from Lib import Helper
from Pages.practice_page import PracticePage
from Pages.sign_in import LoginPage


@pytest.fixture
def helper_obj():
    my_obj = Helper()
    my_obj.navigate_to_page()
    yield my_obj
    my_obj.close_browser()


@pytest.fixture
def practice_page(helper_obj):
    return PracticePage(helper_obj.browser, helper_obj.wait)


@pytest.fixture
def login_page(helper_obj):
    return LoginPage(helper_obj.browser, helper_obj.wait)