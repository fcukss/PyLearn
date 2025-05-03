def between_extremes(numbers):
    if not numbers or len(numbers)==1:
        return 0
    return max(numbers)-min(numbers)
