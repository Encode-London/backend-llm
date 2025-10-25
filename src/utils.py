def parse_input(user_input):
    # Function to parse user input and return structured data
    return user_input.strip().split()

def format_output(output_data):
    # Function to format output data for display
    return "\n".join(str(item) for item in output_data)

def validate_input(user_input):
    # Function to validate user input
    if not user_input:
        raise ValueError("Input cannot be empty.")
    return True