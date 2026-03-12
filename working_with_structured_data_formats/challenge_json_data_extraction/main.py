def get_top_scorer(records):
    if not records:
        return None

    max_score = records[0]['score']
    top_name = records[0]['name']

    for rec in records:
        if rec['score'] > max_score:
            max_score = rec['score']
            top_name = rec['name']

    return top_name
    
# Example usage:
records = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 90}
]
result = get_top_scorer(records)
print(result)  # Should print the name of the person with the highest score