#!/usr/bin/ruby
require_relative './gunny.rb'
require_relative './web_recon.rb'

if $PROGRAM_NAME == __FILE__
  gunny = Gunny.new(ENV['QUEUE_URL'], ENV['RESULTS_DIR'])
  mission = WebRecon.new

  gunny.run_recon(mission)
else
  puts 'Gunny loaded from another file'
end
