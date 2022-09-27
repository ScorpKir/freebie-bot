import os


def get_env_array_str(key: str):
    env_value = os.getenv(key)
    if env_value != '':
        result = env_value.split(',')
        return result
    return None


def get_env_array_int(key: str):
    env_array_str = get_env_array_str(key)
    if env_array_str is not None:
        return [int(item) for item in get_env_array_str(key)]
    return None


def get_env_bool(key: str):
    env_value = os.getenv(key)
    if env_value in ('1', 't', 'true'):
        return True
    return False


