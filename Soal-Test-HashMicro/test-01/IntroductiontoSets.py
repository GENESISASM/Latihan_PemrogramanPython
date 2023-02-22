def average(array):
    #your code goes here
    sumArray = sum(set(array))
    lenArray = len(set(array))
    hasil = sumArray/lenArray
    return hasil;

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)