# authentication/helper.py

def assign_id(obj: object, id_type: int = 4, key_name: str = None) -> str:
    """Assigns a unique identifier (UUID) to an object based on the specified type."""
    import uuid

    if id_type == 5:
        key = key_name if key_name else getattr(obj, "username", None)
        if not key:
            raise KeyError(
                "Object must have an attribute 'username' or a valid 'key_name' must be provided.")
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

    if id_type == 1:
        return str(uuid.uuid1())

    elif id_type == 3:
        key = key_name if key_name else getattr(obj, "username", None)
        if not key:
            raise KeyError(
                "Object must have an attribute 'username' or a valid 'key_name' must be provided.")
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, key))

    else:
        return str(uuid.uuid4())


def current_time(to_str: bool = True):
    from datetime import datetime
    """
    Return the current time. If to_str is True, return the time formatted as '%Y-%m-%dT%H:%M:%S.%f'.
    Otherwise, return the datetime object.
    """
    current_time = datetime.now()
    if to_str:
        formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return formatted_time
    else:
        return current_time


def log_f(data: any, dtype: str="py", file_name: str = "log.md", timing: bool = False) -> None:
    """ log message to console  """
    with open('log.md', 'a') as FILE:
        FILE.write(f'```{dtype}\n')
        if timing:
            from datetime import datetime
            FILE.write(f'{current_time()}')
        FILE.write(f'{data}\n')
        FILE.write('```\n')
