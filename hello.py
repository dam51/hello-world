#!/usr/bin/env python3
"""
A flexible "Hello, world!" script with CLI options.

Usage examples:
  python3 hello.py
  python3 hello.py Alice
  python3 hello.py Alice -g Hi -c 2 -s upper -p !!!
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class GreetingConfig:
    greeting: str = "Hello"
    name: str = "world"
    count: int = 1
    punctuation: str = "!"
    style: str = "plain"  # one of: plain, upper, lower, title


def format_message(cfg: GreetingConfig) -> str:
    base = f"{cfg.greeting}, {cfg.name}{cfg.punctuation}"
    if cfg.style == "upper":
        return base.upper()
    if cfg.style == "lower":
        return base.lower()
    if cfg.style == "title":
        return base.title()
    return base


def run(cfg: GreetingConfig) -> None:
    times = max(1, cfg.count)
    for _ in range(times):
        print(format_message(cfg))


def parse_args(argv: list[str] | None = None) -> GreetingConfig:
    parser = argparse.ArgumentParser(description="Print a customizable greeting.")
    parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="Name to greet (default: world)",
    )
    parser.add_argument(
        "-g",
        "--greeting",
        default="Hello",
        help='Greeting word (default: "Hello")',
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of times to print the greeting (default: 1)",
    )
    parser.add_argument(
        "-p",
        "--punctuation",
        default="!",
        help='Trailing punctuation (default: "!")',
    )
    parser.add_argument(
        "-s",
        "--style",
        choices=["plain", "upper", "lower", "title"],
        default="plain",
        help="Text style transformation to apply",
    )
    args = parser.parse_args(argv)

    # Normalize count to be at least 1
    count = args.count if args.count and args.count > 0 else 1

    return GreetingConfig(
        greeting=args.greeting,
        name=args.name,
        count=count,
        punctuation=args.punctuation,
        style=args.style,
    )


def main(argv: list[str] | None = None) -> None:
    cfg = parse_args(argv)
    run(cfg)


if __name__ == "__main__":
    main()
