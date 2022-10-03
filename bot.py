import vk_api
from dotenv import load_dotenv
import os


class Bot:

    vk_session = None
    vk_api_access = None
    authorized = False

    def __init__(self):
        load_dotenv()
        self.vk_api_access = self.do_auth()

        if self.vk_api_access is not None:
            self.authorized = True

    def do_auth(self):
        access_token = os.getenv('ACCESS_TOKEN')
        try:
            self.vk_session = vk_api.VkApi(token=access_token)
            return self.vk_session.get_api()
        except Exception as error:
            print(error)
            return None
