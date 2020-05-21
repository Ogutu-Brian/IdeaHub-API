SIGN_UP_ENDPOINT = '/authentication/sign-up'

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

        invalid_email_details = {
            "first_name": first_name,
            "last_name": last_name,
            "email": 'invalid@gmail',
            "password": password,
            "confirm_password": confirm_password
        }

        mismatching_password_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "confirm_password": 'another password'
        }

    class ResponseData:
        incomplete_details_error = {
            "first_name": [
                "This field is required."
            ]
        }

        ivalid_email_error = {
            "email": [
                "Enter a valid email address."
            ]
        }

        success_response = {
            "message": [
                "a verification code has been sent to your email."
            ]
        }

        user_exist_error = {
            "user": [
                "a user with this email address exist."
            ]
        }

        mismatching_password_error = {
            "password": [
                "the passwords do not match"
            ]
        }
