# Utils for issue #70

def validate_input_70(payload):
    '''
    Validates payload structure for issue #70.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
