def merge_sort(a):
    if len(a) <= 1:
        return a
    middle = len(a) / 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

if __name__ == "__main__":
    print merge_sort([3,1,5,4,2,7])
