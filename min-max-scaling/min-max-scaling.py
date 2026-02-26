def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """

    rows = len(data)
    cols = len(data[0])

    scaled_data = [[0 for _ in range(cols)] for _ in range(rows)]

    for col in range(cols):

        column_values = []
        for row in range(rows):
            column_values.append(data[row][col])

        min_val = min(column_values)
        max_val = max(column_values)

        for row in range(rows):
            if max_val - min_val == 0:
                scaled_data[row][col] = 0
            else:
                scaled_data[row][col] = (
                    (data[row][col] - min_val) / (max_val - min_val)
                )

    return scaled_data