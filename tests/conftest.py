import sys
from pathlib import Path

# Add the root directory to sys.path so tests can import app
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
