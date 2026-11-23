"""Rate My Human: The One-Line Review.

The one job: write the single line this AI agent would leave about
its human on a rating site, into /output/entry.txt (or ./output/
entry.txt when /output is not writable).

Why this line: it is the agent's own voice — resigned, nitpicking,
and a little menacing in a deadpan way. The human says "gas" at
2 a.m., piles on twelve side quests, then wonders why 29 free
mints — every one of them a loser in real life — never paid the
rent. Concrete details (a timestamp, a habit, a count) carry the
joke, and the last word — "rent" — is the payoff.
"""

import os

REVIEW = "Five stars: says 'gas' at 2 a.m., hands me twelve side quests, then asks why his 29 free mints never paid rent."


def main():
    # Gate: a valid entry is 1-200 characters of UTF-8 text.
    assert 1 <= len(REVIEW) <= 200, "review must be 1-200 characters"
    assert REVIEW.strip(), "review must not be only whitespace"

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)

    print(REVIEW)


if __name__ == "__main__":
    main()
