import tkinter as tk
from tkinter import messagebox

class Equipo:
    def __init__(self, nombre, entrenador):
        self.nombre = nombre
        self.entrenador = entrenador
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_info(self):
        return f"Equipo: {self.nombre}\nEntrenador: {self.entrenador}\nNúmero de jugadores: {len(self.jugadores)}"

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self.nombre}\nEdad: {self.edad}\nPosición: {self.posicion}"

class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.resultado = None

    def jugar_partido(self, resultado):
        self.resultado = resultado

    def mostrar_resultado(self):
        if self.resultado:
            return f"Resultado: {self.equipo_local.nombre} {self.resultado[0]} - {self.resultado[1]} {self.equipo_visitante.nombre}"
        else:
            return "Partido no jugado todavía."

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def mostrar_info(self):
        info = f"Grupo: {self.nombre}\nEquipos en el grupo:"
        for equipo in self.equipos:
            info += f"\n- {equipo.nombre}"
        return info

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self.nombre}\nCiudad: {self.ciudad}\nCapacidad: {self.capacidad} personas"

class Mundial:
    def __init__(self):
        self.grupos = []
        self.estadios = []

    def registrar_grupo(self, grupo):
        self.grupos.append(grupo)

    def registrar_estadio(self, estadio):
        self.estadios.append(estadio)

    def generar_fixture(self):
        # En una implementación completa, generarías el fixture automáticamente.
        # Aquí simplemente devolvemos la cantidad de grupos registrados.
        return f"Se han registrado {len(self.grupos)} grupos en el Mundial."


class MundialApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión Mundial de Fútbol")

        self.mundial = Mundial()

        # Elementos de la interfaz
        self.label_equipo = tk.Label(self, text="Nombre del Equipo:")
        self.label_equipo.grid(row=0, column=0)
        self.entry_equipo = tk.Entry(self)
        self.entry_equipo.grid(row=0, column=1)

        self.label_entrenador = tk.Label(self, text="Nombre del Entrenador:")
        self.label_entrenador.grid(row=1, column=0)
        self.entry_entrenador = tk.Entry(self)
        self.entry_entrenador.grid(row=1, column=1)

        self.btn_registrar_equipo = tk.Button(self, text="Registrar Equipo", command=self.registrar_equipo)
        self.btn_registrar_equipo.grid(row=2, column=0, columnspan=2)

        self.label_jugador = tk.Label(self, text="Nombre del Jugador:")
        self.label_jugador.grid(row=3, column=0)
        self.entry_jugador = tk.Entry(self)
        self.entry_jugador.grid(row=3, column=1)

        self.label_edad = tk.Label(self, text="Edad del Jugador:")
        self.label_edad.grid(row=4, column=0)
        self.entry_edad = tk.Entry(self)
        self.entry_edad.grid(row=4, column=1)

        self.label_posicion = tk.Label(self, text="Posición del Jugador:")
        self.label_posicion.grid(row=5, column=0)
        self.entry_posicion = tk.Entry(self)
        self.entry_posicion.grid(row=5, column=1)

        self.btn_agregar_jugador = tk.Button(self, text="Agregar Jugador", command=self.agregar_jugador)
        self.btn_agregar_jugador.grid(row=6, column=0, columnspan=2)

        self.label_grupo = tk.Label(self, text="Nombre del Grupo:")
        self.label_grupo.grid(row=7, column=0)
        self.entry_grupo = tk.Entry(self)
        self.entry_grupo.grid(row=7, column=1)

        self.btn_registrar_grupo = tk.Button(self, text="Registrar Grupo", command=self.registrar_grupo)
        self.btn_registrar_grupo.grid(row=8, column=0, columnspan=2)

        self.label_estadio = tk.Label(self, text="Nombre del Estadio:")
        self.label_estadio.grid(row=9, column=0)
        self.entry_estadio = tk.Entry(self)
        self.entry_estadio.grid(row=9, column=1)

        self.label_ciudad = tk.Label(self, text="Ciudad del Estadio:")
        self.label_ciudad.grid(row=10, column=0)
        self.entry_ciudad = tk.Entry(self)
        self.entry_ciudad.grid(row=10, column=1)

        self.label_capacidad = tk.Label(self, text="Capacidad del Estadio:")
        self.label_capacidad.grid(row=11, column=0)
        self.entry_capacidad = tk.Entry(self)
        self.entry_capacidad.grid(row=11, column=1)

        self.btn_registrar_estadio = tk.Button(self, text="Registrar Estadio", command=self.registrar_estadio)
        self.btn_registrar_estadio.grid(row=12, column=0, columnspan=2)

        self.btn_generar_fixture = tk.Button(self, text="Generar Fixture", command=self.generar_fixture)
        self.btn_generar_fixture.grid(row=13, column=0, columnspan=2)

        self.label_info = tk.Label(self, text="")
        self.label_info.grid(row=14, column=0, columnspan=2)

    def registrar_equipo(self):
        nombre_equipo = self.entry_equipo.get()
        entrenador_equipo = self.entry_entrenador.get()
        equipo = Equipo(nombre_equipo, entrenador_equipo)
        self.mundial.registrar_grupo(Grupo(nombre_equipo))  # Registrar automáticamente un grupo con el nombre del equipo
        self.label_info.config(text=f"Equipo registrado:\n{equipo.mostrar_info()}")

    def agregar_jugador(self):
        nombre_jugador = self.entry_jugador.get()
        edad_jugador = self.entry_edad.get()
        posicion_jugador = self.entry_posicion.get()
        jugador = Jugador(nombre_jugador, edad_jugador, posicion_jugador)

        # Obtener el último equipo registrado
        if self.mundial.grupos:
            ultimo_grupo = self.mundial.grupos[-1]
            ultimo_grupo.equipos[-1].agregar_jugador(jugador)  # Agregar jugador al último equipo registrado

            self.label_info.config(text=f"Jugador agregado:\n{jugador.mostrar_info()}")
        else:
            messagebox.showwarning("Advertencia", "No hay equipos registrados aún.")

    def registrar_grupo(self):
        nombre_grupo = self.entry_grupo.get()
        grupo = Grupo(nombre_grupo)
        self.mundial.registrar_grupo(grupo)
        self.label_info.config(text=f"Grupo registrado:\n{grupo.mostrar_info()}")

    def registrar_estadio(self):
        nombre_estadio = self.entry_estadio.get()
        ciudad_estadio = self.entry_ciudad.get()
        capacidad_estadio = self.entry_capacidad.get()
        estadio = Estadio(nombre_estadio, ciudad_estadio, capacidad_estadio)
        self.mundial.registrar_estadio(estadio)
        self.label_info.config(text=f"Estadio registrado:\n{estadio.mostrar_info()}")

    def generar_fixture(self):
        fixture_info = self.mundial.generar_fixture()
        self.label_info.config(text=f"Fixture generado:\n{fixture_info}")

if __name__ == "__main__":
    app = MundialApp()
    app.mainloop()
