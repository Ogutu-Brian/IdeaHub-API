from ...authentication.tests.test_data import(
    first_name,
    last_name,
    email
)

FETCH_PROFILE_ENDPOINT = '/profile/profile'


class ResponseData:
    no_credentials_error = {
        'detail': 'Authentication credentials were not provided.'
    }

    fetch_profile = {
        'user': {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
    }
