## Freebie Bot

Бот для ВКонтакте, способный от лица пользователя анализировать по ключевым словам приходящие сообщения
и отвечать на них по заданным сценариям:

* Ответить на приходящее сообщение лично человеку заданным текстом
* Переслать сообщение нужному пользователю

## Требования:

---

* ``pip install -r requirements.txt``
* создать ``.env`` файл по шаблону:

## Пример .env-файла:

---

```
ACCESS_TOKEN=ТОКЕН
USER_IDS=1,2,3
CHAT_IDS=101,102,103
NEED_REPLY=1
REPLY_TEXT=Беру
KEYWORDS=отдам,отдаю,даром,бесплатно,раздам,раздаю,халява 
```

``ACCESS_TOKEN`` - токен доступа ВКонтакте  
``USER_IDS`` - это ID пользователей, которым необходимо переслать сообщение  
``CHAT_IDS`` - идентификаторы чата, которые необходимо прослушивать  
``NEED_REPLY`` - переменная, обозначающая отвечаем ли мы сразу отправителю или пересылаем куда-то сообщения  
``REPLY_TEXT`` - это сообщение, которое отправляется при ответе пользователю  
``KEYWORDS`` - слова из сообщений, на которые будет реагировать бот

# Взять ACCESS_TOKEN:

---
Cамый легкий путь - получить access token c помощью данного сайта:
https://vkhost.github.io/

# Получить ID чата:

---
При открытии в браузере диалога ВКонтакте в адресной строке будет находиться похожая ссылка:
``https://vk.com/im?sel=c170``.  
Строка ``sel=c170`` означает, что мы находимся в чате c идентификатором 170.
