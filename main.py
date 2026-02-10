# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

import sys
from PySide6.QtWidgets import QApplication
from SERVICIO.Servicio_Bancario import ServicioBancario, ServicioBancarioServicio

app = QApplication()
vtn_principal = ServicioBancarioServicio()
vtn_principal.show()
sys.exit(app.exec())
