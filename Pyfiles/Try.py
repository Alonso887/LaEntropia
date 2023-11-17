import tkinter as tk
from tkcalendar import Calendar

def mostrar_calendario():
    fecha_seleccionada = cal.get_date()
    etiqueta.config(text=f"Fecha seleccionada: {fecha_seleccionada}")
    top_calendario.destroy()

def abrir_calendario():
    global top_calendario
    top_calendario = tk.Toplevel(ventana)
    top_calendario.title("Selector de Fecha")

    # Crear un widget de calendario en la ventana superior
    global cal
    cal = Calendar(top_calendario, selectmode="day", year=2023, month=1, day=1)
    cal.pack(pady=10)

    # Crear un botón para cerrar el calendario y obtener la fecha seleccionada
    boton_cerrar_calendario = tk.Button(top_calendario, text="Seleccionar Fecha", command=mostrar_calendario)
    boton_cerrar_calendario.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calendario con Botón")

# Crear un botón para abrir el calendario
boton_abrir_calendario = tk.Button(ventana, text="Abrir Calendario", command=abrir_calendario)
boton_abrir_calendario.pack(pady=10)

# Crear una etiqueta para mostrar la fecha seleccionada
etiqueta = tk.Label(ventana, text="Fecha seleccionada: ")
etiqueta.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()


