N = int(input())

numberFirst = []
numberSecond = []

for i in range(1, N + 1):
    numbers = input()
    numberFirst.append(numbers[1])
    numberSecond.append(numbers[0])

merged = []
squashed = []

for l in range(N - 1):
    sum = numberFirst[l] + numberSecond[l+1]
    merged.append(sum)
    squash = numberSecond[l] + str(int(numberFirst[l]) +
                                   int(numberSecond[l+1])) + numberFirst[l+1]
    if len(squash) == 4:
        squash = squash[0] + squash[2:]

    squashed.append(squash)


res1 = [eval(o) for o in merged]
res2 = [eval(y) for y in squashed]


output = ''

for q in res1:
    output = output + str(q) + ' '


withoutSuffix1 = output.removesuffix(',')

print(withoutSuffix1)

output2 = ''

for m in res2:
    output2 = output2 + str(m) + ' '
withoutSuffix2 = output2.removesuffix(',')


print(withoutSuffix2)
