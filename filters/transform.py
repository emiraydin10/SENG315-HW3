def transform(tokens):
    transformed = []
    modified = []
    removed = []

    for token in tokens:
        
        new_token = token.lower()

        if len(new_token) < 3:
            removed.append((token, "length < 3"))
            continue

        if new_token != token:
            modified.append((token, new_token))

        transformed.append(new_token)

    return transformed, modified, removed