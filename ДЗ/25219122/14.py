for x in "0123456789abcdefghijklmno":
    num1 = int(f"27{x}98876", 26)
    num2 = int(f"26{x}51", 26)
    num3 = int(f"15{x}47", 26)
    num4 = int(f"62{x}5", 26)
    total = num1+ num2+ num3 + num4
    if total % 25 ==0:
        print(total//25)