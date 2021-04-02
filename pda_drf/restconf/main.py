REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [            # You can use list[] or tuple(). i used list.
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',   # Oauth, JWT
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}