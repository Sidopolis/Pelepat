# Utils for issue #50

def validate_input_50(payload):
    '''
    Validates payload structure for issue #50.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
