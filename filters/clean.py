import string

STOP_WORDS = {
    "the", "is", "was", "and", "or", "a", "an", "to",
        "of", "in", "on", "for", "with", "as", "by", "at", "from",
        "that", "this", "it", "be", "are", "were", "but", "not",
        "he", "she", "they", "we", "you", "his", "her", "its", "my", "your",
        "their", "our", "all", "any", "some", "no", "so", "if", "then",
        "there", "here", "when", "where", "what", "which", "who", "whom",
        "about", "into", "over", "after", "before", "between", "under", "again", "further",
        "once", "such", "only", "too", "very", "can", "will", "just", "should", "now", "do","does", "did" , 
        "have", "has", "had", "not", "no", "nor", "than", "too", "very", 
        "s", "t", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn",
        "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn", "shan", "shouldn",
          "wasn", "weren", "won", "wouldn"
}

def clean(tokens):
    cleaned = []
    removed = []

    for token in tokens:
        stripped = token.strip(string.punctuation)

        if stripped == "":
            removed.append((token, "punctuation"))
            continue

        if stripped.lower() in STOP_WORDS:
            removed.append((token, "stop-word"))
            continue

        cleaned.append(stripped)

    return cleaned, removed




