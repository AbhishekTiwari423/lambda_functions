import boto3

def upload_file_to_s3(file_name, bucket, object_name=None):
	"""Upload a file to an S3 bucket

	:param file_name: File to upload
	:param bucket: Bucket to upload to
	:param object_name: S3 object name. If not specified then file_name is used
	:return: True if file was uploaded, else False
	"""
	ACCESS_KEY = "<your access key"
	SECRET_KEY = "<your secret key>"
	# If S3 object_name was not specified, use file_name
	if object_name is None:
		object_name = file_name.split("\\")[-1]

	# Upload the file
	# s3_client = boto3.client('s3')
	s3_client = boto3.client(
				    's3',
				    aws_access_key_id=ACCESS_KEY,
				    aws_secret_access_key=SECRET_KEY
				)
	try:
		response = s3_client.upload_file(file_name, bucket, object_name)
	except ClientError as upload_error:
		return False

	return True


if __name__ == '__main__':
	file_name =""
	bucket =""
	upload_file_to_s3(file_name, bucket)
	print('package updated ')
