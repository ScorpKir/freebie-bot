import os

from bot import Bot
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from parser import parse_message


class ListenerBot(Bot):
    long_poll = None
    chat_ids = None
    need_reply = False
    reply_text = None

    def __init__(self):
        super().__init__()
        self.long_poll = VkLongPoll(self.vk_session)
        self.chat_ids = [int(item) for item in os.getenv('CHAT_IDS').split(',')]
        self.need_reply = int(os.getenv('NEED_REPLY'))
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
                else:
                    for user in self.default_user_ids:
                        self.reply_to_person(user, event.message_id, '')
