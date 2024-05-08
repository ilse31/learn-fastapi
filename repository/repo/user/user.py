


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user(self, user_id):
        return self.db.get_user(user_id)

    def create_user(self, user):
        return self.db.create_user(user)

    def update_user(self, user):
        return self.db.update_user(user)

    def delete_user(self, user_id):
        return self.db.delete_user(user_id)