"""
Módulo de control de temperatura para equipos industriales.
"""


def is_overheating(temp_c):
    """
    Valida si la temperatura está en alarma.
    
    Args:
        temp_c: Temperatura en grados Celsius
        
    Returns:
        True si hay alarma (temperatura > 80°C), False en caso contrario
        
    Raises:
        ValueError: Si la temperatura es negativa (error de sensor)
    """
    if temp_c < 0:
        raise ValueError("Error de lectura del sensor: temperatura negativa detectada")
    
    return temp_c > 80
