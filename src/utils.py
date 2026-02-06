# Utils for issue #14

def validate_input_14(payload):
    '''
    Validates payload structure for issue #14.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
