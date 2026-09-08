with open("17.txt") as f:
    listed = [int(x) for x in f.readlines()]


counter = 0
max_value = max(listed)
max_answer = float('-inf')

for i in range(len(listed) - 2):
    no_zero_count = sum(str(listed[i + j]).count("0") == 0 for j in range(3))
    if no_zero_count >= 2 and listed[i] + listed[i+1] + listed[i+2] < max_value/2:
        counter += 1
        max_answer = max(max_answer, listed[i] + listed[i+1] + listed[i+2])

print(counter, max_answer)