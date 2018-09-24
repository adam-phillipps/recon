require_relative './test_helper.rb'

# stuff as seen
class WTFE
  include Capybara::DSL

  def initialize()
    domain ||= 'https://www.ski.com'
    visit(domain)
    body = page.text
    puts "body goes here: #{body}"
    # File.open('out.txt', 'w') do |f|
    #   puts "body goes here: #{body}"
    #   f.write("write your stuff from #{queue_url} goes here #{Time.now}\n#{body}")
    # end
  end
end

WTFE.new
