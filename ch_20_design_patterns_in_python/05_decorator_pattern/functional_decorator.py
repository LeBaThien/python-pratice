def make_bold(fn):
    def wrapped(*args, **kwargs):
        return f"<b>{fn()}</b>"

    return wrapped


def make_italic(fn):
    def wrapped(*args, **kwargs):
        return f"<i>{fn()}</i>"

    return wrapped


@make_bold
@make_italic
def hello():
    return "Hello World!"


if __name__ == '__main__':
    print(hello())
