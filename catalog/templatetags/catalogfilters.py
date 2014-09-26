from django import template
import locale
from decimal import Decimal

register = template.Library()

@register.filter(name = 'currency')
def currency(value):
    if value == '':
        value = 0
    value = Decimal(value)
    try:
        locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL,'')
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping = True)