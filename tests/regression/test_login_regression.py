# Ese archivo solo registra escenarios (BDD PURO), los datos se encuentran en los feature

#from pathlib import Path                               # Reemplazo de ruta por paths relativos. Fumciona en todos los OS
from pytest_bdd import scenarios



scenarios("../../bdd/features/login.feature")

#FEATURES_DIR = Path(__file__).resolve().parents[2] / "bdd" / "features"
#scenarios(FEATURES_DIR / "login.feature")