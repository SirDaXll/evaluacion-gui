import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QLineEdit, QMessageBox
from medida import Medida

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Galón vs Pinta")
        self.texto1 = QLabel('Bienvenido')
        self.texto2= QLabel('Ingrese los datos')
        self.botonComparar = QPushButton('Comparar')
        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.texto_objeto1 = QLabel('Objeto 1')
        self.texto_objeto2 = QLabel('Objeto 2')
        self.texto_valor1 = QLabel('')
        self.texto_valor2 = QLabel('')
        self.boton_agregar_datos1 = QPushButton('Agregar datos')
        self.boton_agregar_datos2 = QPushButton('Agregar datos')
        self.signo_comparacion = QLabel(" ")

        self.vbox1.addWidget(self.texto_objeto1)
        self.vbox1.addWidget(QLabel('Cantidad:'))
        self.vbox1.addWidget(self.texto_valor1)
        self.vbox1.addWidget(QLabel('Valor equivalente en litros:'))
        self.vbox1.addWidget(self.texto_valor1)
        self.vbox1.addWidget(self.boton_agregar_datos1)
        self.vbox2.addWidget(self.texto_objeto2)
        self.vbox2.addWidget(QLabel('Cantidad:'))
        self.vbox2.addWidget(self.texto_valor2)
        self.vbox2.addWidget(QLabel('Valor equivalente en litros:'))
        self.vbox2.addWidget(self.texto_valor2)
        self.vbox2.addWidget(self.boton_agregar_datos2)
        self.hbox.addLayout(self.vbox1)
        self.hbox.addWidget(self.signo_comparacion)
        self.hbox.addLayout(self.vbox2)

        vbox_principal = QVBoxLayout()
        vbox_principal.addWidget(self.texto1)
        vbox_principal.addWidget(self.texto2)
        vbox_principal.addLayout(self.hbox)
        vbox_principal.addWidget(self.botonComparar)

        self.setLayout(vbox_principal)
        self.setWindowTitle('Interfaz de comparación')
        self.show()

        self.boton_agregar_datos1.clicked.connect(lambda: self.agregarDatos(1))
        self.boton_agregar_datos2.clicked.connect(lambda: self.agregarDatos(2))
        self.botonComparar.clicked.connect(lambda: self.comparar(self.medida1, self.medida2))

    def agregarDatos(self, objeto):
        self.setWindowTitle("Ingresar datos")
        ventanaDatos = QDialog(self)
        layoutDatos = QVBoxLayout(ventanaDatos)
        labelNombre = QLabel('Ingrese el nombre de la medida')
        inputNombre = QLineEdit()
        labelCantidad = QLabel('Ingrese la cantidad')
        inputCantidad = QLineEdit()
        botonGuardar = QPushButton('Guardar')

        layoutDatos.addWidget(labelNombre)
        layoutDatos.addWidget(inputNombre)
        layoutDatos.addWidget(labelCantidad)
        layoutDatos.addWidget(inputCantidad)
        layoutDatos.addWidget(botonGuardar)

        botonGuardar.clicked.connect(lambda: self.guardarDatos(objeto, inputNombre.text(), inputCantidad.text()))
        botonGuardar.clicked.connect(ventanaDatos.close)
        ventanaDatos.exec()

    def guardarDatos(self, objeto, nombre, cantidad):
        if objeto == 1:
            self.texto_objeto1.setText(nombre)
            self.texto_valor1.setText(cantidad)
            self.medida1 = Medida(nombre, cantidad)
        else:
            self.texto_objeto2.setText(nombre)
            self.texto_valor2.setText(cantidad)
            self.medida2 = Medida(nombre, cantidad)


    def comparar(self, medida1, medida2):
        if medida1.valorEquivalente < medida2.valorEquivalente:
            comparacion = "<"
        elif medida1.valorEquivalente > medida2.valorEquivalente:
            comparacion = ">"
        else:
            comparacion = "="
        self.signo_comparacion.setText(comparacion)

   



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(app.exec())
