from django.core.exceptions import ValidationError
import re
from functools import wraps


def validate_item_need(*need_be_in):
    @wraps(need_be_in)
    def validator(value):
        cleaned_value = set(value.lower().split())
        difference = set(need_be_in) - cleaned_value
        if len(difference) == len(need_be_in):
            raise ValidationError('Обязательно используйте слова: '
            f'{", ".join(need_be_in)}!')
        return value
    return validator


def validate_weight_range(value):
    begin = 0
    end = 32767
    if value not in range(begin, end + 1):
        raise ValidationError(f'Weight от {begin} до {end}!')

    return value


def validate_regex(value):
    if not re.fullmatch(r"^[a-zA-Z-_\d]*$", value):
        raise ValidationError('Запись должна содержать только буквы латинцы, цифры, - и _')

    return value
