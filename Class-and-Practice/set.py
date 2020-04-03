myset = {'khan'}
print(myset)

myset2 = set('asifulmamun')
print(myset2)

# set comprehension
compressed = {f for f in "abcdef" if f not in "abcd"}
print(compressed)

compressed = {f for f in "abcdef" if f in "abcdk"}
print(compressed)

first = set("abcdef")
second = set("abc")

print(first | second)
print(first & second)
print(first ^ second)