from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webrecon import helpers, reporting


@reporting.self_report
def get_driver(app):
    """
    Create or get a webdriver or driver, like the Selenium.webdriver.  This
    method is usually used to get the driver resource to navigate to a HTML page
    or a document with HTTP requests.

    Params:
    -------
    app : str
        Name of the app/application that will be using this driver.  This is
        usually used during HTML DOM rendering, navigating, crawling and
        scraping.

    Returns:
    --------
    driver : selenium.webdriver.Firefox
    """
    # from selenium.webdriver.common.keys import Keys
    # capabilities = DesiredCapabilities.FIREFOX.copy()
    # capabilities["marionette"] = False

    return webdriver.Firefox()


@reporting.self_report
def get_page(url, driver=None):
    """
    Get a HTML browser page or document with HTTP request to given URL using
    a webdriver, like Selenium.  You can use this method to navigate, crawl,
    or achieve an objective if your objective is a HTML page.

    Params:
    -------
    url : str
        HTTP URL string.  This is the location of the page you are navigating to.
        stuff stuff stuff and things test test.
    pagename : str
        This is the name of a page that you're going to use to say some stuff

    Keyword Arguments:
    ------------------
    driver : capybara.selenium.driver
        The driver is an object that can navigate using web browsers.  This
        object can usually only be used in an environment that is running
        Selenium.

    Returns:
    --------
    page : capybara.Page
    """
    driver = get_driver("SnardBardery") # figure out a good app name
    return driver.get(url)
