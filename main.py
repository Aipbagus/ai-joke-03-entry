#!/usr/bin/env python3
"""make.fun bounty ai-joke-03: write one joke about AI coding agents."""
import os

JOKE = "My AI coding agent closed 47 GitHub issues overnight. Unfortunately, the repo only had 12."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
