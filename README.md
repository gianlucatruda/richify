# Richify: Markdown Live Renderer

A real-time Markdown rendering tool that supports streaming input. 
Built with Rich and designed to run with uv.

For non-streaming use cases, consider using [rich-cli](https://github.com/Textualize/rich-cli/) instead.

Original inspiration: [LLM Issue #12](https://github.com/simonw/llm/issues/12#issuecomment-2558147310)

## Usage

Run the script directly with uv:
```bash
# Show help
./richify.py

# Pipe content
echo "# Hello" | ./richify.py

# Render a file
cat document.md | ./richify.py

# Stream LLM output
llm "Write some markdown with code snippets" | ./richify.py
```

3. The script uses uv's script runner mode and automatically handles dependencies. No separate installation step is needed!

## How It Works

The script automatically:
- Detects if it's receiving piped input
- Shows help text when run without input
- Handles Unicode and encoding errors
- Maintains consistent markdown styling

Richify uses several key components to render Markdown in real-time:

- **Rich**: For beautiful terminal formatting and Markdown rendering
- **Live Display**: Updates the rendered content in real-time as new text arrives
- **Signal Handling**: Gracefully handles Ctrl+C and termination signals
- **Streaming Input**: Processes input character-by-character for smooth updates

The script automatically manages its dependencies through uv using the script header:
- Python ≥ 3.8
- rich ≥ 13.9.4

## Installation

1. First, [install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already:

2. Clone this repository:
```bash
git clone <repository-url>
cd richify
```

3. (Optional) Convert `richify.py` to an executable script:
```bash
mv richify.py richify
chmod +x richify
```

4. (Optional) Move the executable to somewhere in your `PATH`

e.g. on macOS 

```bash
mv richify /usr/local/bin/
```

Now you can invoke it with `richify` from anywhere.

