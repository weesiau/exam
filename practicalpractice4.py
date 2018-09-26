def ValidateCode(code):
    allowed1 = 'WYZ'
    allowed2 = 'ABC'
    if len(code) == 4:
        if code[0] in allowed1:
            if code[1] in allowed2:
                if code[2] != 0:
                    return True
    return False

print(ValidateCode('YB23'))
