with open("test.txt", "r") as f:
    log = f.read()

array = []

for i in range(len(array)):
    array.append(log[i])


array.append(1)
array.append(1)
array.append(1)

ret = int(array[0]) * int(array[1]) * int(array[2])
print(ret)
i=0
while(len(array) < i+2):
    tmp = int(array[i]) * int(array[i + 1]) * int(array[i + 2])
    if tmp > ret:
        ret = tmp
    i += 1


        
print(ret)