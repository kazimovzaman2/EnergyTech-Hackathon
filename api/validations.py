from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    abonet_code = data['abonet_code'].strip()
    password = data['password'].strip()
    ##
    if not abonet_code or UserModel.objects.filter(abonet_code=abonet_code).exists():
        raise ValidationError('choose another abonet code')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    return data

def validate_abonet_code(data):
    abonet_code = data['abonet_code'].strip()
    if not abonet_code:
        raise ValidationError('an abonet code is needed')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True
