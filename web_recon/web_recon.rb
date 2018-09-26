require_relative './test_helper.rb'

# Class that is able to web scrape by taking commands via
# queue message.
class WebRecon
  include Capybara::DSL

  # Run instructions gathered in the job to complete a scrape
  # A sample job might look like this:
  #
  #   > job.to_hash
  #   {
  #     instructions: [
  #       # should scrape the home page's body
  #       { action: 'scrape_to_bag', hint: 'body' },
  #       # navigate to about us and scrape
  #       { action: 'scrape_to_bag', hint: 'click_link("about us")' },
  #       # navigate to the FAQ page and scrape
  #       { action: 'scrape_to_bag', hint: 'click_link("faq")' }
  #     ],
  #     ...
  #   }
  def process(job)
    visit job.domain

    job.instructions.map do |instruction|
      puts "WebRecon processing #{instruction}"
      carry = if instruction[:hint].include?('(')
                page.public_send(*instruction[:hint].split('(').map { |i| i.delete(')') })
              else
                instruction[:hint]
              end

      # expected methods:
      #
      #   :scrape_to_bag
      puts "WebRecon running: #{instruction[:action]} with: #{carry}"
      public_send(instruction[:action], carry)
    end.join('\n')
  end

  def scrape_to_bag(raw_data)
    data = raw_data.text
    data.gsub(/\s{2,}/, ' ')
  end
end
