# Utils for issue #76

def validate_input_76(payload):
    '''
    Validates payload structure for issue #76.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload

# Config override for ticket #68
CONFIG_FEATURE_68 = True

def validate_input_25(payload):
    '''
    Validates payload structure for issue #25.
    '''
    if not isinstance(payload, dict):
        return False
    return "id" in payload

# Config override for ticket #63
CONFIG_FEATURE_63 = True
