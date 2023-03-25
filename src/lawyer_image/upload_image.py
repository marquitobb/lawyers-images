import os
import uuid
import base64
from typing import Tuple

import boto3
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

def save_base64_to_image(id_lawyer:int, str_base64: str)-> Tuple[str, str]:
    decoded_image = base64.b64decode(str_base64)
    image = Image.open(BytesIO(decoded_image))

    current_dir = os.getcwd()

    id_unique: str = str(uuid.uuid4()).replace("-","") + "_" + str(id_lawyer)

    path = "src/assets/" + id_unique + ".jpg"

    # Formar el path completo de la imagen
    image_path = os.path.join(current_dir, path)

    # save image in the path
    image.save(image_path)

    return image_path, id_unique

def upload_image_bucket(image_path: str, id_unique: str) -> bool:
    with open(image_path, "rb") as f:
        img = f.read()
    try:
        s3_client = boto3.resource(
            "s3",
            aws_access_key_id=str(os.environ.get('AWS_ACCESS_KEY_ID')),
            aws_secret_access_key=os.environ.get('AWS_ACCESS_SECRET_KEY'),
            region_name=os.environ.get('AWS_BUCKET_REGION')
        )
        s3_client.Bucket(os.environ.get('AWS_BUCKET_NAME')).put_object(
            Key=f"{id_unique}.jpg", Body=img
        )

        # finally deleted file
        if os.path.isfile(image_path):
            os.remove(image_path)

        return True
    except Exception as e:
        print(e)
        return False

def get_image_url(id_unique: str) -> str:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=str(os.environ.get('AWS_ACCESS_KEY_ID')),
        aws_secret_access_key=os.environ.get('AWS_ACCESS_SECRET_KEY'),
        region_name=os.environ.get('AWS_BUCKET_REGION')
    )
    object_url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': os.environ.get('AWS_BUCKET_NAME'),
            'Key': f"{id_unique}.jpg"
        }
    )
    return object_url