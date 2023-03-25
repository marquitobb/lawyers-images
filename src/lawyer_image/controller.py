from .models import LawyerImageModel
from .upload_image import upload_image_bucket, save_base64_to_image, get_image_url

class LawyersImages:
    def save_image(self, image_file, id_lawyer) -> dict:
        image_path, id_unique = save_base64_to_image(id_lawyer, image_file)

        if not upload_image_bucket(image_path, id_unique):
            return {"message": "Error uploading image","success":True}

        url_result: str = get_image_url(id_unique)

        if LawyerImageModel().save_lawyer_image(id_lawyer, url_result):
            return {"url_image": url_result, "success":True}

        return {"message": "Error uploading image","success":True}

