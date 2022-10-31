from django.core.exceptions import ValidationError


def validate_item_need(value):
    need_be_in = {'превосходно', 'роскошно', }
    cleaned_value = set(value.lower().split())

    difference = need_be_in - cleaned_value

    if len(difference) == len(need_be_in):
        raise ValidationError(f'Обязательно используйте слова {need_be_in}!')

    return value


def validate_weight_range(value):
    begin = 0
    end = 32767
    if not begin < value < end:
        raise ValidationError(f'Weight от {begin} до {end}!')

    return value
