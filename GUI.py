import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QDialog, QLineEdit, QMessageBox
from medida import Medida

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #GENERAMOS NUESTRAS LABELS Y BOX NECESARIAS EN LA VENTANA PRINCIPAL
    def initUI(self):
        self.setWindowTitle("Galón vs Pinta")
        self.texto1 = QLabel('Bienvenido')
        self.texto2= QLabel('Ingrese los datos')
        self.botonComparar = QPushButton('Comparar')
        self.hbox = QHBoxLayout()
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.textoVariable1 = QLabel('Objeto 1')
        self.textoVariable2 = QLabel('Objeto 2')
        self.textoValor1 = QLabel('')
        self.textoValor2 = QLabel('')
        self.textoValorEquivalente1 = QLabel('')
        self.textoValorEquivalente2 = QLabel('')
        self.botonAgregar1 = QPushButton('Agregar datos')
        self.botonAgregar2 = QPushButton('Agregar datos')
        self.signoComparacion = QLabel(" ")

        #AQUI AGREGAMOS LOS TEXTOS DE LOS LITROS GALONES ETC, ALGUNOS SE MODIFICAN
        self.vbox1.addWidget(self.textoVariable1)
        self.vbox1.addWidget(QLabel('Cantidad:'))
        self.vbox1.addWidget(self.textoValor1)
        self.vbox1.addWidget(QLabel('Valor equivalente en litros:'))
        self.vbox1.addWidget(self.textoValorEquivalente1)
        self.vbox1.addWidget(self.botonAgregar1)
        self.vbox2.addWidget(self.textoVariable2)
        self.vbox2.addWidget(QLabel('Cantidad:'))
        self.vbox2.addWidget(self.textoValor2)
        self.vbox2.addWidget(QLabel('Valor equivalente en litros:'))
        self.vbox2.addWidget(self.textoValorEquivalente2)
        self.vbox2.addWidget(self.botonAgregar2)
        self.hbox.addLayout(self.vbox1)
        self.hbox.addWidget(self.signoComparacion)
        self.hbox.addLayout(self.vbox2)

        vbox_principal = QVBoxLayout()
        vbox_principal.addWidget(self.texto1)
        vbox_principal.addWidget(self.texto2)
        vbox_principal.addLayout(self.hbox)
        vbox_principal.addWidget(self.botonComparar)

        #DIEGO DIJO QUE LE PONGA NOMBRE Y SE MUESTRA
        self.setLayout(vbox_principal)
        self.setWindowTitle('Interfaz de comparación')
        self.show()

        #UTILIZAMOS LAMDA EXPRESIONS PARA MOSTRAR LO QUE NECESITAMOS
        self.botonAgregar1.clicked.connect(lambda: self.agregarDatos(1))
        self.botonAgregar2.clicked.connect(lambda: self.agregarDatos(2))
        self.botonComparar.clicked.connect(lambda: self.comparar(self.medida1, self.medida2))

    #FUNCION QUE DEFIN LA VENTANA DESPLEGABLE PARA EKL INGRESO DE DATOS
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

    #FUNCION QUE AGREGA DATOS EN BASE A LO INGRESADO Y MODIFICA LAS LABELS DE LA VENTANA PRINCIPAL PARA MOSTRARLOS
    #NO SE AGREGA VALIDACION, CONFIAMOS EN QUE SE INGRESE LO NECESARIO
    def guardarDatos(self, objeto, nombre, cantidad):
        medida = Medida(nombre, cantidad)
        if objeto == 1:
            self.textoVariable1.setText(nombre)
            self.textoValor1.setText(cantidad)
            self.texto_valor_litros1 = QLabel('{:.3f}'.format(medida.valorEquivalente))
            self.textoValorEquivalente1.setText('{:.3f}'.format(medida.valorEquivalente))
            self.medida1 = medida
        else:
            self.textoVariable2.setText(nombre)
            self.textoValor2.setText(cantidad)
            self.texto_valor_litros2 = QLabel('{:.3f}'.format(medida.valorEquivalente))
            self.textoValorEquivalente2.setText('{:.3f}'.format(medida.valorEquivalente))
            self.medida2 = medida


    #FUNCION QUE COMPARA LOS DATOS INGRESADOS EN BASE A LA TRANSFORMACION DADA Y MODIFICA EL SIGNO EN PANTALLA EN BASE
    #AL RESULTADO
    def comparar(self, medida1, medida2):
        if medida1.valorEquivalente < medida2.valorEquivalente:
            comparacion = "<"
        elif medida1.valorEquivalente > medida2.valorEquivalente:
            comparacion = ">"
        else:
            comparacion = "="
        self.signoComparacion.setText(comparacion)

   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(app.exec())
