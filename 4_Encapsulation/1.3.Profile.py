class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        is_length_valid = len(value) >= 8
        is_upper_case_present = len([c for c in value if c.upper()]) > 0
        is_digit_present = len([c for c in value if c.isdigit()]) > 0

        if is_digit_present and is_upper_case_present and is_length_valid:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        silent_password_format = "*" * len(self.__password)
        return (f"You have a profile with username: \"{self.__username}\" "
                f"and password: {silent_password_format}")


# profile_with_invalid_password = Profile('My_username', 'My-password')
# print(profile_with_invalid_password)
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# print(profile_with_invalid_username)
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
