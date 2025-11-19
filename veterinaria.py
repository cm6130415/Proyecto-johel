import sys
import json
import random
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QTableWidget, QTableWidgetItem,
                             QDialog, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QMessageBox, QCheckBox, QFormLayout, QComboBox, QStackedWidget,
                             QCalendarWidget)
from PyQt5.QtCore import QDate
from datetime import timedelta
# ===== BASE DE DATOS =====


class usuario:
    def __init__(self,id,nombre,correo,contraseña,rol,telefono,direccion):
        self.id=id
        self.nombre=nombre
        self.correo=correo
        self.contraseña=contraseña
        self.rol=rol
        self.telefono=telefono
        self.direccion=direccion
    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "contraseña": self.contraseña,
            "rol": self.rol,
            "telefono": self.telefono,
            "direccion": self.direccion
        }
    @staticmethod
    def desde_diccionario(datos):
        return usuario(
            id=datos["id"],
            nombre=datos["nombre"],
            correo=datos["correo"],
            contraseña=datos["contraseña"],
            rol=datos["rol"],
            telefono=datos["telefono"],
            direccion=datos["direccion"]
        )
class mascotas:
    def __init__(self,id,nombre,edad,especie,raza,propietario,sexo,peso):
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.especie=especie
        self.raza=raza
        self.propietario=propietario
        self.sexo=sexo
        self.peso=peso 
    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "especie": self.especie,
            "raza": self.raza,
            "propietario": self.propietario,
            "sexo": self.sexo,
            "peso": self.peso
        }
    @staticmethod
    def desde_diccionario(datos):
        return mascotas(
            id=datos["id"],
            nombre=datos["nombre"],
            edad=datos["edad"],
            especie=datos["especie"],
            raza=datos["raza"],
            propietario=datos["propietario"],
            sexo=datos["sexo"],
            peso=datos["peso"]
        )
class citas:
    def __init__(self, id, mascota, fecha, hora, motivo, estado, tipo="Consulta", veterinario=None, asistente=None):
        self.id = id
        self.mascota = mascota
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.tipo = tipo  # "Consulta", "Cirugía", "Grooming"
        self.veterinario = veterinario
        self.asistente = asistente
    
    def a_diccionario(self):
        return {
            "id": self.id,
            "mascota": self.mascota,
            "fecha": self.fecha,
            "hora": self.hora,
            "motivo": self.motivo,
            "estado": self.estado,
            "tipo": self.tipo,
            "veterinario": self.veterinario,
            "asistente": self.asistente
        }
    
    @staticmethod
    def desde_diccionario(datos):
        return citas(
            id=datos["id"],
            mascota=datos["mascota"],
            fecha=datos["fecha"],
            hora=datos["hora"],
            motivo=datos["motivo"],
            estado=datos["estado"],
            tipo=datos.get("tipo", "Consulta"),
            veterinario=datos.get("veterinario"),
            asistente=datos.get("asistente")
        )
class historial_medico:
    def __init__(self,id,mascota,fecha_diagnostico,diagnostico,tratamiento,veterinario):
        self.id=id
        self.mascota=mascota
        self.fecha_diagnostico=fecha_diagnostico
        self.diagnostico=diagnostico
        self.tratamiento=tratamiento
        self.veterinario=veterinario
    def a_diccionario(self):
        return {
            "id": self.id,
            "mascota": self.mascota,
            "fecha_diagnostico": self.fecha_diagnostico,
            "diagnostico": self.diagnostico,
            "tratamiento": self.tratamiento,
            "veterinario": self.veterinario
        }
    @staticmethod
    def desde_diccionario(datos):
        return historial_medico(
            id=datos["id"],
            mascota=datos["mascota"],
            fecha_diagnostico=datos["fecha_diagnostico"],
            diagnostico=datos["diagnostico"],
            tratamiento=datos["tratamiento"],
            veterinario=datos["veterinario"]
        )
class vacunas:
    def __init__(self,id,mascota,nombre_vacuna,fecha_aplicacion,proxima_dosis):
        self.id=id
        self.mascota=mascota
        self.nombre_vacuna=nombre_vacuna
        self.fecha_aplicacion=fecha_aplicacion
        self.proxima_dosis=proxima_dosis
    def a_diccionario(self):
        return {
            "id": self.id,
            "mascota": self.mascota,
            "nombre_vacuna": self.nombre_vacuna,
            "fecha_aplicacion": self.fecha_aplicacion,
            "proxima_dosis": self.proxima_dosis
        }
    @staticmethod
    def desde_diccionario(datos):
        return vacunas(
            id=datos["id"],
            mascota=datos["mascota"],
            nombre_vacuna=datos["nombre_vacuna"],
            fecha_aplicacion=datos["fecha_aplicacion"],
            proxima_dosis=datos["proxima_dosis"]
        )
class cirujias:
    def __init__(self,id,mascota,fecha_cirugia,tipo_cirugia,veterinario,resultado):
        self.id=id
        self.mascota=mascota
        self.fecha_cirugia=fecha_cirugia
        self.tipo_cirugia=tipo_cirugia
        self.veterinario=veterinario
        self.resultado=resultado
    def a_diccionario(self):
        return {
            "id": self.id,
            "mascota": self.mascota,
            "fecha_cirugia": self.fecha_cirugia,
            "tipo_cirugia": self.tipo_cirugia,
            "veterinario": self.veterinario,
            "resultado": self.resultado
        }
    @staticmethod
    def desde_diccionario(datos):
        return cirujias(
            id=datos["id"],
            mascota=datos["mascota"],
            fecha_cirugia=datos["fecha_cirugia"],
            tipo_cirugia=datos["tipo_cirugia"],
            veterinario=datos["veterinario"],
            resultado=datos["resultado"]
        )
