# Form implementation generated from reading ui file 'd:\SYSTOCK\SYSTOCK\DESARROLLO\python\SYS-Systock\app\ui\VentasCredito.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentasCredito(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1422, 1073)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Contenedor = QtWidgets.QWidget(parent=Form)
        self.Contenedor.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: white; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  rgb(50, 50, 50); /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f2f2f2; /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Fondo blanco */\n"
"    border: none; /* Sin bordes visibles */\n"
"    padding: 4px; /* Espaciado interno entre el texto y los bordes */\n"
"    margin-right: 5px; /* Espaciado externo solo a la derecha */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    color: black; /* Texto negro */\n"
"    text-align: left; /* Texto alineado a la izquierda */\n"
"    font-size: 18px; /* Tamaño del texto */\n"
"}\n"
"\n"
"/* Cuando el QLineEdit está enfocado (se está escribiendo) */\n"
"QLineEdit:focus {\n"
"    background-color: rgb(230, 230, 250); /* Color de fondo cuando el campo está activo */\n"
"    border: 1px solid rgb(0, 0, 0); /* Borde negro al estar activo */\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 20px; /* Tamaño de fuente */\n"
"    color:  black; /* Color del texto */\n"
"    margin-right: 10px; /* Espaciado a la derecha */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    text-align: left; /* Alineación del texto a la izquierda */\n"
"}\n"
"QTableWidget {\n"
"    border: none;\n"
"    background-color: #ffffff; /* Fondo blanco para la tabla */\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave alrededor de la tabla */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"    transition: background-color 0.3s ease; /* Suavizado de transición de color de fondo */\n"
"    pointer-events: none; /* Desactiva la interacción con las celdas (como editar) */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aad4ff; /* Color azul claro para celdas seleccionadas */\n"
"    color: black; /* Texto negro para celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none; \n"
"    background-color: #f2f2f2; \n"
"    font-weight: normal; /* No negritas */\n"
"    text-align: center; /* Centrado del texto en los encabezados */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave para los encabezados */\n"
"}\n"
"\n"
"QHeaderView::section:focus {\n"
"    background-color: #f2f2f2; /* Sin color de fondo cuando está en foco */\n"
"    border: none; /* Sin borde cuando está en foco */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    border: none; /* Sin borde cuando las celdas tienen el foco */\n"
"    background-color: #f2f2f2; /* Mantener el fondo sin color azul */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #f2f2f2;\n"
"    border: none;\n"
"    font-weight: normal; /* No negritas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"/* Personalización de la barra de desplazamiento */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    width: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-height: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    height: 0px; /* Sin altura para los botones */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    height: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-width: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    width: 0px; /* Sin ancho para los botones */\n"
"}\n"
"\n"
"\n"
"")
        self.Contenedor.setObjectName("Contenedor")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Contenedor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Contenido = QtWidgets.QStackedWidget(parent=self.Contenedor)
        self.Contenido.setStyleSheet("margin-left:10px;\n"
"border-radius:15px;\n"
"background-color: #f2f2f2; \n"
"")
        self.Contenido.setObjectName("Contenido")
        self.ContenidoPage1 = QtWidgets.QWidget()
        self.ContenidoPage1.setObjectName("ContenidoPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContenidoPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(parent=self.ContenidoPage1)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.InputMarca = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputMarca.sizePolicy().hasHeightForWidth())
        self.InputMarca.setSizePolicy(sizePolicy)
        self.InputMarca.setMinimumSize(QtCore.QSize(250, 50))
        self.InputMarca.setMaximumSize(QtCore.QSize(250, 50))
        self.InputMarca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputMarca.setObjectName("InputMarca")
        self.gridLayout_2.addWidget(self.InputMarca, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 1, 0, 1, 1)
        self.LabelVentasA = QtWidgets.QLabel(parent=self.widget_3)
        self.LabelVentasA.setStyleSheet("#LabelVentasA {\n"
"    font-weight: bold; /* Negrita */\n"
"    font-size: 34px; /* Tamaño de fuente */\n"
"}\n"
"")
        self.LabelVentasA.setObjectName("LabelVentasA")
        self.gridLayout_2.addWidget(self.LabelVentasA, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 3, 1, 1)
        self.BtnEliminar = QtWidgets.QPushButton(parent=self.widget_3)
        self.BtnEliminar.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: red; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\SYSTOCK\\SYSTOCK\\DESARROLLO\\python\\SYS-Systock\\app\\ui\\../../assets/iconos/eliminar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BtnEliminar.setIcon(icon)
        self.BtnEliminar.setIconSize(QtCore.QSize(30, 30))
        self.BtnEliminar.setObjectName("BtnEliminar")
        self.gridLayout_2.addWidget(self.BtnEliminar, 5, 6, 1, 1)
        self.InputDomicilio = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputDomicilio.sizePolicy().hasHeightForWidth())
        self.InputDomicilio.setSizePolicy(sizePolicy)
        self.InputDomicilio.setMinimumSize(QtCore.QSize(250, 50))
        self.InputDomicilio.setMaximumSize(QtCore.QSize(250, 50))
        self.InputDomicilio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputDomicilio.setObjectName("InputDomicilio")
        self.gridLayout_2.addWidget(self.InputDomicilio, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 4, 1, 1)
        self.InputNombre = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputNombre.sizePolicy().hasHeightForWidth())
        self.InputNombre.setSizePolicy(sizePolicy)
        self.InputNombre.setMinimumSize(QtCore.QSize(250, 50))
        self.InputNombre.setMaximumSize(QtCore.QSize(250, 50))
        self.InputNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputNombre.setObjectName("InputNombre")
        self.gridLayout_2.addWidget(self.InputNombre, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget_3)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 6, 1, 1)
        self.InputCantidad = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCantidad.sizePolicy().hasHeightForWidth())
        self.InputCantidad.setSizePolicy(sizePolicy)
        self.InputCantidad.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCantidad.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCantidad.setObjectName("InputCantidad")
        self.gridLayout_2.addWidget(self.InputCantidad, 3, 4, 1, 1)
        self.InputPrecioUnitario = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputPrecioUnitario.sizePolicy().hasHeightForWidth())
        self.InputPrecioUnitario.setSizePolicy(sizePolicy)
        self.InputPrecioUnitario.setMinimumSize(QtCore.QSize(250, 50))
        self.InputPrecioUnitario.setMaximumSize(QtCore.QSize(250, 50))
        self.InputPrecioUnitario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputPrecioUnitario.setObjectName("InputPrecioUnitario")
        self.gridLayout_2.addWidget(self.InputPrecioUnitario, 3, 6, 1, 1)
        self.InputCodigo = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCodigo.sizePolicy().hasHeightForWidth())
        self.InputCodigo.setSizePolicy(sizePolicy)
        self.InputCodigo.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCodigo.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCodigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCodigo.setObjectName("InputCodigo")
        self.gridLayout_2.addWidget(self.InputCodigo, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(parent=self.ContenidoPage1)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TablaVentasCredito = QtWidgets.QTableWidget(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TablaVentasCredito.sizePolicy().hasHeightForWidth())
        self.TablaVentasCredito.setSizePolicy(sizePolicy)
        self.TablaVentasCredito.setMinimumSize(QtCore.QSize(845, 300))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TablaVentasCredito.setFont(font)
        self.TablaVentasCredito.setStyleSheet("\n"
"QTableWidget {\n"
"    border: none;\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave alrededor de la tabla */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"    font-size: 18px; /* Tamaño de letra */\n"
"    transition: background-color 0.3s ease; /* Suavizado de transición de color de fondo */\n"
"    pointer-events: none; /* Desactiva la interacción con las celdas (como editar) */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aad4ff; /* Color azul claro para celdas seleccionadas */\n"
"    color: black; /* Texto negro para celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none; \n"
"    background-color: #f2f2f2; \n"
"    font-size: 18px; /* Tamaño de letra */\n"
"    font-weight: normal; /* No negritas */\n"
"    text-align: center; /* Centrado del texto en los encabezados */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave para los encabezados */\n"
"}\n"
"\n"
"QHeaderView::section:focus {\n"
"    background-color: #f2f2f2; /* Sin color de fondo cuando está en foco */\n"
"    border: none; /* Sin borde cuando está en foco */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    border: none; /* Sin borde cuando las celdas tienen el foco */\n"
"    background-color: #f2f2f2; /* Mantener el fondo sin color azul */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #f2f2f2;\n"
"    font-size: 23px;\n"
"    border: none;\n"
"    font-weight: normal; /* No negritas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"/* Personalización de la barra de desplazamiento */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    width: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"    margin: 0px 2px 0px 0px; /* Un pequeño margen para el desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-height: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    height: 0px; /* Sin altura para los botones */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    height: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"    margin: 0px 0px 2px 0px; /* Un pequeño margen para el desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-width: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"")
        self.TablaVentasCredito.setObjectName("TablaVentasCredito")
        self.TablaVentasCredito.setColumnCount(7)
        self.TablaVentasCredito.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaVentasCredito.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.TablaVentasCredito.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaVentasCredito.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaVentasCredito.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaVentasCredito.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaVentasCredito.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaVentasCredito.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TablaVentasCredito.setHorizontalHeaderItem(6, item)
        self.verticalLayout_3.addWidget(self.TablaVentasCredito, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(parent=self.ContenidoPage1)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.InputTelefonoCli = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputTelefonoCli.sizePolicy().hasHeightForWidth())
        self.InputTelefonoCli.setSizePolicy(sizePolicy)
        self.InputTelefonoCli.setMinimumSize(QtCore.QSize(250, 50))
        self.InputTelefonoCli.setMaximumSize(QtCore.QSize(250, 50))
        self.InputTelefonoCli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputTelefonoCli.setObjectName("InputTelefonoCli")
        self.gridLayout_4.addWidget(self.InputTelefonoCli, 2, 3, 1, 1)
        self.InputDireccion = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputDireccion.sizePolicy().hasHeightForWidth())
        self.InputDireccion.setSizePolicy(sizePolicy)
        self.InputDireccion.setMinimumSize(QtCore.QSize(250, 50))
        self.InputDireccion.setMaximumSize(QtCore.QSize(250, 50))
        self.InputDireccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputDireccion.setObjectName("InputDireccion")
        self.gridLayout_4.addWidget(self.InputDireccion, 2, 2, 1, 1)
        self.LabelTotal = QtWidgets.QLabel(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelTotal.sizePolicy().hasHeightForWidth())
        self.LabelTotal.setSizePolicy(sizePolicy)
        self.LabelTotal.setMinimumSize(QtCore.QSize(250, 50))
        self.LabelTotal.setMaximumSize(QtCore.QSize(250, 50))
        self.LabelTotal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.LabelTotal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LabelTotal.setObjectName("LabelTotal")
        self.gridLayout_4.addWidget(self.LabelTotal, 4, 3, 1, 1)
        self.LabelSubtotal = QtWidgets.QLabel(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelSubtotal.sizePolicy().hasHeightForWidth())
        self.LabelSubtotal.setSizePolicy(sizePolicy)
        self.LabelSubtotal.setMinimumSize(QtCore.QSize(250, 50))
        self.LabelSubtotal.setMaximumSize(QtCore.QSize(250, 50))
        self.LabelSubtotal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.LabelSubtotal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LabelSubtotal.setObjectName("LabelSubtotal")
        self.gridLayout_4.addWidget(self.LabelSubtotal, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 4, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_31 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 0, 0, 1, 1)
        self.InputCedula = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputCedula.sizePolicy().hasHeightForWidth())
        self.InputCedula.setSizePolicy(sizePolicy)
        self.InputCedula.setMinimumSize(QtCore.QSize(250, 50))
        self.InputCedula.setMaximumSize(QtCore.QSize(250, 50))
        self.InputCedula.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputCedula.setObjectName("InputCedula")
        self.gridLayout_4.addWidget(self.InputCedula, 2, 5, 1, 1)
        self.InputNombreCli = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputNombreCli.sizePolicy().hasHeightForWidth())
        self.InputNombreCli.setSizePolicy(sizePolicy)
        self.InputNombreCli.setMinimumSize(QtCore.QSize(250, 50))
        self.InputNombreCli.setMaximumSize(QtCore.QSize(250, 50))
        self.InputNombreCli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputNombreCli.setObjectName("InputNombreCli")
        self.gridLayout_4.addWidget(self.InputNombreCli, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 3, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.label_12 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 1, 1, 1)
        self.BtnGenerarVentaCredito = QtWidgets.QPushButton(parent=self.widget_4)
        self.BtnGenerarVentaCredito.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BtnGenerarVentaCredito.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}")
        self.BtnGenerarVentaCredito.setObjectName("BtnGenerarVentaCredito")
        self.gridLayout_4.addWidget(self.BtnGenerarVentaCredito, 4, 5, 1, 1)
        self.InputMaxCredito = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputMaxCredito.sizePolicy().hasHeightForWidth())
        self.InputMaxCredito.setSizePolicy(sizePolicy)
        self.InputMaxCredito.setMinimumSize(QtCore.QSize(250, 50))
        self.InputMaxCredito.setMaximumSize(QtCore.QSize(250, 50))
        self.InputMaxCredito.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputMaxCredito.setObjectName("InputMaxCredito")
        self.gridLayout_4.addWidget(self.InputMaxCredito, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 3, 1, 1)
        self.InputApellidoCli = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputApellidoCli.sizePolicy().hasHeightForWidth())
        self.InputApellidoCli.setSizePolicy(sizePolicy)
        self.InputApellidoCli.setMinimumSize(QtCore.QSize(250, 50))
        self.InputApellidoCli.setMaximumSize(QtCore.QSize(250, 50))
        self.InputApellidoCli.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputApellidoCli.setObjectName("InputApellidoCli")
        self.gridLayout_4.addWidget(self.InputApellidoCli, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 2, 1, 1)
        self.LimitePagoBox = QtWidgets.QComboBox(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LimitePagoBox.sizePolicy().hasHeightForWidth())
        self.LimitePagoBox.setSizePolicy(sizePolicy)
        self.LimitePagoBox.setMinimumSize(QtCore.QSize(250, 50))
        self.LimitePagoBox.setStyleSheet("QComboBox {\n"
"    background-color: white; /* Fondo blanco */\n"
"    border: none; /* Sin borde */\n"
"    color: black; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes redondeados */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    height: 40px; /* Altura del combo box */\n"
"    margin-top: 20px; /* Espaciado superior */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde */\n"
"    width: 20px; /* Tamaño del botón */\n"
"    /* No se define la flecha, por lo que se elimina */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    cursor: pointer; /* Cursor de mano */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white; /* Fondo del menú desplegable */\n"
"    border: none; /* Sin borde */\n"
"    color: black; /* Color del texto en las opciones */\n"
"    selection-background-color: rgb(106, 106, 106); /* Fondo gris claro al seleccionar */\n"
"    selection-color: white; /* Texto blanco al seleccionar */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"}\n"
"\n"
"")
        self.LimitePagoBox.setObjectName("LimitePagoBox")
        self.gridLayout_4.addWidget(self.LimitePagoBox, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Contenido.addWidget(self.ContenidoPage1)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.horizontalLayout.addWidget(self.Contenedor)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Codigo"))
        self.label_8.setText(_translate("Form", "Valor Domicilio"))
        self.label_30.setText(_translate("Form", "Productos"))
        self.LabelVentasA.setText(_translate("Form", "Vta Crédito"))
        self.label_6.setText(_translate("Form", "Marca"))
        self.BtnEliminar.setText(_translate("Form", "   Eliminar"))
        self.label_7.setText(_translate("Form", "Cantidad"))
        self.label.setText(_translate("Form", "Precio Unitario"))
        self.label_5.setText(_translate("Form", "Producto"))
        item = self.TablaVentasCredito.verticalHeaderItem(0)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(1)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(2)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(3)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(4)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(5)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(6)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(7)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(8)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(9)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(10)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(11)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(12)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(13)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaVentasCredito.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaVentasCredito.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaVentasCredito.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.TablaVentasCredito.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Producto"))
        item = self.TablaVentasCredito.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Marca"))
        item = self.TablaVentasCredito.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Categoria"))
        item = self.TablaVentasCredito.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Cantidad"))
        item = self.TablaVentasCredito.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Precio"))
        item = self.TablaVentasCredito.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Total"))
        self.LabelTotal.setText(_translate("Form", "$"))
        self.LabelSubtotal.setText(_translate("Form", "$"))
        self.label_4.setText(_translate("Form", "Nombre:"))
        self.label_15.setText(_translate("Form", "Total"))
        self.label_2.setText(_translate("Form", "Cedula De Ciudadania"))
        self.label_13.setText(_translate("Form", "Max. Credito"))
        self.label_14.setText(_translate("Form", "Subtotal"))
        self.label_12.setText(_translate("Form", "Fecha limite de Pago"))
        self.label_10.setText(_translate("Form", "Apellido:"))
        self.BtnGenerarVentaCredito.setText(_translate("Form", "Generar Venta a Credito"))
        self.label_11.setText(_translate("Form", "Teléfono:"))
        self.label_9.setText(_translate("Form", "Dirección:"))
