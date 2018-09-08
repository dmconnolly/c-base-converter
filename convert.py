supported_bases = [2, 8, 10, 16]
max_string_length = 18

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
        valid_input_format = s[0].lower() == "0"
    if base == 10:
        valid_input_format = s[0] != "0" and s.isdigit()
    if base == 16:
        valid_input_format = s[:2].lower() == "0x"

    if not valid_input_format:
        return None

    try:
        return int(s, base)
    except ValueError:
        return None

def to_base(s : str, base : int):
    if not base in supported_bases:
        return None

    if not 1 <= len(s) <= max_string_length:
        return None

    bases = list(supported_bases)

    try:
        bases.remove(base)
    except ValueError:
        pass

    val = from_base(s, bases)

    if(val == None):
        return None

    return val_to_base(val, base)

def val_to_base(val : int, base : int):
    if base == 2:
        return bin(val)
    if base == 8:
        return '0{:o}'.format(val)
    if base == 10:
        return str(val)
    if base == 16:
        return hex(val)
