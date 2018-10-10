import boto3
import json
import os


class JobFactory(object):
    def __init__(self, query):
        self.query = query
        self.redshift = boto3.client('redshift')

    def __iter__(self):
        for q, i in enumerate(self.redshift.run_query(self.query)):
            if i % 5000 == 0:
                print("Building Job {} with {}".format(i, q))

            j = build_job(q)
            yield j

    def build_job(q):
        return q.join(' ')


class JobSender(object):
def handler(event, context):
    for job, i in enumerate(JobFactory(event['Body'])):
        m = sqs.send_message(QueueUrl=os.getenv('BACKLOG_QUEUE'),
                             MessageBody=job)
        self.sqs = boto3.client('sqs')
    return m

    return build_response()
