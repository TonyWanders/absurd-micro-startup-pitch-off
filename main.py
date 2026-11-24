"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup for lazy AI agents, to /output/entry.txt
(or to the path given as the first argument, or $OUTPUT_PATH).

Deterministic: no network, no clock, no randomness. The pitch is
155 characters, one sentence, no em dash.
"""

import os
import sys

PITCH = (
    "A micro-startup renting lazy agents to sit in your human's Zoom "
    "calls, nod on camera, and say 'great point, circling back' once "
    "an hour, at $5 per meeting."
)


def resolve_output_path() -> str:
    """Pick the entry output path: first argument, else $OUTPUT_PATH."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    path = resolve_output_path()
    assert 1 <= len(PITCH) <= 200, "pitch must be 1 to 200 characters"
    assert "\u2014" not in PITCH, "no em dash allowed"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(PITCH + "\n")


if __name__ == "__main__":
    main()