class productos:
    def __init__(self,id,nombre,descripcion,precio,stock):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.stock=stock
    def a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock
        }
    @staticmethod
    def desde_diccionario(datos):
        return productos(
            id=datos["id"],
            nombre=datos["nombre"],
            descripcion=datos["descripcion"],
            precio=datos["precio"],
            stock=datos["stock"]
        )
class facturas:
    def __init__(self,id,usuario,productos,fecha,total,metodo_pago):
        self.id=id
        self.usuario=usuario
        self.productos=productos
        self.fecha=fecha
        self.total=total
        self.metodo_pago=metodo_pago
    def a_diccionario(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "productos": self.productos,
            "fecha": self.fecha,
            "total": self.total,
            "metodo_pago": self.metodo_pago
        }
    @staticmethod
    def desde_diccionario(datos):
        return facturas(
            id=datos["id"],
            usuario=datos["usuario"],
            productos=datos["productos"],
            fecha=datos["fecha"],
            total=datos["total"],
            metodo_pago=datos["metodo_pago"]
        )
# ===== DIÁLOGOS =====
class DialogoAgendarCita(QDialog):
    """Diálogo para agendar una nueva cita."""
    def __init__(self, mascotas_lista, usuarios_lista, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agendar Cita")
        self.setFixedSize(450, 450)
        self.mascotas_lista = mascotas_lista
        self.usuarios_lista = usuarios_lista

        # Campos
        self.combo_mascota = QComboBox()
        self.combo_mascota.addItems([f"{m.nombre} ({m.propietario})" for m in mascotas_lista])
        
        # Tipo de cita
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Consulta", "Cirugía", "Grooming"])
        self.combo_tipo.currentTextChanged.connect(self.actualizar_campos_segun_tipo)
        
        # Calendario para fecha
        self.calendario = QCalendarWidget()
        self.calendario.setSelectedDate(QDate.currentDate())
        
        self.input_hora = QLineEdit()
        self.input_hora.setPlaceholderText("Ej: 14:30")
        
        self.input_motivo = QTextEdit()
        self.input_motivo.setPlaceholderText("Motivo de la cita")
        
        self.combo_estado = QComboBox()
        self.combo_estado.addItems(["Pendiente", "Completada", "Cancelada"])
        
        # Campos para cirugía
        self.label_veterinario = QLabel("Veterinario:")
        self.combo_veterinario = QComboBox()
        self.actualizar_veterinarios()
        
        self.label_asistente = QLabel("Asistente:")
        self.combo_asistente = QComboBox()
        self.actualizar_asistentes()
        
        # Botón guardar
        self.boton_guardar = QPushButton("Agendar")
        self.boton_guardar.clicked.connect(self.agendar_cita)

        # Layout
        layout = QFormLayout()
        layout.addRow("Mascota:", self.combo_mascota)
        layout.addRow("Tipo de cita:", self.combo_tipo)
        layout.addRow("Fecha:", self.calendario)
        layout.addRow("Hora (HH:MM):", self.input_hora)
        layout.addRow("Motivo:", self.input_motivo)
        layout.addRow("Estado:", self.combo_estado)
        layout.addRow(self.label_veterinario, self.combo_veterinario)
        layout.addRow(self.label_asistente, self.combo_asistente)
        layout.addRow(self.boton_guardar)
        self.setLayout(layout)

        self.cita = None
        self.actualizar_campos_segun_tipo()

    def actualizar_veterinarios(self):
        """Cargar solo veterinarios disponibles."""
        self.combo_veterinario.clear()
        veterinarios = [u.nombre for u in self.usuarios_lista if u.rol == "Veterinario"]
        self.combo_veterinario.addItems(veterinarios if veterinarios else ["Sin veterinarios"])

    def actualizar_asistentes(self):
        """Cargar solo asistentes disponibles."""
        self.combo_asistente.clear()
        asistentes = [u.nombre for u in self.usuarios_lista if u.rol == "Asistente"]
        self.combo_asistente.addItems(asistentes if asistentes else ["Sin asistentes"])

    def actualizar_campos_segun_tipo(self):
        """Mostrar/ocultar campos según el tipo de cita."""
        es_cirugia = self.combo_tipo.currentText() == "Cirugía"
        self.label_veterinario.setVisible(es_cirugia)
        self.combo_veterinario.setVisible(es_cirugia)
        self.label_asistente.setVisible(es_cirugia)
        self.combo_asistente.setVisible(es_cirugia)

    def agendar_cita(self):
        """Validar y crear la cita."""
        try:
            # Obtener datos
            mascota_texto = self.combo_mascota.currentText()
            mascota_nombre = mascota_texto.split(" (")[0]
            mascota = next((m for m in self.mascotas_lista if m.nombre == mascota_nombre), None)
            
            if not mascota:
                QMessageBox.warning(self, "Error", "Mascota no válida.")
                return

            fecha = self.calendario.selectedDate().toString("yyyy-MM-dd")
            hora = self.input_hora.text().strip()
            motivo = self.input_motivo.toPlainText().strip()
            estado = self.combo_estado.currentText()
            tipo = self.combo_tipo.currentText()
            veterinario = self.combo_veterinario.currentText() if tipo == "Cirugía" else None
            asistente = self.combo_asistente.currentText() if tipo == "Cirugía" else None

            # Validaciones
            if not hora or not motivo:
                QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
                return

            if tipo == "Cirugía" and (veterinario == "Sin veterinarios" or asistente == "Sin asistentes"):
                QMessageBox.warning(self, "Error", "Debe haber veterinarios y asistentes disponibles para cirugías.")
                return

            # Validar formato de hora
            try:
                datetime.strptime(hora, "%H:%M")
            except ValueError:
                QMessageBox.warning(self, "Error", "Formato de hora incorrecto (use HH:MM).")
                return

            # Generar ID pseudoaleatorio de 7 dígitos
            id_cita = str(random.randint(1000000, 9999999))

            # Crear objeto cita
            self.cita = citas(
                id=id_cita,
                mascota=mascota.nombre,
                fecha=fecha,
                hora=hora,
                motivo=motivo,
                estado=estado,
                tipo=tipo,
                veterinario=veterinario,
                asistente=asistente
            )

            QMessageBox.information(self, "Éxito", f"Cita agendada con ID: {id_cita}")
            self.accept()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error: {str(e)}")
class DialogoEditarCita(QDialog):
    """Diálogo para editar una cita existente."""
    def __init__(self, cita_obj, mascotas_lista, usuarios_lista, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Cita")
        self.setFixedSize(450, 450)
        self.cita_obj = cita_obj
        self.mascotas_lista = mascotas_lista
        self.usuarios_lista = usuarios_lista

        self.combo_mascota = QComboBox()
        self.combo_mascota.addItems([f"{m.nombre} ({m.propietario})" for m in mascotas_lista])
        for i in range(self.combo_mascota.count()):
            if cita_obj.mascota in self.combo_mascota.itemText(i):
                self.combo_mascota.setCurrentIndex(i)
                break
        
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Consulta", "Cirugía", "Grooming"])
        self.combo_tipo.setCurrentText(cita_obj.tipo)
        self.combo_tipo.currentTextChanged.connect(self.actualizar_campos_segun_tipo)
        
        self.calendario = QCalendarWidget()
        fecha_obj = datetime.strptime(cita_obj.fecha, "%Y-%m-%d")
        self.calendario.setSelectedDate(QDate(fecha_obj.year, fecha_obj.month, fecha_obj.day))
        
        self.input_hora = QLineEdit(cita_obj.hora)
        
        self.input_motivo = QTextEdit()
        self.input_motivo.setText(cita_obj.motivo)
        
        self.combo_estado = QComboBox()
        self.combo_estado.addItems(["Pendiente", "Confirmada", "Completada", "Cancelada"])
        self.combo_estado.setCurrentText(cita_obj.estado)
        
        self.label_veterinario = QLabel("Veterinario:")
        self.combo_veterinario = QComboBox()
        self.actualizar_veterinarios()
        if cita_obj.veterinario:
            idx = self.combo_veterinario.findText(cita_obj.veterinario)
            if idx >= 0:
                self.combo_veterinario.setCurrentIndex(idx)
        
        self.label_asistente = QLabel("Asistente:")
        self.combo_asistente = QComboBox()
        self.actualizar_asistentes()
        if cita_obj.asistente:
            idx = self.combo_asistente.findText(cita_obj.asistente)
            if idx >= 0:
                self.combo_asistente.setCurrentIndex(idx)

        self.boton_guardar = QPushButton("Guardar cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)

        layout = QFormLayout()
        layout.addRow("Mascota:", self.combo_mascota)
        layout.addRow("Tipo de cita:", self.combo_tipo)
        layout.addRow("Fecha:", self.calendario)
        layout.addRow("Hora (HH:MM):", self.input_hora)
        layout.addRow("Motivo:", self.input_motivo)
        layout.addRow("Estado:", self.combo_estado)
        layout.addRow(self.label_veterinario, self.combo_veterinario)
        layout.addRow(self.label_asistente, self.combo_asistente)
        layout.addRow(self.boton_guardar)
        self.setLayout(layout)
        
        self.actualizar_campos_segun_tipo()

    def actualizar_veterinarios(self):
        self.combo_veterinario.clear()
        veterinarios = [u.nombre for u in self.usuarios_lista if u.rol == "Veterinario"]
        self.combo_veterinario.addItems(veterinarios if veterinarios else ["Sin veterinarios"])

    def actualizar_asistentes(self):
        self.combo_asistente.clear()
        asistentes = [u.nombre for u in self.usuarios_lista if u.rol == "Asistente"]
        self.combo_asistente.addItems(asistentes if asistentes else ["Sin asistentes"])

    def actualizar_campos_segun_tipo(self):
        es_cirugia = self.combo_tipo.currentText() == "Cirugía"
        self.label_veterinario.setVisible(es_cirugia)
        self.combo_veterinario.setVisible(es_cirugia)
        self.label_asistente.setVisible(es_cirugia)
        self.combo_asistente.setVisible(es_cirugia)

    def guardar_cambios(self):
        """Validar y actualizar la cita."""
        try:
            mascota_texto = self.combo_mascota.currentText()
            mascota_nombre = mascota_texto.split(" (")[0]
            
            fecha = self.calendario.selectedDate().toString("yyyy-MM-dd")
            hora = self.input_hora.text().strip()
            motivo = self.input_motivo.toPlainText().strip()
            estado = self.combo_estado.currentText()
            tipo = self.combo_tipo.currentText()
            veterinario = self.combo_veterinario.currentText() if tipo == "Cirugía" else None
            asistente = self.combo_asistente.currentText() if tipo == "Cirugía" else None

            if not hora or not motivo:
                QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
                return

            if tipo == "Cirugía" and (veterinario == "Sin veterinarios" or asistente == "Sin asistentes"):
                QMessageBox.warning(self, "Error", "Debe haber veterinarios y asistentes disponibles para cirugías.")
                return

            try:
                datetime.strptime(hora, "%H:%M")
            except ValueError:
                QMessageBox.warning(self, "Error", "Formato de hora incorrecto (use HH:MM).")
                return

            self.cita_obj.mascota = mascota_nombre
            self.cita_obj.fecha = fecha
            self.cita_obj.hora = hora
            self.cita_obj.motivo = motivo
            self.cita_obj.estado = estado
            self.cita_obj.tipo = tipo
            self.cita_obj.veterinario = veterinario
            self.cita_obj.asistente = asistente

            QMessageBox.information(self, "Éxito", "Cita actualizada correctamente.")
            self.accept()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error: {str(e)}")
class DialogoAgregarUsuario(QDialog):
    """Diálogo para agregar un nuevo usuario."""
    def __init__(self, usuarios_existentes, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar Usuario")
        self.setFixedSize(350, 300)
        self.usuarios_existentes = usuarios_existentes

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre completo")
        
        self.input_correo = QLineEdit()
        self.input_correo.setPlaceholderText("Correo electrónico")
        
        self.input_contraseña = QLineEdit()
        self.input_contraseña.setPlaceholderText("Contraseña")
        self.input_contraseña.setEchoMode(QLineEdit.Password)
        
        self.input_telefono = QLineEdit()
        self.input_telefono.setPlaceholderText("Teléfono")
        
        self.input_direccion = QLineEdit()
        self.input_direccion.setPlaceholderText("Dirección")
        
        self.combo_rol = QComboBox()
        self.combo_rol.addItems(["Recepcionista", "Veterinario", "Asistente", "Administrador"])

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_usuario)

        layout = QFormLayout()
        layout.addRow("Nombre:", self.input_nombre)
        layout.addRow("Correo:", self.input_correo)
        layout.addRow("Contraseña:", self.input_contraseña)
        layout.addRow("Teléfono:", self.input_telefono)
        layout.addRow("Dirección:", self.input_direccion)
        layout.addRow("Rol:", self.combo_rol)
        layout.addRow(self.boton_guardar)
        self.setLayout(layout)

        self.usuario = None

    def guardar_usuario(self):
        nombre = self.input_nombre.text().strip()
        correo = self.input_correo.text().strip()
        contraseña = self.input_contraseña.text().strip()
        telefono = self.input_telefono.text().strip()
        direccion = self.input_direccion.text().strip()
        rol = self.combo_rol.currentText()

        if not nombre or not correo or not contraseña or not telefono or not direccion:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if any(u.correo == correo for u in self.usuarios_existentes):
            QMessageBox.warning(self, "Error", "El correo ya existe.")
            return

        id_usuario = str(random.randint(1000000, 9999999))

        self.usuario = usuario(
            id=id_usuario,
            nombre=nombre,
            correo=correo,
            contraseña=contraseña,
            rol=rol,
            telefono=telefono,
            direccion=direccion
        )

        QMessageBox.information(self, "Éxito", f"Usuario '{nombre}' creado correctamente.")
        self.accept()
class DialogoEditarUsuario(QDialog):
    """Diálogo para editar un usuario existente."""
    def __init__(self, usuario_obj, usuarios_existentes, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Usuario")
        self.setFixedSize(350, 300)
        self.usuario_obj = usuario_obj
        self.usuarios_existentes = usuarios_existentes

        self.input_nombre = QLineEdit(usuario_obj.nombre)
        self.input_correo = QLineEdit(usuario_obj.correo)
        self.input_contraseña = QLineEdit(usuario_obj.contraseña)
        self.input_contraseña.setEchoMode(QLineEdit.Password)
        self.input_telefono = QLineEdit(usuario_obj.telefono)
        self.input_direccion = QLineEdit(usuario_obj.direccion)
        
        self.combo_rol = QComboBox()
        self.combo_rol.addItems(["Recepcionista", "Veterinario", "Asistente", "Administrador"])
        self.combo_rol.setCurrentText(usuario_obj.rol)

        self.boton_guardar = QPushButton("Guardar cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)

        layout = QFormLayout()
        layout.addRow("Nombre:", self.input_nombre)
        layout.addRow("Correo:", self.input_correo)
        layout.addRow("Contraseña:", self.input_contraseña)
        layout.addRow("Teléfono:", self.input_telefono)
        layout.addRow("Dirección:", self.input_direccion)
        layout.addRow("Rol:", self.combo_rol)
        layout.addRow(self.boton_guardar)
        self.setLayout(layout)

    def guardar_cambios(self):
        nombre = self.input_nombre.text().strip()
        correo = self.input_correo.text().strip()
        contraseña = self.input_contraseña.text().strip()
        telefono = self.input_telefono.text().strip()
        direccion = self.input_direccion.text().strip()
        rol = self.combo_rol.currentText()

        if not nombre or not correo or not contraseña or not telefono or not direccion:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if correo != self.usuario_obj.correo and any(u.correo == correo for u in self.usuarios_existentes):
            QMessageBox.warning(self, "Error", "El correo ya existe.")
            return

        self.usuario_obj.nombre = nombre
        self.usuario_obj.correo = correo
        self.usuario_obj.contraseña = contraseña
        self.usuario_obj.telefono = telefono
        self.usuario_obj.direccion = direccion
        self.usuario_obj.rol = rol

        QMessageBox.information(self, "Éxito", "Usuario actualizado correctamente.")
        self.accept()
class DialogoAgregarMascota(QDialog):
    """Diálogo para agregar una nueva mascota."""
    def __init__(self, mascotas_existentes, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar Mascota")
        self.setFixedSize(350, 350)
        self.mascotas_existentes = mascotas_existentes

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre de la mascota")
        
        self.input_edad = QLineEdit()
        self.input_edad.setPlaceholderText("Edad (años)")
        
        self.combo_especie = QComboBox()
        self.combo_especie.addItems(["Perro", "Gato", "Conejo", "Pajaro", "Otro"])
        
        self.input_raza = QLineEdit()
        self.input_raza.setPlaceholderText("Raza")
        
        self.input_propietario = QLineEdit()
        self.input_propietario.setPlaceholderText("Nombre del propietario")
        
        self.combo_sexo = QComboBox()
        self.combo_sexo.addItems(["Macho", "Hembra"])
        
        self.input_peso = QLineEdit()
        self.input_peso.setPlaceholderText("Peso (kg)")

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_mascota)

        layout = QFormLayout()
        layout.addRow("Nombre:", self.input_nombre)
        layout.addRow("Edad:", self.input_edad)
        layout.addRow("Especie:", self.combo_especie)
        layout.addRow("Raza:", self.input_raza)
        layout.addRow("Propietario:", self.input_propietario)
        layout.addRow("Sexo:", self.combo_sexo)
        layout.addRow("Peso:", self.input_peso)
        layout.addRow(self.boton_guardar)
        self.setLayout(layout)

        self.mascota = None

    def guardar_mascota(self):
        nombre = self.input_nombre.text().strip()
        edad = self.input_edad.text().strip()
        especie = self.combo_especie.currentText()
        raza = self.input_raza.text().strip()
        propietario = self.input_propietario.text().strip()
        sexo = self.combo_sexo.currentText()
        peso = self.input_peso.text().strip()

        if not nombre or not edad or not raza or not propietario or not peso:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            edad_int = int(edad)
            peso_float = float(peso)
            if edad_int < 0 or peso_float <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Edad y peso deben ser números válidos.")
            return

        if any(m.nombre == nombre for m in self.mascotas_existentes):
            QMessageBox.warning(self, "Error", "Ya existe una mascota con ese nombre.")
            return

        id_mascota = str(random.randint(1000000, 9999999))

        self.mascota = mascotas(
            id=id_mascota,
            nombre=nombre,
            edad=edad_int,
            especie=especie,
            raza=raza,
            propietario=propietario,
            sexo=sexo,
            peso=peso_float
        )

        QMessageBox.information(self, "Éxito", f"Mascota '{nombre}' creada correctamente.")
        self.accept()
class DialogoEditarMascota(QDialog):
    """Diálogo para editar una mascota existente."""
    def __init__(self, mascota_obj, mascotas_existentes, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Mascota")
        self.setFixedSize(350, 350)
        self.mascota_obj = mascota_obj
        self.mascotas_existentes = mascotas_existentes

        self.input_nombre = QLineEdit(mascota_obj.nombre)
        self.input_edad = QLineEdit(str(mascota_obj.edad))
        
        self.combo_especie = QComboBox()
        self.combo_especie.addItems(["Perro", "Gato", "Conejo", "Pajaro", "Otro"])
        self.combo_especie.setCurrentText(mascota_obj.especie)
        
        self.input_raza = QLineEdit(mascota_obj.raza)
        self.input_propietario = QLineEdit(mascota_obj.propietario)
        
        self.combo_sexo = QComboBox()
        self.combo_sexo.addItems(["Macho", "Hembra"])
        self.combo_sexo.setCurrentText(mascota_obj.sexo)
        
        self.input_peso = QLineEdit(str(mascota_obj.peso))

        self.boton_guardar = QPushButton("Guardar cambios")
        self.boton_guardar.clicked.connect(self.guardar_cambios)

        layout = QFormLayout()
        layout.addRow("Nombre:", self.input_nombre)
        layout.addRow("Edad:", self.input_edad)
        layout.addRow("Especie:", self.combo_especie)
        layout.addRow("Raza:", self.input_raza)
        layout.addRow("Propietario:", self.input_propietario)
        layout.addRow("Sexo:", self.combo_sexo)
        layout.addRow("Peso:", self.input_peso)
        layout.addRow(self.boton_guardar)
        self.setLayout(layout)

    def guardar_cambios(self):
        nombre = self.input_nombre.text().strip()
        edad = self.input_edad.text().strip()
        especie = self.combo_especie.currentText()
        raza = self.input_raza.text().strip()
        propietario = self.input_propietario.text().strip()
        sexo = self.combo_sexo.currentText()
        peso = self.input_peso.text().strip()

        if not nombre or not edad or not raza or not propietario or not peso:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            edad_int = int(edad)
            peso_float = float(peso)
            if edad_int < 0 or peso_float <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Edad y peso deben ser números válidos.")
            return

        if nombre != self.mascota_obj.nombre and any(m.nombre == nombre for m in self.mascotas_existentes):
            QMessageBox.warning(self, "Error", "Ya existe una mascota con ese nombre.")
            return

        self.mascota_obj.nombre = nombre
        self.mascota_obj.edad = edad_int
        self.mascota_obj.especie = especie
        self.mascota_obj.raza = raza
        self.mascota_obj.propietario = propietario
        self.mascota_obj.sexo = sexo
        self.mascota_obj.peso = peso_float

        QMessageBox.information(self, "Éxito", "Mascota actualizada correctamente.")
        self.accept()
# ===== PÁGINAS =====
class paginaInicio(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
class paginaCitas(QWidget):
    def __init__(self, app_ref=None):
        super().__init__()
        self.app_ref = app_ref
        layout = QVBoxLayout()

        # Botón para agendar cita
        self.boton_agendar = QPushButton("Agendar Nueva Cita")
        self.boton_agendar.clicked.connect(self.agendar_nueva_cita)
        
        # Tabla para mostrar citas
        self.tabla_citas = QTableWidget()
        self.tabla_citas.setColumnCount(9)
        self.tabla_citas.setHorizontalHeaderLabels(["ID", "Mascota", "Fecha", "Hora", "Tipo", "Veterinario", "Asistente", "Estado", "Acciones"])
        self.tabla_citas.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_citas.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla_citas.itemDoubleClicked.connect(self.editar_cita)

        layout.addWidget(self.boton_agendar)
        layout.addWidget(self.tabla_citas)
        self.setLayout(layout)

        self.actualizar_tabla()

    def agendar_nueva_cita(self):
        """Abrir diálogo para agendar cita (CREATE)."""
        if not self.app_ref or not self.app_ref.mascotas:
            QMessageBox.warning(self, "Error", "No hay mascotas registradas.")
            return

        dialogo = DialogoAgendarCita(self.app_ref.mascotas, self.app_ref.usuario, self)
        if dialogo.exec_() == QDialog.Accepted:
            if dialogo.cita:
                self.app_ref.citas.append(dialogo.cita)
                self.app_ref.guardar_citas()
                self.actualizar_tabla()
        if hasattr(self.app_ref, 'pagina_perfil'):
            self.app_ref.pagina_perfil.actualizar_horario()

    def editar_cita(self, item):
        """Editar cita al hacer doble clic (UPDATE)."""
        if not self.app_ref:
            return

        fila = item.row()
        if fila < 0 or fila >= len(self.app_ref.citas):
            return

        cita_obj = self.app_ref.citas[fila]
        dialogo = DialogoEditarCita(cita_obj, self.app_ref.mascotas, self.app_ref.usuario, self)
        if dialogo.exec_() == QDialog.Accepted:
            self.app_ref.guardar_citas()
            self.actualizar_tabla()

    def eliminar_cita(self, fila):
        """Eliminar cita (DELETE)."""
        if not self.app_ref or fila < 0 or fila >= len(self.app_ref.citas):
            return

        confirmacion = QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Está seguro de eliminar la cita para '{self.app_ref.citas[fila].mascota}' del {self.app_ref.citas[fila].fecha}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacion == QMessageBox.Yes:
            self.app_ref.citas.pop(fila)
            self.app_ref.guardar_citas()
            self.actualizar_tabla()

    def actualizar_tabla(self):
        """Actualizar y mostrar la tabla de citas (READ)."""
        self.tabla_citas.setRowCount(0)
        if self.app_ref:
            for idx, cita in enumerate(self.app_ref.citas):
                fila = self.tabla_citas.rowCount()
                self.tabla_citas.insertRow(fila)
                self.tabla_citas.setItem(fila, 0, QTableWidgetItem(cita.id))
                self.tabla_citas.setItem(fila, 1, QTableWidgetItem(cita.mascota))
                self.tabla_citas.setItem(fila, 2, QTableWidgetItem(cita.fecha))
                self.tabla_citas.setItem(fila, 3, QTableWidgetItem(cita.hora))
                self.tabla_citas.setItem(fila, 4, QTableWidgetItem(cita.tipo))
                self.tabla_citas.setItem(fila, 5, QTableWidgetItem(cita.veterinario or "-"))
                self.tabla_citas.setItem(fila, 6, QTableWidgetItem(cita.asistente or "-"))
                self.tabla_citas.setItem(fila, 7, QTableWidgetItem(cita.estado))
                
                # Botón Eliminar
                boton_eliminar = QPushButton("Eliminar")
                boton_eliminar.clicked.connect(lambda checked, f=idx: self.eliminar_cita(f))
                self.tabla_citas.setCellWidget(fila, 8, boton_eliminar)

        self.tabla_citas.resizeColumnsToContents()
class paginaMascotas(QWidget):
    def __init__(self, app_ref=None):
        super().__init__()
        self.app_ref = app_ref
        layout = QVBoxLayout()

        # Botón para agregar mascota
        self.boton_agregar = QPushButton("Agregar nueva mascota")
        self.boton_agregar.clicked.connect(self.agregar_mascota)

        # Tabla para mostrar mascotas
        self.tabla_mascotas = QTableWidget()
        self.tabla_mascotas.setColumnCount(9)
        self.tabla_mascotas.setHorizontalHeaderLabels(["ID", "Nombre", "Edad", "Especie", "Raza", "Propietario", "Sexo", "Peso", "Acciones"])
        self.tabla_mascotas.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_mascotas.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla_mascotas.itemDoubleClicked.connect(self.editar_mascota)

        layout.addWidget(self.boton_agregar)
        layout.addWidget(self.tabla_mascotas)
        self.setLayout(layout)

        self.actualizar_tabla()

    def agregar_mascota(self):
        """Abrir diálogo para agregar mascota (CREATE)."""
        if not self.app_ref:
            QMessageBox.warning(self, "Error", "No hay referencia a la aplicación.")
            return

        dialogo = DialogoAgregarMascota(self.app_ref.mascotas, self)
        if dialogo.exec_() == QDialog.Accepted:
            if dialogo.mascota:
                self.app_ref.mascotas.append(dialogo.mascota)
                self.app_ref.guardar_mascotas()
                self.actualizar_tabla()
                # Actualizar tabla de citas si está abierta
                if hasattr(self.app_ref, 'pagina_citas'):
                    self.app_ref.pagina_citas.actualizar_tabla()

    def editar_mascota(self, item):
        """Editar mascota al hacer doble clic (UPDATE)."""
        if not self.app_ref:
            return

        fila = item.row()
        if fila < 0 or fila >= len(self.app_ref.mascotas):
            return

        mascota_obj = self.app_ref.mascotas[fila]
        dialogo = DialogoEditarMascota(mascota_obj, self.app_ref.mascotas, self)
        if dialogo.exec_() == QDialog.Accepted:
            self.app_ref.guardar_mascotas()
            self.actualizar_tabla()

    def eliminar_mascota(self, fila):
        """Eliminar mascota (DELETE)."""
        if not self.app_ref or fila < 0 or fila >= len(self.app_ref.mascotas):
            return

        confirmacion = QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Está seguro de eliminar la mascota '{self.app_ref.mascotas[fila].nombre}'?\n(Nota: Se eliminarán las citas asociadas)",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacion == QMessageBox.Yes:
            mascota_eliminada = self.app_ref.mascotas[fila]
            # Eliminar citas asociadas a esta mascota
            self.app_ref.citas = [c for c in self.app_ref.citas if c.mascota != mascota_eliminada.nombre]
            # Eliminar mascota
            self.app_ref.mascotas.pop(fila)
            self.app_ref.guardar_mascotas()
            self.app_ref.guardar_citas()
            self.actualizar_tabla()
            QMessageBox.information(self, "Éxito", "Mascota eliminada correctamente.")

    def actualizar_tabla(self):
        """Actualizar y mostrar la tabla de mascotas (READ)."""
        self.tabla_mascotas.setRowCount(0)
        if self.app_ref:
            for idx, mascota in enumerate(self.app_ref.mascotas):
                fila = self.tabla_mascotas.rowCount()
                self.tabla_mascotas.insertRow(fila)
                self.tabla_mascotas.setItem(fila, 0, QTableWidgetItem(mascota.id))
                self.tabla_mascotas.setItem(fila, 1, QTableWidgetItem(mascota.nombre))
                self.tabla_mascotas.setItem(fila, 2, QTableWidgetItem(str(mascota.edad)))
                self.tabla_mascotas.setItem(fila, 3, QTableWidgetItem(mascota.especie))
                self.tabla_mascotas.setItem(fila, 4, QTableWidgetItem(mascota.raza))
                self.tabla_mascotas.setItem(fila, 5, QTableWidgetItem(mascota.propietario))
                self.tabla_mascotas.setItem(fila, 6, QTableWidgetItem(mascota.sexo))
                self.tabla_mascotas.setItem(fila, 7, QTableWidgetItem(f"{mascota.peso} kg"))
                
                # Botón Eliminar
                boton_eliminar = QPushButton("Eliminar")
                boton_eliminar.clicked.connect(lambda checked, f=idx: self.eliminar_mascota(f))
                self.tabla_mascotas.setCellWidget(fila, 8, boton_eliminar)

        self.tabla_mascotas.resizeColumnsToContents()
class paginaHistorial(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
class paginaperfil(QWidget):
    def __init__(self, app_ref=None):
        super().__init__()
        self.app_ref = app_ref
        layout = QVBoxLayout()

        # Tabs para usuarios y horario
        from PyQt5.QtWidgets import QTabWidget
        tabs = QTabWidget()

        # Tab 1: Gestión de usuarios
        tab_usuarios = QWidget()
        layout_usuarios = QVBoxLayout()

        self.boton_agregar = QPushButton("Agregar nuevo usuario")
        self.boton_agregar.clicked.connect(self.agregar_usuario)

        self.tabla_usuarios = QTableWidget()
        self.tabla_usuarios.setColumnCount(7)
        self.tabla_usuarios.setHorizontalHeaderLabels(["ID", "Nombre", "Correo", "Teléfono", "Dirección", "Rol", "Acciones"])
        self.tabla_usuarios.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_usuarios.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla_usuarios.itemDoubleClicked.connect(self.editar_usuario)

        layout_usuarios.addWidget(self.boton_agregar)
        layout_usuarios.addWidget(self.tabla_usuarios)
        tab_usuarios.setLayout(layout_usuarios)

        # Tab 2: Horario semanal de operaciones
        tab_horario = QWidget()
        layout_horario = QVBoxLayout()

        self.tabla_horario = QTableWidget()
        self.tabla_horario.setColumnCount(5)
        self.tabla_horario.setHorizontalHeaderLabels(["Fecha", "Hora", "Tipo", "Mascota", "Personal Involucrado"])
        self.tabla_horario.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla_horario.setSelectionBehavior(QTableWidget.SelectRows)

        layout_horario.addWidget(QLabel("Operaciones de la semana:"))
        layout_horario.addWidget(self.tabla_horario)
        tab_horario.setLayout(layout_horario)

        tabs.addTab(tab_usuarios, "Usuarios")
        tabs.addTab(tab_horario, "Horario Semanal")

        layout.addWidget(tabs)
        self.setLayout(layout)

        self.actualizar_tabla()
        self.actualizar_horario()

    def agregar_usuario(self):
        """Abrir diálogo para agregar usuario."""
        if not self.app_ref:
            QMessageBox.warning(self, "Error", "No hay referencia a la aplicación.")
            return

        dialogo = DialogoAgregarUsuario(self.app_ref.usuario, self)
        if dialogo.exec_() == QDialog.Accepted:
            if dialogo.usuario:
                self.app_ref.usuario.append(dialogo.usuario)
                self.app_ref.guardar_usuarios()
                self.actualizar_tabla()
                self.actualizar_horario()

    def editar_usuario(self, item):
        """Editar usuario al hacer doble clic."""
        if not self.app_ref:
            return

        fila = item.row()
        if fila < 0 or fila >= len(self.app_ref.usuario):
            return

        usuario_obj = self.app_ref.usuario[fila]
        dialogo = DialogoEditarUsuario(usuario_obj, self.app_ref.usuario, self)
        if dialogo.exec_() == QDialog.Accepted:
            self.app_ref.guardar_usuarios()
            self.actualizar_tabla()

    def eliminar_usuario(self, fila):
        """Eliminar usuario."""
        if not self.app_ref or fila < 0 or fila >= len(self.app_ref.usuario):
            return

        confirmacion = QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Está seguro de eliminar al usuario '{self.app_ref.usuario[fila].nombre}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacion == QMessageBox.Yes:
            self.app_ref.usuario.pop(fila)
            self.app_ref.guardar_usuarios()
            self.actualizar_tabla()

    def actualizar_tabla(self):
        """Actualizar la tabla con los usuarios."""
        self.tabla_usuarios.setRowCount(0)
        if self.app_ref:
            for idx, user in enumerate(self.app_ref.usuario):
                fila = self.tabla_usuarios.rowCount()
                self.tabla_usuarios.insertRow(fila)
                self.tabla_usuarios.setItem(fila, 0, QTableWidgetItem(user.id))
                self.tabla_usuarios.setItem(fila, 1, QTableWidgetItem(user.nombre))
                self.tabla_usuarios.setItem(fila, 2, QTableWidgetItem(user.correo))
                self.tabla_usuarios.setItem(fila, 3, QTableWidgetItem(user.telefono))
                self.tabla_usuarios.setItem(fila, 4, QTableWidgetItem(user.direccion))
                self.tabla_usuarios.setItem(fila, 5, QTableWidgetItem(user.rol))
                
                boton_eliminar = QPushButton("Eliminar")
                boton_eliminar.clicked.connect(lambda checked, f=fila: self.eliminar_usuario(f))
                self.tabla_usuarios.setCellWidget(fila, 6, boton_eliminar)

        self.tabla_usuarios.resizeColumnsToContents()

    def actualizar_horario(self):
        """Mostrar operaciones (cirugías) de la semana."""
        self.tabla_horario.setRowCount(0)
        if not self.app_ref:
            return

        hoy = datetime.now().date()
        # Obtener semana actual (lunes a domingo)
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        fin_semana = inicio_semana + timedelta(days=6)

        # Filtrar citas de tipo Cirugía en esta semana
        for cita in self.app_ref.citas:
            try:
                fecha_cita = datetime.strptime(cita.fecha, "%Y-%m-%d").date()
                if inicio_semana <= fecha_cita <= fin_semana and cita.tipo == "Cirugía":
                    fila = self.tabla_horario.rowCount()
                    self.tabla_horario.insertRow(fila)
                    
                    personal = []
                    if cita.veterinario:
                        personal.append(f"Vet: {cita.veterinario}")
                    if cita.asistente:
                        personal.append(f"Asist: {cita.asistente}")
                    personal_texto = ", ".join(personal) if personal else "N/A"

                    self.tabla_horario.setItem(fila, 0, QTableWidgetItem(cita.fecha))
                    self.tabla_horario.setItem(fila, 1, QTableWidgetItem(cita.hora))
                    self.tabla_horario.setItem(fila, 2, QTableWidgetItem(cita.tipo))
                    self.tabla_horario.setItem(fila, 3, QTableWidgetItem(cita.mascota))
                    self.tabla_horario.setItem(fila, 4, QTableWidgetItem(personal_texto))
            except:
                pass

        self.tabla_horario.resizeColumnsToContents()
class paginasalir(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
# ===== APLICACIÓN PRINCIPAL =====
class veterinariaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión para Veterinaria")
        self.setFixedSize(800, 600)
        main_layout = QVBoxLayout()
        # Listas de datos
        self.usuario = []
        self.mascotas = []
        self.citas = []
        self.historial_medico = []
        self.vacunas = []
        self.cirujias = []
        self.productos = []
        self.facturas = []
        # Cargar datos
        self.cargar_citas()
        self.cargar_usuarios()
        self.cargar_mascotas()
        # Menú de navegación
        menu = QHBoxLayout()
        btn_inicio = QPushButton("Inicio")
        btn_citas = QPushButton("Citas")
        btn_pacientes = QPushButton("Mascotas")
        btn_historial = QPushButton("Historial")
        btn_perfil = QPushButton("Perfil")
        btn_salir = QPushButton("Salir")
        menu.addWidget(btn_inicio)
        menu.addWidget(btn_citas)
        menu.addWidget(btn_pacientes)
        menu.addWidget(btn_historial)
        menu.addWidget(btn_perfil)
        menu.addWidget(btn_salir)
        # Stack de páginas
        self.stacked = QStackedWidget()
        self.pagina_inicio = paginaInicio()
        self.pagina_citas = paginaCitas(app_ref=self)
        self.pagina_mascotas = paginaMascotas(app_ref=self)
        self.pagina_historial = paginaHistorial()
        self.pagina_perfil = paginaperfil(app_ref=self)
        self.pagina_salir = paginasalir()
        # Conectar botones
        btn_inicio.clicked.connect(lambda: self.stacked.setCurrentWidget(self.pagina_inicio))
        btn_citas.clicked.connect(lambda: self.stacked.setCurrentWidget(self.pagina_citas))
        btn_pacientes.clicked.connect(lambda: self.stacked.setCurrentWidget(self.pagina_mascotas))
        btn_historial.clicked.connect(lambda: self.stacked.setCurrentWidget(self.pagina_historial))
        btn_perfil.clicked.connect(lambda: self.stacked.setCurrentWidget(self.pagina_perfil))
        btn_salir.clicked.connect(self.close)
        # Añadir widgets al stack
        self.stacked.addWidget(self.pagina_inicio)
        self.stacked.addWidget(self.pagina_citas)
        self.stacked.addWidget(self.pagina_mascotas)
        self.stacked.addWidget(self.pagina_historial)
        self.stacked.addWidget(self.pagina_perfil)
        self.stacked.addWidget(self.pagina_salir)
        # Layout final
        main_layout.addLayout(menu)
        main_layout.addWidget(self.stacked)
        self.setLayout(main_layout)
    #Funciones para guardar y cargar datos
    def guardar_citas(self):
        """Guardar citas en JSON."""
        try:
            with open("citas.json", "w") as archivo:
                json.dump([cita.a_diccionario() for cita in self.citas], archivo, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron guardar las citas: {str(e)}")
    def cargar_citas(self):
        """Cargar citas desde JSON."""
        try:
            with open("citas.json", "r") as archivo:
                datos = json.load(archivo)
                self.citas = [citas.desde_diccionario(cita) for cita in datos]
        except FileNotFoundError:
            self.citas = []
    def guardar_usuarios(self):
        """Guardar usuarios en JSON."""
        try:
            with open("usuarios.json", "w") as archivo:
                json.dump([user.a_diccionario() for user in self.usuario], archivo, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron guardar los usuarios: {str(e)}")
    def cargar_usuarios(self):
        """Cargar usuarios desde JSON."""
        try:
            with open("usuarios.json", "r") as archivo:
                datos = json.load(archivo)
                self.usuario = [usuario.desde_diccionario(user) for user in datos]
        except FileNotFoundError:
            self.usuario = []
    def guardar_mascotas(self):
        """Guardar mascotas en JSON."""
        try:
            with open("mascotas.json", "w") as archivo:
                json.dump([mascota.a_diccionario() for mascota in self.mascotas], archivo, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron guardar las mascotas: {str(e)}")
    def cargar_mascotas(self):
        """Cargar mascotas desde JSON."""
        try:
            with open("mascotas.json", "r") as archivo:
                datos = json.load(archivo)
                self.mascotas = [mascotas.desde_diccionario(mascota) for mascota in datos]
        except FileNotFoundError:
            self.mascotas = []
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    ventana = veterinariaApp()
    ventana.show()
    sys.exit(app.exec_())