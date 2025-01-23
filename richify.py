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
import select
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown


def show_help():
    console = Console()
    help_text = """
## Usage:
- Pipe Markdown content into the script:
  `echo "# Hello" | ./richify.py`
- Or use it with a file:
  `cat file.md | ./richify.py`

## Example:
```bash
echo "# Title\\n\\nSome *formatted* text" | ./richify.py
```
"""
    console.print(Markdown(help_text))


def is_pipe_input():
    """Check if the script is receiving piped input."""
    return not sys.stdin.isatty()


def main():
    # Check if input is being piped
    if not is_pipe_input():
        show_help()
        return

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
