def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 2]
    print(numbers, '\n',  insertion_sort(numbers))     





