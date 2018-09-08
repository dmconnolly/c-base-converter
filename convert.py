max_string_length = 18

def from_bin(s : str):
    if(s[:2].lower() != "0b"):
        return None
    try:
        return int(s, 2)
    except ValueError:
        return None

def from_oct(s : str):
    if(s[0].lower() != "0"):
        return None
    try:
        return int(s, 8)
    except ValueError:
        return None

def from_dec(s : str):
    try:
        return int(s, 10)
    except ValueError:
        return None

def from_hex(s : str):
    if(s[:2].lower() != "0x"):
        return None
    try:
        return int(s, 16)
    except ValueError:
        return None

def get_val(s : str):
    if len(s) <= max_string_length:
        val = from_oct(s)
        if(val != None): return val

        val = from_dec(s)
        if(val != None): return val

        val = from_hex(s)
        if(val != None): return val

        val = from_bin(s)
        if(val != None): return val

    return None
