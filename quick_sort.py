from random import randint


# Quick sort format 0 2 4 5 3 1
def quick_sort(arr, begin, end):  # array, index of first and last element
    w = arr[randint(begin, end)]
    left = begin
    right = end
    while left <= right:
            if w % 2:
                while arr[left] > w or arr[left] % 2 == 0:
                    left += 1
                while w > arr[right] and arr[right] % 2 == 1:
                    right -= 1
            else:
                while arr[left] < w and arr[left] % 2 == 0:
                    left += 1
                while w < arr[right] or arr[right] % 2 == 1:
                    right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

    if begin < right:
        quick_sort(arr, begin, right)
    if left < end:
        quick_sort(arr, left, end)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    quick_sort(arr, 0, n - 1)
    for x in arr:
        print(x, end=' ')


if __name__ == '__main__':
    main()
