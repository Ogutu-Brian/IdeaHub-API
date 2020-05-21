APP_INITIAL = 'IdeaHub.apps'


def get_app_routes(app_name):
    return '{}.{}.urls'.format(APP_INITIAL, app_name)
