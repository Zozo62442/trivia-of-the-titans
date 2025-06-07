def validate_answer(user_input, options):
    """
    Validate user input.
    """
    valid_inputs = ['A', 'B', 'C', 'D']
    return user_input in valid_inputs and len(options) == 4