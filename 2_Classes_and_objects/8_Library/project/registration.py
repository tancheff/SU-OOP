from user import User
from library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        old_username = ""
        for user in library.user_records:
            if user.user_id == user_id:
                if new_username != user.username:
                    old_username = user.username
                    user.username = new_username

                    # change username in rented books:
                    for user_rented in library.rented_books:
                        if user_rented == old_username:
                            user_rented = new_username

                    return (f"Username successfully changed to: {new_username} "
                            f"for user id: {user.user_id}")
                else:
                    return (f"Please check again the provided username - "
                            f"it should be different than the username used so far!")
            else:
                return f"There is no user with id = {user_id}!"




