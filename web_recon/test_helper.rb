require 'capybara'
require 'capybara/dsl'
require 'selenium-webdriver'

# Configure Capybara
Capybara.default_driver = :selenium

Capybara.default_max_wait_time = 60

Capybara.javascript_driver = :headless_chrome

Capybara.run_server = false

capabilities = Selenium::WebDriver::Remote::Capabilities.chrome(
  'chromeOptions' => {
    'args' => ['--no-default-browser-check', '--start-maximized']
  }
)
Capybara.register_driver :selenium do |driver|
  Capybara::Selenium::Driver.new(
    driver,
    browser: :chrome,
    url: "http://#{ENV['SELENIUM_HOST']}:#{ENV['SELENIUM_PORT']}/wd/hub",
    desired_capabilities: capabilities
  )
end
