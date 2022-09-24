def parse_message(message, keywords):
    for item in keywords:
        if item in message.lower():
            return True
    return False
