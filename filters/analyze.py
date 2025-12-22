from collections import Counter

def analyze(tokens):
    total_tokens = len(tokens)
    unique_tokens = len(set(tokens))

    if total_tokens == 0:
        return {
            "total_tokens": 0,
            "unique_tokens": 0,
            "average_token_length": 0,
            "top_tokens": [],
            "length_distribution": {}
        }

    total_length = sum(len(token) for token in tokens)
    average_length = round(total_length / total_tokens, 2)

    counter = Counter(tokens)

    top_tokens = [
        (token, freq)
        for token, freq in counter.most_common()
        if freq > 1
    ]

    length_distribution = {}
    for token in tokens:
        length = len(token)
        length_distribution[length] = length_distribution.get(length, 0) + 1

    return {
        "total_tokens": total_tokens,
        "unique_tokens": unique_tokens,
        "average_token_length": average_length,
        "top_tokens": top_tokens,
        "length_distribution": length_distribution
    }