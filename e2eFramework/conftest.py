import os.path

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"  # registering
    )


@pytest.fixture(scope="function", autouse=True)
def browserInstance(request):  # adding a request to get hold of all CLI configurations - Default fixture
    browser_name = request.config.getoption("browser_name")  # sending browser name from command line
    if browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser: {}".format(browser_name))

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Store the driver inside the test node for accessing the same in hooks
    request.node.driver = driver
    yield driver
    driver.close()


@pytest.mark.hookwrapper  # this piece of code is required to generate html report
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Prepare screenshot file path
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')

            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is" + file_name)
            driver = getattr(item, "driver", None)
            if driver:
                try:
                    driver.get_screenshot_as_file(file_name)
                    html_content = (
                            '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    )
                    extra.append(pytest_html.extras.html(html_content))
                except Exception as e:
                    print(f"Failed to capture screenshot: {e}")
            else:
                print("Driver not available on item")

            report.extra = extra
