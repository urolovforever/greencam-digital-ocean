from django.utils.translation import get_language


def get_translated(obj, field_name):
    """Return the translated field value based on current language.
    Falls back to the default (English) field if translation is empty."""
    lang = get_language() or 'en'
    if lang == 'uz':
        uz_value = getattr(obj, f'{field_name}_uz', '') or ''
        if uz_value.strip():
            return uz_value
    return getattr(obj, field_name, '')
