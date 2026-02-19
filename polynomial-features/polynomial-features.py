def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    result = []
    for x in values:
        row = []
        for i in range (degree+1):
            row.append(x ** i)
        result.append(row)
    return result
        