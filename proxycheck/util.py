def format_params(kwargs) -> dict:
    params = {}
    for name, value in kwargs.items():
        if value is not None:
            if type(value) == bool:
                params[name] = int(value)
            else:
                params[name] = value

    return params
