import pytest
from py.xml import html
from datetime import datetime

@pytest.fixture()
def hello():
    print('hello')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    # 增加描述字段
    report.desc = str(item.function.__doc__)
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra
        

def pytest_html_report_title(report):
    report.title="xxx"

def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("描述"))

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.desc))

