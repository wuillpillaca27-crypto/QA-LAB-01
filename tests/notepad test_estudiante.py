from src.estudiante import aprobar

def test_aprobado():
    assert aprobar(15) == "Aprobado"

def test_desaprobado():
    assert aprobar(8) == "Desaprobado"