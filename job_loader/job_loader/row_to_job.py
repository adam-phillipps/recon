import boto3
import json
import mysql.connector as db
import numpy as np
import os
import conversions


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
        conn = db.connect(host=os.getenv('DBHOST'),
                          user=os.getenv('DBUSER'),
                          password=os.getenv('DBPASS'),
                          database=os.getenv('DBNAME'))
        client = conn.cursor()
        client.execute(query)
        result = client.fetchall()

        for job in result:
          sqs.send_message(QueueUrl=os.getenv('BACKLOG'),
                           MessageBody=build_job(job))
