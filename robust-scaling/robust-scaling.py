def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    if len(values) == 0:
        return []

    if len(values) == 1:
        return [0]  # single value scaled = 0

    values_sorted = sorted(values)
    n = len(values_sorted)

    # Median
    if n % 2 == 1:
        median = values_sorted[n // 2]
        lower_half = values_sorted[:n // 2]
        upper_half = values_sorted[n // 2 + 1:]
    else:
        median = (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2
        lower_half = values_sorted[:n // 2]
        upper_half = values_sorted[n // 2:]

    # Function to calculate median safely
    def calc_median(arr):
        m = len(arr)
        if m == 0:
            return 0
        if m % 2 == 1:
            return arr[m // 2]
        else:
            return (arr[m // 2 - 1] + arr[m // 2]) / 2

    q1 = calc_median(lower_half)
    q3 = calc_median(upper_half)

    iqr = q3 - q1

    if iqr == 0:
        return [x - median for x in values]

    return [(x - median) / iqr for x in values]