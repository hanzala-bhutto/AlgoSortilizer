def quinsertSort(draw_info,draw_list,ascending=True):
    lst = draw_info.lst

    def insertion_sort(lst, low, n):
        for i in range(low + 1, n + 1):
            val = lst[i]
            j = i
            while j>low and lst[j-1]>val:
                lst[j]= lst[j-1]
                j-= 1
                draw_list(draw_info, {j-1: draw_info.GREEN, j: draw_info.RED}, True)
                yield True
            lst[j]= val
            
    
    # Partition function for quicksort
    def partition(lst, low, high):
        pivot = lst[high]
        i = j = low
        for i in range(low, high):
            if lst[i]<pivot:
                lst[i], lst[j]= lst[j], lst[i]
                j+= 1
                draw_list(draw_info, {j: draw_info.GREEN, i: draw_info.RED}, True)
                yield True
        lst[j], lst[high]= lst[high], lst[j]
        draw_list(draw_info, {j: draw_info.GREEN, high: draw_info.RED}, True)
        yield True    
        return j

    def hybrid_quick_sort(lst, low, high,ascending=True):
        while low<high:
    
            # If the size of the array is less
            # than threshold apply insertion sort
            # and stop recursion
            if high-low + 1<10:
                yield from insertion_sort(lst, low, high)
                break
    
            else:
                pivot = yield from partition(lst, low, high)
                # Optimised quicksort which works on
                # the smaller arrays first
    
                # If the left side of the pivot
                # is less than right, sort left part
                # and move to the right part of the array
                if pivot-low<high-pivot:
                    yield from hybrid_quick_sort(lst, low, pivot-1)
                    low = pivot + 1
                else:
                    # If the right side of pivot is less
                    # than left, sort right side and
                    # move to the left side
                    yield from hybrid_quick_sort(lst, pivot + 1, high)
                    high = pivot-1
        
    yield from hybrid_quick_sort(lst, 0, len(lst)-1, ascending)
    return lst