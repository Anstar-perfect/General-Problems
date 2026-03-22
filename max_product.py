length = int(input("Enter the number of values:"))
arr = []
for i in range(length):
    values = int(input("Enter your positive value:"))
    arr.append(values)

product = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            pass
        else:
            product.append(arr[i]*arr[j])

max_pro = max(product)
print('The max product possible:',max(product))
print('The values that can make the max product are',max(arr),int(max_pro/max(arr)))
