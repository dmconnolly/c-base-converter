import sublime
import sublime_plugin
import math

supported_bases = [2, 8, 10, 16]

settings = {}

#sublime.error_message("!!")

def plugin_loaded():
    settings = sublime.load_settings('c-base-converter.sublime-settings')

def get_base(s : str):
    if len(s) > 2 and s[:2].lower() == "0b":
        # Binary
        return (2, 2)
    elif len(s) > 2 and s[:2].lower() == "0x":
        # Hexidecimal
        return (2, 16)
    elif s[0] == "0":
        #Octal
        return (1, 8)
    elif s.isnumeric():
        # Decimal
        return (0, 10)
    else:
        # Invalid
        return (None, None)

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

    (prefix_len, current_base) = get_base(s)

    if s == None or current_base == None:
        return None

    (s, suffix) = split_suffix(s)

    if not s:
        return None

    max_val = (2 ** settings.get('max_value_bits', 64)) - 1
    max_len = math.ceil(math.log(max_val) / math.log(current_base))

    if (len(s) - prefix_len) > max_len:
        return None

    if current_base == base:
        return None

    try:
        val = int(s, current_base)
    except ValueError:
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
