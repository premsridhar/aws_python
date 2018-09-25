import boto3
import click

session = boto3.Session(profile_name = 'pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('List-Buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print (bucket)

@cli.command('List-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List bucket objects"
    for obj in s3.Bucket(bucket).objects.all():
        print (obj)

if __name__ == '__main__':
    cli()
