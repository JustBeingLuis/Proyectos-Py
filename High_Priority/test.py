import psutil
import os
import sys

def set_high_priority(process_name):
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                psutil.Process(pid).nice(psutil.HIGH_PRIORITY_CLASS)
                print(f"Se estableció alta prioridad para el proceso {process_name} (PID: {pid}).")
                return
        print(f"No se encontró el proceso {process_name}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py nombre_del_proceso")
        sys.exit(1)

    process_name = sys.argv[1]
    set_high_priority(process_name)
