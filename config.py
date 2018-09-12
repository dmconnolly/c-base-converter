import sublime
import sublime_plugin

_loaded = False

_bases = [
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

def plugin_loaded():
    global _loaded
    _loaded = True

def plugin_unloaded():
    global _loaded
    _loaded = False

def settings():
    if not _loaded:
        return None
    return sublime.load_settings('c-base-converter.sublime-settings')

def bases():
    s = settings()

    if not s:
        return []

    return [base for base in _bases if s.get(base['settings_string'], True)]
