require_relative './test_helper.rb'
require 'logger'

logger = Logger.new(ENV['LOG_PATH'] || STDOUT)
logger.level = ENV['LOG_LEVEL'] || Logger::DEBUG

# stuff as seen
class WTFE
  include Capybara::DSL
  def initialize(domain = ENV['HOST'], queue_url = ENV['QUEUE_URL'])
    sleep 20
    logger.debug("domain: #{domain}, queue_url: #{queue_url}")
    puts "domain: #{domain}, queue_url: #{queue_url}"
    visit domain
    File.open("out.txt", 'w') do |f|
      f.write("write your stuff here #{Time.now}")
    end
  end
end

WTFE.new(*ARGV[1, -1])
