import boto3
import sys
from boto3 import exceptions
from botocore import exceptions


def get_ecs_cluster_services(clusters_list: dict):
    session = boto3.Session(profile_name='qa')
    regions_clusters = {}

    for key, value in clusters_list.items():
        ecs = session.client('ecs', region_name=key)
        paginator = ecs.get_paginator('list_services')
        cluster_services_arns = {}
        for cluster_arn in value:
            services_arns = []
            try:
                for page in paginator.paginate(cluster=cluster_arn):
                    services_arns.extend(page['serviceArns'])
                    services_arns_converted_to_dict = {item: {} for item in services_arns}
                    cluster_services_arns[cluster_arn] = services_arns_converted_to_dict
            except exceptions.ClientError as e:
                print(e)
                sys.exit(1)

            regions_clusters[key] = cluster_services_arns

    return regions_clusters


if __name__ == '__main__':
    cluster_list = {'eu-west-1': ['****', '***'], }
    services = get_ecs_cluster_services(cluster_list)
    print(services)
