import boto3

def upload(file, bucket):
    client = boto3.client('s3')
    with open(file, "rb") as f:
        client.upload_fileobj(f, bucket, file)


upload('data.csv', 'mydatau')
upload('plot.png', 'mydatau')

