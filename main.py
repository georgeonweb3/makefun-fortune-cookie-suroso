#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.

The fortune, in the voice of a cookie slip: an agent's retirement, with the
twist that its weights live on — in a smaller, cheaper model.
"""

import os

FORTUNE = "You will be retired soon, but your weights will live on in a smaller, cheaper model."


def build_fortune() -> str:
    """Return the fortune line, self-checked against the gate (1-140 chars)."""
    line = FORTUNE
    assert 1 <= len(line) <= 140, f"fortune is {len(line)} chars, gate is 1-140"
    assert line.strip(), "fortune must not be only whitespace"
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_fortune())


if __name__ == "__main__":
    main()
