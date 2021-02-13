def transform(legacy_data):
    return {val.lower(): k for k,v in legacy_data.items() for val in v}
