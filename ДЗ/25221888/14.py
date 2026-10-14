alf = '0123456789abcdefg'

for x in alf:
    part1 = int(f'12346{x}17', 17)
    part2 = int(f'7{x}171', 17)
    total = part1 + part2
    if total % 16 == 0:
        print(total / 16)
    