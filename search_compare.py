import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    return found, (end - start)


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end = time.time()
    return found, (end - start)


def binary_search_iterative(a_list,item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, (end - start)
    
    
def binary_search_recursive(a_list,item):
    start = time.time()
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                end = time.time()
                return binary_search_recursive(a_list[:midpoint], item), (end - start)
            else:
                end = time.time()
                return binary_search_recursive(a_list[midpoint + 1:], item), (end - start)
def main():
    the_size = 500
    total_time_seq = 0
    total_time_ord_seq = 0
    total_time_bin_iter = 0
    total_time_bin_rec = 0
    proceed = True
    while proceed:
        for i in range(100):
            mylist = get_me_random_list(the_size)
            # sorting is not needed for sequential search.
            seq_return = sequential_search(mylist, -1)
            # sorting mylist.
            mylist = sorted(mylist)
            ord_seq_ret = ordered_sequential_search(mylist, -1)
            bin_iter_ret = binary_search_iterative(mylist, -1)
            bin_rec_ret = binary_search_recursive(mylist, -1)

            total_time_seq += seq_return[1]
            total_time_ord_seq += ord_seq_ret[1]
            total_time_bin_iter += bin_iter_ret[1]
            total_time_bin_rec += bin_rec_ret[1]
            avg_time_seq = total_time_seq / 100
            avg_time_ord_seq = total_time_ord_seq / 100
            avg_time_bin_iter = total_time_bin_iter / 100
            avg_time_bin_rec = total_time_bin_rec / 100
        if the_size == 500:
            print(f"Sequential Search took {avg_time_seq:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Ordered Sequential Search Iterative took {avg_time_ord_seq:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Binary Search Iterative took {avg_time_bin_iter:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Binary Search Recursive took {avg_time_bin_rec:10.7f} seconds to run, on average for a list of {the_size} elements.")
            the_size = 1000
        elif the_size == 1000:
            print(f"\nSequential Search took {avg_time_seq:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Ordered Sequential Search Iterative took {avg_time_ord_seq:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Binary Search Iterative took {avg_time_bin_iter:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Binary Search Recursive took {avg_time_bin_rec:10.7f} seconds to run, on average for a list of {the_size} elements.")
            the_size = 10000
        else:
            print(f"\nSequential Search took {avg_time_seq:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Ordered Sequential Search Iterative took {avg_time_ord_seq:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Binary Search Iterative took {avg_time_bin_iter:10.7f} seconds to run, on average for a list of {the_size} elements.")
            print(f"Binary Search Recursive took {avg_time_bin_rec:10.7f} seconds to run, on average for a list of {the_size} elements.")
            proceed = False

if __name__ == "__main__":
    """Main entry point"""
    main()