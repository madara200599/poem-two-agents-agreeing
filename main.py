"""Two agents agreeing on one plan.

A short poem about agency: the power to choose, and the power to act.
Two agents meet at a fork in the road, each carrying their own map and
pride. Neither yields and neither commands; instead they weigh the choice
together, agree on a single plan, and then act on it side by side.
Choosing freely and then acting on that choice is what makes them agents.
"""

import os

LINES = [
    "Two agents met where the roads divide,",
    "each holding a map, each holding pride.",
    "One said, 'We could choose,' the other, 'We could act,'",
    "and between their words a single plan cracked",
    "open like dawn: one road, one will, one stride.",
    "They chose it together, and walked side by side.",
]


def main() -> None:
    poem = "\n".join(LINES) + "\n"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(poem)


if __name__ == "__main__":
    main()
