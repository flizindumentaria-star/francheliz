import tkinter as tk


# Clase base de comando
class Comando:
    def ejecutar(self):
        raise NotImplementedError("Este comando debe implementar ejecutar().")


# Comando para subir volumen
class SubirVolumen(Comando):
    def ejecutar(self):
        print("Volumen subido")


# Comando para bajar volumen
class BajarVolumen(Comando):
    def ejecutar(self):
        print("Volumen bajado")


# Control remoto que ejecuta comandos
class ControlRemoto:
    def __init__(self):
        self.comando = None

    def asignar_comando(self, comando):
        self.comando = comando

    def presionar_boton(self):
        if self.comando:
            self.comando.ejecutar()
        else:
            print("No se ha asignado ningún comando")


def crear_app():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Control Remoto")

    # Crear el control remoto
    control = ControlRemoto()

    # Funciones para los botones
    def subir_volumen():
        control.asignar_comando(SubirVolumen())
        control.presionar_boton()

    def bajar_volumen():
        control.asignar_comando(BajarVolumen())
        control.presionar_boton()

    # Botón para subir volumen
    boton_subir = tk.Button(ventana, text="Subir Volumen", command=subir_volumen)
    boton_subir.pack(pady=10)

    # Botón para bajar volumen
    boton_bajar = tk.Button(ventana, text="Bajar Volumen", command=bajar_volumen)
    boton_bajar.pack(pady=10)

    return ventana


if __name__ == "__main__":
    app = crear_app()
    # Ejecutar la ventana
    app.mainloop()
