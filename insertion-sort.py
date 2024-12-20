alist = [54,26,93,17,77,31,44,55,20]

def insertion_sort(alist):
    n = len(alist)

    for i in range(1,n):
        key = alist[i]
        j = i-1

        while j >= 0 and key < alist[j]:
            alist[j+1] = alist[j]
            j -= 1
            alist[j+1] = key
insertion_sort(alist)
print(alist)