def miniMaxSum(arr):
    total = sum(arr)
    min_val = total - max(arr)
    max_val = total - min(arr)
    print(f"{min_val} {max_val}")
