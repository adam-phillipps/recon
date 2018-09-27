require 'aws-sdk-s3'
require 'aws-sdk-sqs'
require_relative './job.rb'

# Load bots and the config they need to run
class Gunny
  def initialize(queue_url, results_dir)
    puts "Starting Gunny with queue_url: #{queue_url} and results_dir: #{results_dir}"
    @queue_url = queue_url
    @results_dir = results_dir
  end

  def s3
    @s3 ||= Aws::S3::Client.new(region: 'us-west-2')
  end

  def sqs
    @sqs ||= Aws::SQS::Client.new(region: 'us-west-2')
  end

  # Get the next message from the queue and yield it for whatever
  # method that called this one.
  def next_job
    opts = {
      queue_url: @queue_url, max_number_of_messages: 1,
      visibility_timeout: 120, wait_time_seconds: 20
    }
    begin
      job = nil # hoisting for better error messages
      msg = sqs.receive_message(opts)
      puts "Recieved from #{queue_name}: #{msg.messages.first}"
      job = Job.new(msg.messages.map(&:receipt_handle).first, msg.messages.map(&:body).first)
    rescue Aws::SQS::Errors::ServiceError => ex
      puts "Failed job: #{job} with: #{ex}"
    end
  end

  def job_count
    opts = {
      queue_url:  @queue_url,
      attribute_names: ['ApproximateNumberOfMessages']
    }
    count = sqs.get_queue_attributes(opts)['attributes']['ApproximateNumberOfMessages'].to_i
    puts "#{count} jobs exist in the #{queue_name} queue"
    count
  end

  def queue_name
    @queue_url.gsub(/.*\/(\w+)$/, '\1')
  end

  def run_recon(recon_bot)
    while job_count > 0
      puts 'Jobs exist so Gunny is deploying recon bots'
      job = next_job
      results = recon_bot.process(job)
      puts "Received results from recon: #{results}"
      post_results(job.id.to_s, results)
      puts "Deleting queue message from successful job: #{job.id}"
      sqs.delete_message(queue_url: @queue_url, receipt_handle: job.receipt_handle)
    end
  end

  def post_results(file_name, results)
    puts "Posting #{results} to #{@results_dir}"
    s3.put_object(body: results, bucket: @results_dir, key: file_name)
  end
end
