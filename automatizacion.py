import boto3
from datetime import datetime, timedelta

# Configuración de los clientes de AWS
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
s3 = boto3.client('s3')
autoscaling = boto3.client('autoscaling')

def listar_instancias_ec2():
    print("\n--- Instancias EC2 ---")
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | Tipo: {instance['InstanceType']} | Estado: {instance['State']['Name']}")

def reporte_cpu_cloudwatch():
    print("\n--- Reporte de CPU en las ultimas 24 hrs ---")
    instancias = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for reservation in instancias['Reservations']:
        for instance in reservation['Instances']:
            id_instancia = instance['InstanceId']
            
            stats = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': id_instancia}],
                StartTime=datetime.utcnow() - timedelta(hours=24),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )
            
            if stats['Datapoints']:
                promedio = stats['Datapoints'][0]['Average']
                print(f"Instancia {id_instancia}: CPU Promedio {promedio:.2f}%")
            else:
                print(f"Instancia {id_instancia}: Sin metricas disponibles.")

def listar_s3_y_objetos():
    print("\n--- Buckets S3 y Objetos ---")
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        nombre_bucket = bucket['Name']
        print(f"Bucket: {nombre_bucket}")
        
        objetos = s3.list_objects_v2(Bucket=nombre_bucket)
        if 'Contents' in objetos:
            for obj in objetos['Contents']:
                print(f"  - Objeto: {obj['Key']}")
        else:
            print("  - (Bucket vacio)")

def consultar_autoscaling():
    print("\n--- Grupos de Auto Scaling ---")
    response = autoscaling.describe_auto_scaling_groups()
    for asg in response['AutoScalingGroups']:
        print(f"Nombre: {asg['AutoScalingGroupName']}")
        print(f"  Capacidad Minima: {asg['MinSize']}")
        print(f"  Capacidad Maxima: {asg['MaxSize']}")
        print(f"  Capacidad deseada: {asg['DesiredCapacity']}")

if __name__ == "__main__":
    listar_instancias_ec2()
    reporte_cpu_cloudwatch()
    listar_s3_y_objetos()
    consultar_autoscaling()
