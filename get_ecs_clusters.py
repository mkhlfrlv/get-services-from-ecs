import boto3
import sys
from boto3 import exceptions
from botocore import exceptions


def get_ecs_clusters_in_all_regions():
    session = boto3.Session(profile_name='my_aws')
    ec2 = session.client('ec2', region_name="us-east-1")

    try:
        regions = [region_name['RegionName'] for region_name in ec2.describe_regions()['Regions']]
    except exceptions.ClientError as e:
        print(e)
        sys.exit(1)

    all_clusters = {}

    for region_name in regions:
        ecs_client = session.client('ecs', region_name=region_name)
        try:
            response = ecs_client.list_clusters()
            if response['clusterArns']:
                all_clusters[region_name] = response['clusterArns']
        except Exception as e:
            print(f"Error in region {region_name}: {str(e)}")

    return all_clusters


if __name__ == '__main__':
    clusters = get_ecs_clusters_in_all_regions()
    print(clusters)
