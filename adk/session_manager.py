class SessionManager:

    def __init__(self):
        self.session_data = {}

    def save(self, key, value):
        self.session_data[key] = value

    def get(self, key):
        return self.session_data.get(key)

    def show_all(self):
        return self.session_data