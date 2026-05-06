"""
Pruebas automáticas para el módulo de control de temperatura.
"""

import pytest
from temperature import is_overheating


def test_high_temperature():
    """Prueba que detecta temperaturas altas (alarma)."""
    assert is_overheating(90) is True


def test_normal_temperature():
    """Prueba que valida temperaturas normales."""
    assert is_overheating(60) is False


def test_threshold_temperature():
    """Prueba el límite exacto de 80°C."""
    assert is_overheating(80) is False
    assert is_overheating(80.1) is True


def test_invalid_temperature():
    """Prueba que rechaza temperaturas negativas."""
    with pytest.raises(ValueError):
        is_overheating(-5)


def test_zero_temperature():
    """Prueba temperatura de 0°C (válida)."""
    assert is_overheating(0) is False
