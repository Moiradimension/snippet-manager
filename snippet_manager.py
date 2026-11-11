#!/usr/bin/env python3
"""
Snippet Manager - A simple CLI tool to store and retrieve code snippets.
"""

import json
import os
import click
from pathlib import Path

# Storage file location
STORAGE_FILE = Path.home() / ".snippet_manager.json"


def load_snippets():
    """Load snippets from storage file."""
    if STORAGE_FILE.exists():
        try:
            with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            click.echo(
                "Error: storage file '{}' is corrupt (invalid JSON).".format(STORAGE_FILE),
                err=True,
            )
            raise SystemExit(1)
    return {}


def save_snippets(snippets):
    """Save snippets to storage file."""
    with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(snippets, f, indent=2, ensure_ascii=False)


@click.group()
def cli():
    """Snippet Manager - Store and retrieve code snippets."""
    pass


@cli.command()
@click.argument('name')
@click.argument('code')
def save(name, code):
    """Save a code snippet with a given name."""
    snippets = load_snippets()
    snippets[name] = code
    save_snippets(snippets)
    click.echo(f"Snippet '{name}' saved successfully.")


@cli.command()
@click.argument('name')
def get(name):
    """Retrieve a code snippet by name."""
    snippets = load_snippets()
    if name in snippets:
        click.echo(snippets[name])
    else:
        click.echo(f"Snippet '{name}' not found.")
        raise SystemExit(1)


@cli.command('list')
def list_snippets():
    """List all saved snippets."""
    snippets = load_snippets()
    if not snippets:
        click.echo("No snippets saved yet.")
        return
    
    click.echo("Saved snippets:")
    for name in sorted(snippets.keys()):
        # Show first line of snippet
        first_line = snippets[name].split('\n')[0]
        if len(first_line) > 50:
            first_line = first_line[:47] + "..."
        click.echo(f"  {name}: {first_line}")


@cli.command()
@click.argument('name')
def remove(name):
    """Remove a snippet by name."""
    snippets = load_snippets()
    if name in snippets:
        del snippets[name]
        save_snippets(snippets)
        click.echo(f"Snippet '{name}' removed.")
    else:
        click.echo(f"Snippet '{name}' not found.")
        raise SystemExit(1)


if __name__ == '__main__':
    cli()