from stack import Stack
#from tuplestack import Stack

s = Stack()
s.push(1)
s.push(2)

t = Stack()
t.push('a')

print("Plain iterator:")
counter = 0
for x in s:
    for y in s:
        print(x, y)
        counter += 1
assert counter == 4, "There double loop is supposed to find four pairs."
assert not s.is_empty(), "The s stack is not supposed to be empty here."
assert not t.is_empty(), "The t stack is not supposed to be empty here."

counter = 0
for x in s:
    for y in t:
        counter += 1
assert counter == 2, "The loop over s and t is supposed to increment the counter twice."

print("Destructive iterator:")
for x in s.destructive_iterator():
    print(x)

assert s.is_empty(), "The s stack is supposed to be empty here."
assert not t.is_empty(), "The t stack is not supposed to be empty here."



