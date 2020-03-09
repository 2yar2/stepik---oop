import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Chooce lang")

@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_langeages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()

