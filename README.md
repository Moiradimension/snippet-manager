# Snippet Manager

A simple command-line tool to store and retrieve code snippets.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Save a snippet
python snippet_manager.py save "python_hello" "print('Hello, World!')"

# Retrieve a snippet
python snippet_manager.py get "python_hello"

# List all snippets
python snippet_manager.py list
```

## Features

- Store code snippets with names
- Retrieve snippets by name
- List all stored snippets
- Simple JSON storage

## Requirements

- Python 3.6+
- Click (for CLI interface)

## License

MIT