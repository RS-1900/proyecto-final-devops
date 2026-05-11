import boto3
import time

db = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'devops-tabla'

# 1. Crear tabla
try:
    table = db.create_table(
        TableName=table_name,
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    print("Creando tabla..............")
    table.wait_until_exists()
except Exception as e:
    print(f"La tabla ya existe o sucedio un error: {e}")
    table = db.Table(table_name)

# 2. Insertar registro
table.put_item(Item={'id': '001', 'nombre': 'UsuarioPrueba', 'status': 'activo'})
print("Registro insertado")

# 3. Modificar campo (usando alias para 'status')
table.update_item(
    Key={'id': '001'},
    UpdateExpression="SET #s = :nuevo_status",
    ExpressionAttributeNames={'#s': 'status'},
    ExpressionAttributeValues={':nuevo_status': 'procesado'}
)
print("Registro actualizado")

# 4. Eliminar registro
table.delete_item(Key={'id': '001'})
print("Registro eliminado con exito")
