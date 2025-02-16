
def is_password_secure(s):
    validation = False
    special_char = ""
    lower_char = ""
    upper_char = ""
    digit_char = ""

    for char in s:
        if not char.isalpha() and not char.isdigit():
            special_char += char
        elif char.isalpha() and char.islower():
            lower_char += char
        elif char.isalpha() and char.isupper():
            upper_char += char
        elif char.isdigit():
            digit_char += char

    if len(s) >= 8 and len(special_char) >= 1:
        if len(lower_char) >= 1 and len(upper_char) >= 1:
            if len(lower_char) >= 1 and len(digit_char) >= 1:
                validation = True
    return validation
