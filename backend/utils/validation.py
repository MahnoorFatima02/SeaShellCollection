from utils.custom_exceptions import ValidationException

def validate_shell_data(data):
    required_fields = ['name', 'species', 'description']
    
    for field in required_fields:
        if field not in data or not data[field]:
            raise ValidationException(f"{field} is required")
    
    return None