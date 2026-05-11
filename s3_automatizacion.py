import boto3
import os

s3 = boto3.client('s3')
BUCKET_NAME = 'bucket-devops-286768452536'
FILE_NAME = 'test_archivo.txt'

#crea archivo local
with open(FILE_NAME, 'w') as f:
    f.write("Archivo de prueba para automatizacion S3.")

# lo sube a la carpeta d pruebas
s3.upload_file(FILE_NAME, BUCKET_NAME, f'pruebas/{FILE_NAME}')
print(f"Archivo {FILE_NAME} subido econ exito")

# lista los objetos
print("\nListado de objetos en el bucket:")
response = s3.list_objects_v2(Bucket=BUCKET_NAME)

if 'Contents' in response:
    for obj in response['Contents']:
        print(f"Nombre: {obj['Key']} | Tamaño: {obj['Size']} bytes | Modificado: {obj['LastModified']}")
else:
    print("El bucket esta vacio")
