require_relative './test_helper.rb'
require 'logger'

logger = Logger.new(STDOUT)
logger.level = ENV['LOGLEVEL'] || Logger::DEBUG

# stuff as seen
class WTFE
  include Capybara::DSL
  def initialize(domain = ENV['HOST'], queue_url = ENV['QUEUE_URL'])
    logger.debug("domain: #{domain}, queue_url: #{queue_url}")
    visit domain
    File.open("out.txt", 'w') { |f| f.write("write your stuff here #{Time.now}") }

    sleep 20
  end
end

WTFE.new(ARGV.first)
