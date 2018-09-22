# require File.expand_path('../../config/environment', __FILE__)

# Capybara config with docker-compose environment vars
# require 'minitest/rails/capybara'
require 'capybara'
require 'capybara/dsl'
require 'selenium-webdriver'

Capybara.app_host = "http://#{ENV['TEST_APP_HOST']}:#{ENV['TEST_PORT']}"
Capybara.default_driver = :selenium_chrome_headless
Capybara.default_max_wait_time = 5
# Capybara.javascript_driver = :selenium
Capybara.run_server = false
# Configure the Chrome driver capabilities & register
# args = ['--no-default-browser-check', '--start-maximized']
# caps = Selenium::WebDriver::Remote::Capabilities.chrome('chromeOptions' => { 'args' => args })
# Capybara.register_driver :selenium_chrome_headless do |app|
#   Capybara::Selenium::Driver.new(
#       app,
#       browser: :selenium_chrome_headless,
#       url: "http://#{ENV['SELENIUM_HOST']}:#{ENV['SELENIUM_PORT']}/wd/hub",
#       desired_capabilities: caps
#   )
# end
