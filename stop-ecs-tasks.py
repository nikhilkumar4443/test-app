import boto3


def lambda_handler(event, context):
    client = boto3.client('ecs')
    cluster_name = "test"
    services = client.list_services(
        cluster=cluster_name
    )['serviceArns']
    
    print(services)
    for service_arn in services:
        service_name=service_arn.split("/")[2]
        tasks = client.list_tasks(
            cluster=cluster_name,
            serviceName=service_name
        )['taskArns']
        for task in tasks:
            
            print(f"stopping task with ID {task}")
            resp=client.stop_task(
                cluster=cluster_name,
                task=task
            )
            print(resp)
            
    return {
        'statusCode': 200
    }
