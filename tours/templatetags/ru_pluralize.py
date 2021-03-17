from django import template

register = template.Library()


@register.filter
def ru_pluralize(value, arg="дурак,дурака,дураков"):
    args = arg.split(",")
    number = abs(int(value))
    a = number % 10
    b = number % 100

    if (a == 1) and (b != 11):
        return f"{number} {args[0]}"
    elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
        return f"{number} {args[1]}"
    else:
        return f"{number} {args[2]}"
