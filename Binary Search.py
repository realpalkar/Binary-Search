pos = -1

list = [2,4,8,9,41,56]
n = 56

def search(list,n):
    l = 0
    u = len(list)-1

    while l<=u:
        mid = (l+u) // 2
        globals()['pos'] = mid

        if list[mid] == n:
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid -1

if search(list,n):
    print('found at',pos)
else:
    print('not found')


