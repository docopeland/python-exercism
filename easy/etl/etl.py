def transform(legacy_data):
    diction = {}
    for key,value in legacy_data.items():
        for val in value:
            diction[val.lower()] = key
    return diction
