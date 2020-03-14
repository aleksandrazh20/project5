# Вариант 1, бинарный поиск

import time
# Бинарный поиск рекурсией
def binary_search_rec(a,n):
    if len(a) == 0:
        return None
    else:
        mid = len(a) // 2
    if a[mid] == n:
        return mid
    else:
        if n < a[mid]:
            return binary_search_rec(a[:mid],n)
        else:
            return binary_search_rec(a[mid + 1:],n)

# Бинарный поиск итеративно
def binary_search_it(a,n):
    mid = len(a) // 2
    first = 0
    last = len(a) - 1

    while a[mid] != n and first <= last:
        if n > a[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2

    if first > last:
        return None
    else:
        return mid


a = list(map(int, input().split()))
n = int(input())
type = input('Recursion, iteration: ').lower()
# Выбор функции(рекурсия, итерация)
if type == 'recursion':
    print(binary_search_rec(a,n))
    start = time.time()
    print('Time: ' + str(time.time()-start) + 'sec')
else:
    print(binary_search_it(a,n))
    start = time.time()
    print('Time: ' + str(time.time() - start) + 'sec')