from django.core.exceptions import ValidationError
import re
from django.utils.deconstruct import deconstructible
from bs4 import BeautifulSoup


@deconstructible
class validate_item_need():
    def __init__(self, *need_be_in):
        self.need_be_in = need_be_in

    def __call__(self, value):
        cleaned_value = set(BeautifulSoup(value.lower(), features="html.parser").find_all(text=True))
        difference = set(self.need_be_in) - cleaned_value
        if len(difference) == len(self.need_be_in):
            raise ValidationError(
                'Обязательно используйте слова: '
                f'{", ".join(self.need_be_in)}!'
            )

        return value


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
