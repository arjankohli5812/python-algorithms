#Given a list n, returns the list sorted in ascending order.
def mergeSort(n):
    if len(n) > 1:
        mid = len(n) // 2
        a = mergeSort(n[:mid])
        b = mergeSort(n[mid:])
        return merge(a, b)
    else:
        return n

#Given 2 lists, combines them into a single list in ascending order.
def merge(a, b):
    i = j = 0
    m = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            m.append(a[i])
            i+=1
        else:
            m.append(b[j])
            j+=1
    
    while i < len(a):
        m.append(a[i])
        i+=1
        
    while j < len(b):
        m.append(b[j])
        j+=1
    
    return m
