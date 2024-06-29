import boto3
import sys
from boto3 import exceptions
from botocore import exceptions


def get_service_environment_variables(region_name: str, cluster_name: str, service_name: str):
    session = boto3.Session(profile_name='qa')
    ecs = session.client(service_name='ecs', region_name=region_name)

    try:
        service_response = ecs.describe_services(
            cluster=cluster_name,
            services=[service_name]
        )
    except exceptions.ClientError as e:
        print(e)
        sys.exit(1)

    task_definition_arn = service_response['services'][0]['taskDefinition']

    task_def_response = ecs.describe_task_definition(
        taskDefinition=task_definition_arn
    )
    container_definitions = task_def_response['taskDefinition']['containerDefinitions']

    environment_vars = {}
    for container in container_definitions:
        environment_vars[container['name']] = {env_var['name']: env_var['value'] for env_var in container['environment']}
    return environment_vars


if __name__ == '__main__':
    cluster = '******'
    service = '******'
    service = get_service_environment_variables(cluster, service)
    for variable in service['******']:
        print(variable)
