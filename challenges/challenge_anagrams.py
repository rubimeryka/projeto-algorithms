def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def sort(word):
    list_word = list(word.lower())
    sorted_list = merge_sort(list_word)
    return "".join(sorted_list)


def is_anagram(first_string, second_string):

    sorted_first = sort(first_string)
    sorted_second = sort(second_string)

    if sorted_first == "" and sorted_second == "":
        return sorted_first, sorted_second, False

    return sorted_first, sorted_second, sorted_first == sorted_second
