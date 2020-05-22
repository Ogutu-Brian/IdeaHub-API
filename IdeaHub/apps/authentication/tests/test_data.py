SIGN_UP_ENDPOINT = '/authentication/sign-up'
VERIFICATION_ENDPOINT = '/authentication/verify'

first_name = 'Brian'
last_name = 'O'
email = 'test@gmail.com'
password = 'testpassword'
confirm_password = 'testpassword'
unexisting_email = 'unexisting@gmail.com'
invalid_code = 'invalid code'


class SignUpData:
    class TestData:
        complete_details = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }

        incomplete_details = {
            'last_name': last_name,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }

        invalid_email_details = {
            'first_name': first_name,
            'last_name': last_name,
            'email': 'invalid@gmail',
            'password': password,
            'confirm_password': confirm_password
        }

        mismatching_password_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'confirm_password': 'another password'
        }

    class ResponseData:
        incomplete_details_error = {
            'first_name': [
                'This field is required.'
            ]
        }

        ivalid_email_error = {
            'email': [
                'Enter a valid email address.'
            ]
        }

        success_response = {
            'message': [
                'a verification code has been sent to your email.'
            ]
        }

        user_exist_error = {
            'user': [
                'a user with this email address exist.'
            ]
        }

        mismatching_password_error = {
            'password': [
                'the passwords do not match'
            ]
        }

        missing_verification_field_error = {
            'email': [
                'This field is required.'
            ]
        }

        mismatching_verification_code_error = {
            'verification_code': [
                'The verification code does not match.'
            ]
        }

        user_does_not_exist_error = {
            'user': [
                'A user with this email address does not exist.'
            ]
        }
