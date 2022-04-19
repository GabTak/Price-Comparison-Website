from django.template.defaulttags import register

@register.filter
def multiply(a, b):
    return a * b

    