import pytest
from selenium import webdriver
import pytest_html
import pytest_metadata
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


# generate report
# it is a hook for adding env info to the HTML report

def pytest_configure(config):
    config.stash[metadata_key]['Project_Name'] = 'testing Report'
    config.stash[metadata_key]['Project_description'] = 'Python selenium for E-commere site testing'
    config.stash[metadata_key]['Module_Name'] = 'Login'
    config.stash[metadata_key]['tester'] = 'Asit'


# to skip any data from the report, this is the hook to use.
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop('Plugins', None)
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Packages', None)


