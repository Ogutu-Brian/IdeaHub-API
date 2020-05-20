first_name = 'Brian'
last_name = 'O'
email = 'test@gmail.com'
password = 'testpassword'
confirm_password = 'testpassword'


class SignUpData:
    class TestData:
        complete_details = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }

        incomplete_details = {
            "last_name": last_name,
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }

    class ResponseData:
        incomplete_details_error = {
            "first_name": [
                "This field is required."
            ]
        }
