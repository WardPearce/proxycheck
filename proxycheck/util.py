from datetime import datetime


def format_params(kwargs) -> dict:
    params = {}
    for name, value in kwargs.items():
        if value is not None:
            if isinstance(value, bool):
                params[name] = int(value)
            elif isinstance(value, datetime):
                params[name] = value.strftime("%d-%B-%Y")
            else:
                params[name] = value

    return params
