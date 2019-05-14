from django import template

register = template.Library();

@register.filter
def get_at_index(list, index):
    return list[index];

@register.filter
def index_in_set(index, list):
    if index in list:
        return True;
    else:
        return False;
