class Data:
    def __init__(self,value,index,count=0):
        self.value = value
        self.index = index
        self.count = count

def sort(arr):
    if arr is None or len(arr)<2:
        return

    hm = {}

    for i in range(len(arr)):
        hm.setdefault(arr[i],Data(arr[i],i)).count += 1

    values = [*hm.values()]


    k=0

    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k+=1
if __name__ == '__main__':
    arr = [1,4,2,9,9,1,4,2,0,5,4,3,9]
    print('Original:',arr) 
    sort(arr)
    print('Sorted:',arr)                       