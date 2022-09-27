import os

from bot import Bot
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from nlp import parse_message


class ListenerBot(Bot):
    # Текущий экземпляр longpoll
    long_poll = None

    # Идентификаторы чатов для прослушивания
    chat_ids = None

    # Идентификаторы пользователей для пересылки
    default_user_ids = None

    # Идентификаторы чатов для пересылки
    default_chat_ids = None

    # Флаг надобности в ответе
    need_reply = False

    # Флаг надобности в пересылке в беседу
    needs_chat_sending = False

    # Флаг надобности в пересылке отдельным людям
    needs_person_sending = False

    # Текст ответа
    reply_text = None

    def __init__(self):
        super().__init__()
        self.long_poll = VkLongPoll(self.vk_session)
        self.chat_ids = [int(item) for item in os.getenv('CHAT_IDS').split(',')]
        self.default_chat_ids = [int(item) for item in os.getenv('SEND_CHAT_IDS').split(',')]
        self.default_user_ids = [int(item) for item in os.getenv('USER_IDS').split(',')]
        self.needs_chat_sending = bool(os.getenv('NEED_CHAT_SENDING'))
        self.needs_person_sending = bool(os.getenv('NEED_PERSON_SENDING'))
        self.need_reply = bool(os.getenv('NEED_REPLY'))
        self.reply_text = os.getenv('REPLY_TEXT')
        self.keywords = os.getenv('KEYWORDS').split(',')

    def reply_to_chat(self, chat_id, message_id, message_text):
        self.vk_session.method(
            'messages.send',
            {
                'chat_id': chat_id,
                'random_id': get_random_id(),
                'message': message_text,
                'forward_messages': [message_id]
            }
        )

    def reply_to_person(self, user_id, message_id, message_text):
        self.vk_session.method(
            'messages.send',
            {
                'user_id': user_id,
                'random_id': get_random_id(),
                'message': message_text,
                'forward_messages': [message_id]
            }
        )

    def run(self):
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.chat_id in self.chat_ids \
                    and parse_message(event.message, self.keywords):
                if self.need_reply:
                    self.reply_to_person(event.user_id, event.message_id, self.reply_text)
                elif self.needs_person_sending:
                    if self.default_user_ids is not None:
                        for user in self.default_user_ids:
                            self.reply_to_person(user, event.message_id, '')
                elif self.needs_chat_sending:
                    if self.default_chat_ids is not None:
                        for chat in self.default_chat_ids:
                            self.reply_to_chat(chat, event.message_id, '')
