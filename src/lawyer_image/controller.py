from .models import LawyerImageModel

class LawyersImages:
    @classmethod
    def get_connection(cls) -> any:
        lawyers_image = LawyerImageModel().get_all_lawyer_images()
        return lawyers_image