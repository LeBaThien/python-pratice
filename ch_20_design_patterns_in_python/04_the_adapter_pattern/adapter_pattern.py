class FacebookUser:
    def login_facebook(self):
        return "User logger in with Facebook"


class GoogleUser:
    def login_google(self):
        return "User logged in with Google"


class LoginAdapter:
    def __init__(self, user, login_method):
        self.user = user
        self.login_method = login_method

    def login(self):
        return getattr(self.user, self.login_method)()


if __name__ == '__main__':
    facebook_user = FacebookUser()
    google_user = GoogleUser()

    facebook_adapter = LoginAdapter(facebook_user, "login_facebook")
    google_adapter = LoginAdapter(google_user, "login_google")

    print(facebook_adapter.login())
    print(google_adapter.login())