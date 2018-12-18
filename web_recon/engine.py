from webrecon import gcse, agent
import conversions
import boto3
import redis


sqs = boto3.client('sqs')
cache = redis.Redis(
    host=gcse._lookfor('CACHE_HOST'),
    port=gcse._lookfor('CACHE_PORT'),
    password=gcse._lookfor('CACHE_PASS'))

while _job_count() > 0:
    job = sqs.receive_message(QueueUrl=gcse._lookfor('BACKLOG_URL'),
                              MaxNumberOfMessages=1,
                              VisibilityTimeout=gcse._lookfor('JOB_TIME'),
                              WaitTimeSeconds=20)['Messages'][0]

    rec_handle = job['ReceiptHandle']
    jbody = job['Body']

    origin_id, func, params = _parse_params(jbody)
    replay_steps = cache.lslice(f"{origin_id}:replay", 0, -1)

    # replay all the steps that have already happened to get back to the point
    # where the last recon agent passed this job off
    tmpres = None
    for step in replay_steps:
        runnable   = abilities.import_pkg_and_get_func(step)
        num_params = abilities.params_count(runnable)
        params     = cache.lslice(f"{origin_id}:params", 0, num_params)
        tmpres     = runnable(params)

    objectives = cache.hgetall(f"{origin_id}:objectives")
    fulfill(objectives, tmpres)
    # update the index with the actions taken and the results
    report_actions(es)


@record_actions(es)
def fulfill(objectives, context):
    results = []
    for objective in objectives:
        getter = abilities.getter(objective)
        result = getter(context)
        results.append(result)

    return results


def _job_count():
    return sqs.get_queue_attributes(QueueUrl='',
                                    AttributeNames=['ApproximateNumberOfMessages'])
