from .models import LawyerImageModel
from .upload_image import upload_image_bucket, save_base64_to_image, get_image_url
class LawyersImages:
    
    # TODO: create a function to save the image in the database
    def save_image(self, image_file, lawyer_id) -> dict:
        # TODO: save image in S3 server
        image_path, id_unique = save_base64_to_image(lawyer_id, image_file)

        upload_image_bucket(image_path, id_unique)

        url_result = get_image_url(id_unique)

        print("url_result-------- ", url_result)

        # response_save_data = LawyerImageModel().save_lawyer_image(lawyer_id, image_file)
        # data_response = {
        #     "url_image": response_save_data,
        # }
        # https://parolegal-user.s3.us-west-1.amazonaws.com/mclovinnn.jpg
        data_response = {
            "url_image": "test",
        }
        return data_response

    def get_connection(self) -> any:
        lawyers_image = LawyerImageModel().get_all_lawyer_images()
        return lawyers_image

    # @classmethod
    # def get_lawyer_image(cls, lawyer_image

# class UploadImages:
    
    