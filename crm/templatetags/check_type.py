"""
filters for checking the type of objects and formfields

Usage:

{% if form|obj_type:'mycustomform' %}
  <form class="custom" action="">
{% else %}
  <form action="">
{% endif %}


{% if field|field_type:'checkboxinput' %}
  <label class="cb_label">{{ field }} {{ field.label }}</label>
{% else %}
  <label for="id_{{ field.name }}">{{ field.label }}</label> {{ field }}
{% endif %}

"""

from django import template
register = template.Library()

def is_none(obj):
    try:
        return  True if obj == None else False
    except:
        pass
    return False

register.filter('is_none', is_none)

