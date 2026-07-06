#!/usr/bin/env python
import sys
import traceback

try:
    import app
    print("App imported successfully!")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
