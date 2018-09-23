require 'capybara'
require 'capybara/dsl'
require 'selenium-webdriver'
# require "selenium/webdriver"
# require 'chrome-headless'

# Configure Capybara, the Chrome driver capabilities, etc before the bot
Capybara.default_max_wait_time = 5
Capybara.run_server = false
args = ['--no-default-browser-check', '--start-maximized']
caps = Selenium::WebDriver::Remote::Capabilities.chrome('chromeOptions' => { 'args' => args })
Capybara.default_driver = :selenium
Capybara.javascript_driver = :headless_chrome
Capybara.register_driver :selenium do |driver|
  Capybara::Selenium::Driver.new(
      driver,
      browser: :chrome,
      url: "http://#{ENV['SELENIUM_HOST']}:#{ENV['SELENIUM_PORT']}/wd/hub",
      desired_capabilities: caps
  )
end
