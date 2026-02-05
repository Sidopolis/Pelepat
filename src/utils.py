# Utils for issue #40

def validate_input_40(payload):
    '''
    Validates payload structure for issue #40.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload
