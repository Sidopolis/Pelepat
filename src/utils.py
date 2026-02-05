# Utils for issue #8

def validate_input_8(payload):
    '''
    Validates payload structure for issue #8.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
