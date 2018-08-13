import boto3

def email_handler(event, context):
	print('lambda start')
	jsonStr= json.dumps(event)
	print(jsonStr)
	emailSubject= 'job status'
    sns=boto3.resource('sns')
    mytopic_arn='test'
    response = sns.publish(mytopic_arn, jsonStr)}