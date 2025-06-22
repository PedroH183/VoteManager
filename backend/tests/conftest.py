import sys
from pathlib import Path

# Pytest runs from the repository root which does not include the "backend"
# directory on ``sys.path``. Adding it here allows importing ``app`` modules
# without setting ``PYTHONPATH`` manually.
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
