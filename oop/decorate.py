import webbrowser


def validator(func):
    def wrapper(url):
        # print("text before")
        if "." in url:
            func(url)
        else:
            print("incorrect url")
        # print("text after")

    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)


open_url("https://github.com")
