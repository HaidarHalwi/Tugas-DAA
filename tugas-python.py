import random
import time

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Generate random array for testing
def generate_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Measure time for sorting
def measure_sorting_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Main function to test both sorting algorithms
def main():
    sizes = [0, 10, 20, 40, 60, 80, 100]
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }

    for size in sizes:
        arr = generate_array(size)
        print(f"\nTesting for {size} elements:")
        for name, algorithm in algorithms.items():
            arr_copy = arr.copy()
            execution_time = measure_sorting_time(algorithm, arr_copy)
            print(f"{name} executed in {execution_time} seconds.")

if __name__ == "__main__":
    main()
