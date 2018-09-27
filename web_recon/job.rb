require 'json'

# translate a queue message into something the bots can use
class Job
  attr_reader :id, :data_root, :receipt_handle

  def initialize(receipt_handle, body)
    @receipt_handle = receipt_handle
    @instructions = []
    populate_i_vars(body)
  end

  def domain
    @data_root
  end

  def url
    domain
  end

  # Take the body this job was instantiated with and turn it into a package
  # that can be used by this job.
  #
  # If the body is a csv, this job will get default actions to do a basic
  # scrape of a website.
  # The scrape includes the home page and the 'about us' and 'faq' footer
  # info-pages.
  #
  # If the body is JSON, we parse the JSON and use the values in it to populate
  # the i-vars. A JSON message should have the `:instructions`, `:data_root`
  # and `:id` keys, where `:instructions` is a list of instructions to run,
  #  `:id` is the job's id that we use to keep track of where data is coming
  # from etc. and the `:data_root` key holds the URL (or something similar)
  # where to start
  # running those instructions from; e.g. a product's PDP on various
  # competitor sites or some website's home page.
  def populate_i_vars(body)
    if (data = JSON.parse(body) rescue nil)
      puts "ok"
      @id = data['id']
      @data_root = data['data_root']
      @instructions = data['instructions']
    else
      puts "confused"
      @id, @data_root = *body.split(',')
      @instructions = default_instructions
    end
  end

  def default_instructions
    [
      { action: 'scrape_to_bag', hint: 'body' } # ,
      # { action: 'scrape_to_bag', hint: 'click_link("about us")' },
      # { action: 'scrape_to_bag', hint: 'click_link("faq")' }
    ]
  end

  # example output:
  #
  #     [
  #       { action: 'scrape_to_bag', hint: 'click_link "about us"' },
  #       { action: 'scrape_to_bag', hint: 'click_link("faq")' }
  #     ]
  def instructions
    @instructions ||= []
  end

  def to_hash
    {
      id: @id,
      data_root: @data_root,
      instructions: @instructions
    }
  end
end
