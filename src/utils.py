# Utils for issue #28

def validate_input_28(payload):
    '''
    Validates payload structure for issue #28.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
