x=8
y=0
a='Hello!'
b=""

if x and b:
    print("Both x and b are true") # won't execute
if not(y) or not(a):
    print("Either y or a is false") # will execute
if x or y == False:
    print("either x or y is false") # will execute
    if x > y:
        print("x is greater than y") # will execute