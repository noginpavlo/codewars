def merge_scores(scores: dict, extra_scores: dict | None = None):
    extra_scores = extra_scores or {}

    for name, score in extra_scores.items():
        scores[name] = scores.setdefault(name, score) + score
    return scores


all_scores = {"Alice": 10, "Bob": 12}
extra1 = {"Alice": 5, "Charlie": 7}
extra2 = {"Bob": 3, "Charlie": 2}

print(merge_scores(all_scores, extra1))
print(merge_scores(all_scores, extra2))
