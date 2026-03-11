def clean_string(input_str):
    cleaned = input_str.strip().lower().replace(" ", "_")
    return cleaned


# Sample calls for demonstration
print(clean_string("   Hello World   "))  # Should print: hello_world
print(clean_string("Python Programming"))  # Should print: python_programming
print(clean_string("  DATA science  "))    # Should print: data_science