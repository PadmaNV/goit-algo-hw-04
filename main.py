import timeit
import random


from InsertionSort import insertion_sort
from MergeSort import merge_sort
from TimSort import tim_sort


if __name__ == '__main__':
    data_small = [random.randint(0, 1_000) for _ in range(100)]
    data_medium = [random.randint(0, 10_000) for _ in range(1_000)]
    data_large = [random.randint(0, 100_000) for _ in range(10_000)]


    ts_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=10)
    ts_merge = timeit.timeit(lambda: merge_sort(data_small), number=10)
    ts_tim = timeit.timeit(lambda: tim_sort(data_small[:]), number=10)

    tm_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=10)
    tm_merge = timeit.timeit(lambda: merge_sort(data_medium), number=10)
    tm_tim = timeit.timeit(lambda: tim_sort(data_medium[:]), number=10)
    
    tl_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=10)
    tl_merge = timeit.timeit(lambda: merge_sort(data_large), number=10)
    tl_tim = timeit.timeit(lambda: tim_sort(data_large[:]), number=10)


    print(f"| {'Algorithm':<14} | {'Small':<14} | {'Medium':<14} | {'Large':<14} |")
    print(f"| {'-'*14} | {'-'*14} | {'-'*14} | {'-'*14} |")
    print(f"| {'Insertion Sort':<14} | {ts_insertion:14.5f} | {tm_insertion:14.5f} | {tl_insertion:14.5f} |")
    print(f"| {'Merge Sort':<14} | {ts_merge:14.5f} | {tm_merge:14.5f} | {tl_merge:14.5f} |")
    print(f"| {'Tim Sort':<14} | {ts_tim:14.5f} | {tm_tim:14.5f} | {tl_tim:14.5f} |")
    print(f"  {'-'*14}   {'-'*14}   {'-'*14}   {'-'*14}  ")
