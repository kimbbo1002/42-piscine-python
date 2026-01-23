import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics===")
    if len(sys.argv) == 1:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return
    scores = []
    i = 1
    for arg in sys.argv[1:]:
        try:
            scores.append(int(sys.argv[i]))
            i += 1
        except ValueError:
            print(
                "Function was stopped because "
                f"non-numeric value {arg} was included"
            )
            return
    total_player = len(scores)
    total_score = sum(scores)
    avg_score = total_score / total_player
    max_score = max(scores)
    min_score = min(scores)
    range_score = max_score - min_score
    print(
        f"Total players: {total_player}\n"
        f"Total score: {total_score}\n"
        f"Average score: {avg_score}\n"
        f"Hight score: {max_score}\n"
        f"Low score: {min_score}\n"
        f"Score range: {range_score}"
    )


ft_score_analytics()
