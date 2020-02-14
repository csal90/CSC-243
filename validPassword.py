def validPwd(pwd):
    if len(pwd) < 8:
        return False
    count_alphabet = 0
    count_digit = 0
    count_specialchar = 0
    for c in pwd:
        if c.isalpha():
            count_alphabet += 1
        if c.isalpha():
            count_digit += 1
        if c in '!@#$%^&*':
            count_specialchar += 1
        return count_alphabet > 0 and count_digit > 0 and count_specialchar