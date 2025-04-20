s = 'ababa'
output = {}

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        output[sub] = output.get(sub, 0) + 1

print(output)
