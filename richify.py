#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "rich>=13.9.4",
# ]
# ///

"""
Real-time Markdown renderer using Rich.

This script renders Markdown content in real-time as it's being piped in,
providing immediate visual feedback of the formatted text.

Original inspiration:
https://github.com/simonw/llm/issues/12#issuecomment-2558147310
"""

import sys
import signal
from typing import Optional
from rich.console import Console, ConsoleOptions, RenderResult
from rich.live import Live
from rich.markdown import Markdown, Heading
from rich import print as rprint
from rich.style import Style
from rich.text import Text

# Global configuration
MARKDOWN_STYLE = {
    "code_theme": "ansi_dark",
    "justify": "left",
}


class FancyHeading(Heading):
    """A heading class that uses colors instead of centering for headings"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        text = self.text
        if self.tag == 1:
            # Create new Text object with just the content
            styled_text = Text(
                str(self.text),
                style=Style(color="light_goldenrod1", bgcolor="slate_blue3"),
            )
            yield Text("")
            yield styled_text
        else:
            # apply default text styles, see default_styles.py in rich
            text.justify = "left"
            text.style = Style(color="blue")
            yield Text("")
            yield text


Markdown.elements["heading"] = FancyHeading


class MarkdownRenderer:
    def __init__(self):
        self.console = Console(highlight=True)
        self.md_content = "\n"
        self.live: Optional[Live] = None

    def create_markdown(self, content: str) -> Markdown:
        """Create a Markdown object with consistent styling."""
        _md = Markdown(content, **MARKDOWN_STYLE)
        _md.elements["heading"] = FancyHeading
        _md.elements["heading_open"] = FancyHeading
        # print(_md.elements)
        return _md

    def render_help(self) -> None:
        """Display usage instructions and examples."""
        help_text = """
## Richify: Markdown Live Renderer

Real-time Markdown rendering tool that formats text as you type or pipe it in.

### Usage:
- Pipe Markdown content into the script:
  `echo "# Hello" | ./richify.py`
- Or use it with a file:
  `cat file.md | ./richify.py`
- Press Ctrl+C to exit

### Examples:

Render a markdown file
```bash
cat document.md | ./richify.py
```

Stream the output of an LLM query with markdown formatting
```bash
llm "Write some markdown with code snippets" | ./richify.py
```
"""
        self.console.print(self.create_markdown(help_text))

    @staticmethod
    def is_pipe_input() -> bool:
        """Check if the script is receiving piped input."""
        return not sys.stdin.isatty()

    def handle_signal(self, signum: int, frame) -> None:
        """Handle interrupt signals gracefully."""
        if self.live:
            self.live.stop()
        rprint("\n[yellow]Rendering stopped by user[/yellow]")
        sys.exit(0)

    def render_stream(self) -> None:
        """Render markdown content from stdin in real-time."""
        try:
            with Live(
                self.create_markdown(""), console=self.console, refresh_per_second=10
            ) as live:
                self.live = live
                while True:
                    chunk = sys.stdin.read(20)
                    if not chunk:
                        break
                    self.md_content += chunk
                    live.update(self.create_markdown(self.md_content))
        except UnicodeDecodeError as e:
            rprint(f"[red]Error: Invalid character encoding - {str(e)}[/red]")
        except Exception as e:
            rprint(f"[red]Unexpected error: {str(e)}[/red]")

    def run(self) -> None:
        """Main execution method."""
        # Set up signal handlers
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)

        if not self.is_pipe_input():
            self.render_help()
            return

        self.render_stream()


def main() -> None:
    """Entry point of the script."""
    renderer = MarkdownRenderer()
    renderer.run()


if __name__ == "__main__":
    main()
