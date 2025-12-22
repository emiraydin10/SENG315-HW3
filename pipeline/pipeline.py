from filters.tokenize import tokenize
from filters.clean import clean
from filters.transform import transform
from filters.analyze import analyze

def run_pipeline(text):
    log = []

    tokens = tokenize(text)
    log.append("Tokenize filter executed")

    clean_tokens, removed_clean = clean(tokens)
    log.append("Clean filter executed")

    transformed_tokens, modified_tokens, removed_transform = transform(clean_tokens)
    log.append("Transform filter executed")

    analysis = analyze(transformed_tokens)
    log.append("Analyze filter executed")

    return {
        "pipeline_log": log,

        "tokenize_output": tokens,
        "clean_output": clean_tokens,
        "transform_output": transformed_tokens,

        "removed_clean": removed_clean,
        "modified_transform": modified_tokens,
        "removed_transform": removed_transform,

        "analysis_output": analysis
    }