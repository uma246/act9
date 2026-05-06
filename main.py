"""
Aplicación principal de monitoreo de temperatura.
"""

from temperature import is_overheating


def main():
    """Función principal de la aplicación."""
    try:
        temp_input = input("Ingrese temperatura (°C): ")
        temp = float(temp_input)
        
        if is_overheating(temp):
            print("⚠️ ALARMA: Temperatura alta detectada")
        else:
            print("✅ Temperatura normal")
            
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
