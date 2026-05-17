def printer_error(s):
    return f"{len([char for char in s if char > 'm'])}/{len(s)}"