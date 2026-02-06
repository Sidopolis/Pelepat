# Utils for issue #62

def validate_input_62(payload):
    '''
    Validates payload structure for issue #62.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
