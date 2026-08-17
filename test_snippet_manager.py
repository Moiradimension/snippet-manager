#!/usr/bin/env python3
"""
Simple tests for snippet_manager.py
"""

import os
import tempfile
import json
from pathlib import Path

# Mock the storage file for testing
TEST_STORAGE = Path(tempfile.mkdtemp()) / "test_snippets.json"


def test_save_and_get():
    """Test saving and retrieving a snippet."""
    # This is a simplified test - in real usage, you'd use pytest or unittest
    print("Testing save and get functionality...")
    
    # Mock the storage file
    import snippet_manager
    original_storage = snippet_manager.STORAGE_FILE
    snippet_manager.STORAGE_FILE = TEST_STORAGE
    
    try:
        # Test save
        snippet_manager.save_snippets({"test": "print('hello')"})
        
        # Test load
        snippets = snippet_manager.load_snippets()
        assert snippets == {"test": "print('hello')"}, f"Expected {{'test': \"print('hello')\"}}, got {snippets}"
        
        print("[OK] Save and get test passed")
        
    finally:
        # Cleanup
        snippet_manager.STORAGE_FILE = original_storage
        if TEST_STORAGE.exists():
            TEST_STORAGE.unlink()


def test_list_command():
    """Test listing snippets."""
    print("Testing list functionality...")
    
    # Mock the storage file
    import snippet_manager
    original_storage = snippet_manager.STORAGE_FILE
    snippet_manager.STORAGE_FILE = TEST_STORAGE
    
    try:
        # Create test data
        test_data = {
            "python_hello": "print('Hello, World!')",
            "javascript_hello": "console.log('Hello!')",
            "ruby_hello": "puts 'Hello'"
        }
        snippet_manager.save_snippets(test_data)
        
        # Test load
        snippets = snippet_manager.load_snippets()
        assert len(snippets) == 3, f"Expected 3 snippets, got {len(snippets)}"
        
        print("[OK] List test passed")
        
    finally:
        # Cleanup
        snippet_manager.STORAGE_FILE = original_storage
        if TEST_STORAGE.exists():
            TEST_STORAGE.unlink()


if __name__ == "__main__":
    print("Running snippet manager tests...")
    test_save_and_get()
    test_list_command()
    print("\nAll tests passed!")