import sublime
import sublime_plugin

bases = [
    {
        'value': 2,
        'string': 'Binary',
        'settings_string': 'binary_enabled'
    },
    {
        'value': 8,
        'string': 'Octal',
        'settings_string': 'octal_enabled'
    },
    {
        'value': 10,
        'string': 'Decimal',
        'settings_string': 'decimal_enabled'
    },
    {
        'value': 16,
        'string': 'Hexidecimal',
        'settings_string': 'hexidecimal_enabled'
    }
]

enabled_bases = []

settings = None

def plugin_loaded():
    global settings
    global enabled_bases

    settings = sublime.load_settings('c-base-converter.sublime-settings')

    enabled_bases = []
    for base in bases:
        if settings.get(base['settings_string'], True):
            enabled_bases.append(base)
