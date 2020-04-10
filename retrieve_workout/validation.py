def query_values_validation(value):
    validate_type(value)

def validate_type(value):
    if len(value) == 0:
        raise ValueError('ValidationFailure')
    if not isinstance(value, str):
        raise ValueError('ValidationFailure')
    if not value.isalpha():
        raise ValueError('ValidationFailure')