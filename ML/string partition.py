text = "heyy"
res = []
for i in range(0, len(text)):
    for j in range(i+1, len(text)+1):
        res.append(text[i:j])

print(res)
