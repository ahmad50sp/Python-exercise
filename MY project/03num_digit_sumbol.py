inputString = "P@#yn26at^&i5ve"
char_count = 0
symbol_count = 0
digit_count = 0
for char_count in inputString:
    if char_count.isalpha():
        char_count += 1
    elif digit_count.isdigit():
        digit_count += 1
    else:
        symbol_count.issymbol()
        symbol_count += 1
    print("leters :", char_count)
    print("digit :", digit_count)
    print("symbol", symbol_count)
