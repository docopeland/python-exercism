def slices(series, length):
    if len(series) < length or length < 1:
        raise ValueError("length value out of range")
    else:
        return [series[i:i+length] for i in range(len(series)-length+1)]