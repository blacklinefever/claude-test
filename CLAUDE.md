# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python utility script that provides an interactive number addition calculator. The project consists of a single Python file with no external dependencies.

## Development Commands

### Environment Setup
With Anaconda installed, create and activate a conda environment:
```bash
conda create -n claude-test python=3.11
conda activate claude-test
```

### Package Installation Priority
1. **conda-forge** (preferred): `conda install -c conda-forge <package-name>`
2. **conda defaults** (fallback): `conda install <package-name>`
3. **pip** (final fallback): `pip install <package-name>`

### System Utilities
Use Homebrew for system-level tools and utilities:
- **Applications**: `brew install --cask <app-name>` (preferred for GUI apps)
- **CLI tools**: `brew install <utility-name>`

### Running the Script
```bash
python add_numbers.py
```

The script runs interactively, prompting users to enter numbers until they press Enter without input.

**First Run**: MotherDuck will open browser for SSO authentication. Subsequent runs use stored token.

## Code Structure

- **add_numbers.py**: Main script containing the interactive number addition functionality
  - Uses only Python standard library
  - Includes input validation and error handling
  - Follows procedural programming pattern with proper main function structure

## Technical Details

- **Python Version**: Requires Python 3.x (managed via Anaconda)
- **Environment**: Uses conda for Python environment management
- **Package Priority**: conda-forge → conda defaults → pip
- **Dependencies**: DuckDB (from conda-forge) and Python standard library
- **Architecture**: Single-file script with main() function entry point
- **Data Storage**: 
  - CSV files (local)
  - MotherDuck cloud database (primary, with local fallback)
- **Cloud Integration**: Automatic SSO authentication with MotherDuck
- **Error Handling**: Validates numeric input with try/except for ValueError

## Development Notes

- No build system or package management required
- No testing framework currently configured
- Code uses clear naming conventions and proper error handling
- Script can be imported as a module in other Python applications