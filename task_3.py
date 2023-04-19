with open('input.txt', 'r') as f_in:
    a = int(f_in.readline().strip())
 
b = a // 10
c = b + 1
result = c * b * 100 + 25
 
with open('output.txt', 'w') as f_out:
    f_out.write(str(result))
