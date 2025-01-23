#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "rich>=13.9.4",
# ]
# ///

"""
https://github.com/simonw/llm/issues/12#issuecomment-2558147310
"""

import sys
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown


def main():
    console = Console()
    md = ""
    with Live(Markdown(""), console=console, refresh_per_second=10) as live:
        while True:
            chunk = sys.stdin.read(1)
            if not chunk:
                break
            md += chunk
            live.update(Markdown(md))


if __name__ == "__main__":
    main()
