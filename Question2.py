def alternate_pos_neg(arr):
    positives = [num for num in arr if num >= 0]
    negatives = [num for num in arr if num < 0]
    
    result = []
    pos_index, neg_index = 0, 0
    
    while pos_index < len(positives) and neg_index < len(negatives):
        result.append(positives[pos_index])
        result.append(negatives[neg_index])
        pos_index += 1
        neg_index += 1
    
    while pos_index < len(positives):
        result.append(positives[pos_index])
        pos_index += 1
    
    # Append the remaining elements from the negative list, if any
    while neg_index < len(negatives):
        result.append(negatives[neg_index])
        neg_index += 1
    
    return result

input_array = [-3, 1, 2, 4, -6, 8, -8, -11]
result = alternate_pos_neg(input_array)
print(result)

#time complexity is O(n) where n is size of array 'arr'
