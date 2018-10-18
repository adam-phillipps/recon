import boto3
import json
import os
import mysql.connector as mc
import numpy as np


def build_job(row):
    job = {
        'id': row[0],
        'brand': row[8],
        'description': row[6],
        'measurement': ' '.join(map(str, row[14:]))
    }
    return json.dumps(job)

def send_to_queue(sqs, message):
    sqs.send_message(QueueUrl=os.getenv('BACKLOG_QUEUE'),
                             MessageBody=message)

# If this file called directly...
#
#   1. get rows from db
#   2. send job to queue for each row
if __name__ == '__main__':
    sqs = boto3.client('sqs')
    fname = os.getenv('QUERY') or 'pdp_as_row.sql'
    fpath = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                         os.pardir,
                                         fname))
    with open(fpath, 'r') as fcontents:
        query = fcontents.read()
        conn = mc.connect(host=os.getenv('DBHOST'),
                          user=os.getenv('DBUSER'),
                          password=os.getenv('DBPASS'),
                          database=os.getenv('DBNAME'))
        client = conn.cursor()
        client.execute(query)
        result = client.fetchall()

        for job in result:
            send_to_queue(sqs, build_job(job))
