with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
 
if n >= 1:
    total = (n * (n + 1)) // 2
else:
    total = (-n * (-n + 1)) // 2
    total = -total + 1
 
with open('output.txt', 'w') as f:
    f.write(str(total))
