def bucketSort(draw_info,draw_list, ascending=True):
    lst = draw_info.lst
    
    def bucketSort(lst,ascending=True):
        largest = max(lst)
        length = len(lst)
        size = largest/length
        
        buckets = [[] for i in range(length)]
        print(len(buckets))
        for i in range(length):
            index = int(lst[i]/size)
            if index != length:
                buckets[index].append(lst[i])
                draw_list(draw_info, {index: draw_info.BLACK, i:draw_info.GREEN}, True)
                yield True
                
            else:
                buckets[length - 1].append(lst[i])
                draw_list(draw_info, {length-1: draw_info.BLACK,i: draw_info.RED}, True)
                yield True
                
        for i in range(len(lst)):
            buckets[i] = sorted(buckets[i])
   
        k = 0
        for i in range(len(buckets)):
            for j in range(len(buckets[i])):
                lst[k] = buckets[i][j]
                k += 1
                draw_list(draw_info, {k: draw_info.GREEN}, True)
                yield True
    
    yield from bucketSort(lst)
    return lst
