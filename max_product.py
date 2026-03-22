arr = [12,19,28,13,34]
product = []

for i in range(len(arr)):
    for j in range(len(arr)):
        
        product.append(arr[i]*arr[j])

print(product)