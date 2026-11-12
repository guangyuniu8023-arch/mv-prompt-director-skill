#!/usr/bin/env python3
"""Print one uniformly selected MV preset ID."""

import argparse
import secrets

PRESET_IDS = ("P1", "P2", "P3", "P4", "P5", "P6", "P7")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidates",
        nargs="+",
        choices=PRESET_IDS,
        default=list(PRESET_IDS),
        help="Allowed preset IDs; all seven are eligible by default.",
    )
    args = parser.parse_args()
    candidates = list(dict.fromkeys(args.candidates))
    print(secrets.choice(candidates))


if __name__ == "__main__":
    main()
