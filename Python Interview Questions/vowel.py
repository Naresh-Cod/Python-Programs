text = 'hello word'
count = sum(1 for i in text if i.lower() in 'aeiou')
print(count)