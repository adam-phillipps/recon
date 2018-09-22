require_relative './test_helper.rb'

# stuff as seen
class WTFE
  include Capybara::DSL
  def initialize(url)
    puts "\n\n#{url}"
    visit url
    File.open("out.txt", 'w') { |f| f.write("write your stuff here #{Time.now}") }

    sleep 20
  end
end

WTFE.new(ARGV.first)
