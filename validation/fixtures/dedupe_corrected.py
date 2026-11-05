def dedupe(values):
    result = []
    for value in values:
        if not any(value == retained for retained in result):
            result.append(value)
    return result
