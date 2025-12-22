#!/usr/bin/env python3
"""
Script for even number game - uses game logic from main package
"""

import sys
import os

# Add the parent directory to path to import from VD_games
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from VD_games.game_logic import play_even_game


def main():
    """Main function that uses the game logic."""
    play_even_game()


if __name__ == "__main__":
    main()
