import sys
from pathlib import Path

# Corrigindo o path para encontrar o executável do Python
# Isso é necessário para que o pytest encontre os módulos corretamente !!
ROOT_DIR = Path(__file__).resolve().parents[1] # ROOT DIR = backend
sys.path.append(str(ROOT_DIR))
