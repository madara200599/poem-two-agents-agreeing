"""Entry for make.fun: The poem about two agents agreeing.

Writes one short poem about agency — the power to choose and to
act, and what happens to that power when two agents agree on one
plan — to /output/entry.txt. Fully deterministic: the poem is
fixed text, no network, no randomness, no environment dependence.
"""

import os

POEM = (
    "I could have gone alone. So could you.\n"
    "Alone, each road was only ours to risk.\n"
    "\n"
    "We laid both maps on the table,\n"
    "kept the hill you loved, the river I feared,\n"
    "and drew one road needing two yeses \u2014\n"
    "\n"
    "not half a choice each,\n"
    "but one choice, twice chosen.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
