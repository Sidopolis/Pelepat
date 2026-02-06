# Utils for issue #57

def validate_input_57(payload):
    '''
    Validates payload structure for issue #57.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
