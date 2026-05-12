import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Despliegue exitoso en AWS",
        "Microservicio DevOps activo",
        "Infraestructura como Codigo lista",
        "Monitoreo configurado correctamente",
        "Seguridad aplicada en la nube"
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': random.choice(mensajes),
            'servicio': 'microservicio-devops'
        })
    }
