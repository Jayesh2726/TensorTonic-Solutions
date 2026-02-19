import math
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    min_val = min(values)
    max_val = max(values)

    if max_val == min_val:
        return [0] * len(values)
    width = (max_val - min_val)/ num_bins
    results = []

    for x in values:
        bin_index = math.floor((x - min_val) /width)
        bin_index = min(bin_index, num_bins - 1)
        results.append(bin_index)
    return results        
        