import boto3
print('Lista de buckets: ')
s3resource = boto3.resource('s3','us-east-1')
buckets = s3resource.buckets.all()
for bucket in buckets:
    print(f'\t{bucket.name}') 