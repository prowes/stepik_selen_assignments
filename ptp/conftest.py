import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    sleep(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
