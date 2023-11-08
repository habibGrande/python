#1
def biggie_size (arr):
    for x in range(0,len(arr), 1):
        if arr[x] > 0:
            arr[x]="big"
    return arr        
        
print(biggie_size([-1, 3, 5, -5]))

#2
def count_positives(arr):
    count = 0
    for x in range(1,len(arr),1):
        if arr[x] > 0:
            count = count+1
            arr[len(arr)-1] = count
    return arr
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#3
def sum_total(arr):
    sum=0
    for x in range(0,len(arr),1):
        sum += arr[x]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

#4
def average(arr):
    avarageNum=0
    for x in range (0,len(arr),1):
        avarageNum += arr[x]
    avarageNum = avarageNum / len(arr)
    return avarageNum
print(average([1,2,3,4]))

#5
def length(arr):
    arrLength = len(arr)
    return arrLength
print( length([37,2,1,-9]) )

#6
def minimum (arr):
    if len(arr) == 0: 
        return False
    else:
         minimumNum = min(arr)
    return(minimumNum)
print( minimum([37,2,1,-9]))

#7 
def maximum (arr):
    if len(arr) == 0: 
        return False
    else:
        maximumNum = max(arr)
    return(maximumNum)
print(maximum([37,2,1,-9]))


#8
def ultimate_analysis(arr):
    dictionary={"sumTotal":sum_total(arr),"average" :average(arr), "minimum" : minimum (arr), "maximum":maximum (arr), "length":length(arr)}
    return(dictionary)

print(ultimate_analysis([37,2,1,-9]))

#9
def reverse_list(list):
    arr=[]
    for x in range(len(list)-1,-1,-1):
        arr.append(list[x])
    return arr
     
print(reverse_list([37,2,1,-9]))