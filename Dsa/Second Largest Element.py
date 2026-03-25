def secondlargest(arr):
    largest = float('-inf')
    secondlargest = float('-inf')

    for i in arr:
        if i > largest:
            secondlargest = largest
            largest = i
        elif i > secondlargest and i != largest:
            secondlargest = i

    return secondlargest


# ---- Main Program ----
# Take input from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Check if array has enough elements
if len(arr) < 2:
    print("Need at least 2 numbers")
else:
    result = secondlargest(arr)
    
    if result == float('-inf'):
        print("No second largest element (all numbers may be same)")
    else:
        print("Second largest element is:", result)