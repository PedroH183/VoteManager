import sys
from pathlib import Path

# Fixing the Python path for pytest
# This is necessary for pytest to find the modules correctly
ROOT_DIR = Path(__file__).resolve().parents[1] # ROOT DIR = backend
sys.path.append(str(ROOT_DIR))
