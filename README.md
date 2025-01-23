# Richify: Markdown Live Renderer

Real-time Markdown rendering tool that formats text as you type or pipe it in.

## Usage:
- Pipe Markdown content into the script:
  `echo "# Hello" | ./richify.py`
- Or use it with a file:
  `cat file.md | ./richify.py`
- Press Ctrl+C to exit

## Examples:

Render a markdown file
```bash
cat document.md | ./richify.py
```

Stream the output of an [LLM](https://github.com/simonw/llm) query with markdown formatting
```bash
llm "Write some markdown with code snippets" | ./richify.py
```
(This was the original use case. If you don't care about streaming, you probably just want to use [rich-cli](https://github.com/Textualize/rich-cli/) instead.)

Original inspiration:

[https://github.com/simonw/llm/issues/12#issuecomment-2558147310](https://github.com/simonw/llm/issues/12#issuecomment-2558147310)
