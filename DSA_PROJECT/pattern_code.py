def is_possible(arr, students, max_pages):
    count = 1
    pages = 0
    
    for num in arr:
        if pages + num > max_pages:
            count += 1
            pages = num
        else:
            pages += num
            
    return count <= students


def allocate_books(arr, students):
    low = max(arr)
    high = sum(arr)
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_possible(arr, students, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans