def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper
