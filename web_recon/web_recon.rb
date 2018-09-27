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
    puts "WebRecon working on #{job.to_hash}"
    visit job.domain

    job.instructions.map do |instruction|
      puts "WebRecon processing #{instruction}"
      hint = instruction['hint']
      carry = if hint.include?('(')
        page.public_send(*hint.split('(').map { |i| i.delete(')') })
      else
        if hint.eql?('body')
          page
        else
          page.find(hint)
        end
      end

      # expected methods:
      #
      #   :scrape_to_bag
      puts "WebRecon running: #{instruction['action']} with: #{carry}"
      public_send(instruction['action'], carry)
    end.join('\n')
  end

  def scrape_to_bag(target)
    target.text
  end
end
