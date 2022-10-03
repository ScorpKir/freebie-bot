## Freebie Bot

Бот для ВКонтакте, способный от лица пользователя анализировать по ключевым словам приходящие сообщения
и отвечать на них по заданным сценариям:

* Ответить на приходящее сообщение лично человеку заданным текстом
* Переслать сообщение нужным пользователям (пользователю)
* Переслать сообщение в нужные чаты (чат)

## Требования:


* ``pip install -r requirements.txt``
* создать ``.env`` файл по шаблону:

## Пример .env-файла:


```
ACCESS_TOKEN=ТОКЕН
USER_IDS=1,2,3
SEND_CHAT_IDS=1,2,3
CHAT_IDS=1,2
NEED_CHAT_SENDING=0
NEED_PERSON_SENDING=1
NEED_REPLY=0
REPLY_TEXT=Беру бесплатно, какая комната?
KEYWORDS=отдам,отдаю,даром,бесплатно,раздам,раздаю,халява
```

``ACCESS_TOKEN`` - токен доступа ВКонтакте  
``USER_IDS`` - ID пользователей, которым необходимо переслать сообщение  
``SEND_CHAT_IDS`` - ID чатов, куда необходимо будет пересылать  
``CHAT_IDS`` - идентификаторы чата, которые необходимо прослушивать  
``NEED_CHAT_SENDING`` - переменная, обозначающая пересылаем ли мы сообщения в беседы  
``NEED_PERSON_SENDING`` - переменная, отправляем ли мы сообщение отдельным людям  
``NEED_REPLY`` - переменная, обозначающая отвечаем ли мы сразу отправителю  
``REPLY_TEXT`` - сообщение, которое отправляется при ответе пользователю  
``KEYWORDS`` - слова из сообщений, на которые будет реагировать бот

## Взять ACCESS_TOKEN:

* Cамый легкий путь - получить access token c помощью данного сайта:
https://vkhost.github.io/

## Получить ID чата:

При открытии в браузере диалога ВКонтакте в адресной строке будет находиться похожая ссылка:
``https://vk.com/im?sel=c170``.  
Строка ``sel=c170`` означает, что мы находимся в чате c идентификатором 170.
