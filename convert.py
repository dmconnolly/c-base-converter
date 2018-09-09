import sublime
import sublime_plugin

supported_bases = [2, 8, 10, 16]

settings = sublime.load_settings('c-base-converter.sublime-settings')

def from_base(s : str, bases : list):
    for base in bases:
        val = val_from_base(s, base)
        if val != None:
            return val
    return None

def val_from_base(s : str, base : int):
    valid_input_format = True

    if base == 2:
        valid_input_format = s[:2].lower() == "0b"
    if base == 8:
        valid_input_format = s[0] == "0" and len(s) > 1
    if base == 10:
        valid_input_format = (s[0] != "0" or len(s) == 1) and s.isdigit()
    if base == 16:
        valid_input_format = s[:2].lower() == "0x"

    if not valid_input_format:
        return None

    try:
        return int(s, base)
    except ValueError:
        return None

def split_suffix(s : str):
    u_count = 0
    l_count = 0

    for c in s[len(s)-min(len(s)-1, 3):].lower():
        if "u" == c:
            u_count += 1
            if u_count > 1:
                return (None, None)

        elif "l" == c:
            l_count += 1
            if(l_count > 2):
                return (None, None)

    suffix = s[len(s) - (u_count + l_count):]
    s = s[:len(s)-len(suffix)]

    return (s, suffix)

def to_base(s : str, base : int):
    if not base in supported_bases:
        return None

    if not len(s) > 0:
        return None

    (s, suffix) = split_suffix(s)

    if s == None or len(s) > settings.get('max_value_length'):
        return None

    bases = list(supported_bases)

    try:
        bases.remove(base)
    except ValueError:
        pass

    val = from_base(s, bases)

    if(val == None):
        return None

    return val_to_base(val, base) + suffix

def val_to_base(val : int, base : int):
    if base == 2:
        return bin(val)
    if base == 8:
        return '0{:o}'.format(val)
    if base == 10:
        return str(val)
    if base == 16:
        return hex(val)
