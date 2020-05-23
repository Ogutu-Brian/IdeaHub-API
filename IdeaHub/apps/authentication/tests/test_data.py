from ..utils.response_messages import ResponseMessages

SIGN_UP_ENDPOINT = '/authentication/sign-up'
VERIFICATION_ENDPOINT = '/authentication/verify'
LOGIN_ENDPOINT = '/authentication/login'


first_name = 'Brian'
last_name = 'O'
email = 'test@gmail.com'
password = 'testpassword'
confirm_password = 'testpassword'
unexisting_email = 'unexisting@gmail.com'
invalid_code = 'invalid code'
invalid_password = 'invalid password'


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

        invalid_email_error = {
            'email': [
                'Enter a valid email address.'
            ]
        }

        success_response = {
            'message': [
                ResponseMessages.success_signup_message
            ]
        }

        user_exist_error = {
            'user': [
                ResponseMessages.existing_user_error_message
            ]
        }

        mismatching_password_error = {
            'password': [
                ResponseMessages.unmatching_password_error
            ]
        }

        missing_email_field_error = {
            'email': [
                'This field is required.'
            ]
        }

        mismatching_verification_code_error = {
            'verification_code': [
                ResponseMessages.mismatching_verification_code
            ]
        }

        user_does_not_exist_error = {
            'user': [
                ResponseMessages.unexisting_user_error
            ]
        }

        verify_user_response = {
            'message': [
                ResponseMessages.successful_account_verification
            ]
        }

        unverified_user_error = {
            'user': [
                ResponseMessages.unverified_account_error
            ]
        }

        invalid_password_error = {
            'message': [
                ResponseMessages.invalid_password_error
            ]
        }

        multiple_verification_error = {
            'verification_code': [
                ResponseMessages.multiple_verification_error
            ]
        }
