import sys
import qrcode
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog


class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Generator")
        self.setFixedSize(400, 550)

        self.text_entry = QLineEdit(self)
        self.text_entry.setPlaceholderText("Ingresar texto para generar el QR code:")
        self.text_entry.setGeometry(50, 50, 300, 50)

        self.qr_code_label = QLabel(self)
        self.qr_code_label.setAlignment(Qt.AlignCenter)
        self.qr_code_label.setGeometry(50, 130, 300, 300)

        self.generate_button = QPushButton("Generar QR", self)
        self.generate_button.setGeometry(130, 450, 140, 40)
        self.generate_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.generate_button.clicked.connect(self.generate_qr_code)

        self.export_button = QPushButton("Exportar", self)
        self.export_button.setGeometry(130, 500, 140, 40)
        self.export_button.setStyleSheet("background-color: #008CBA; color: white;")
        self.export_button.clicked.connect(self.export_image)

    def generate_qr_code(self):
        text = self.text_entry.text()
        qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
        qr_code.add_data(text)
        qr_code.make(fit=True)
        qr_code_image = qr_code.make_image(fill_color="black", back_color="white")
        qr_code_image.save("qr_code.png")
        pixmap = QPixmap("qr_code.png")
        self.qr_code_label.setPixmap(pixmap)

    def export_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar imagen", "", "Images (*.png *.xpm *.jpg)",
                                                   options=options)
        if file_name:
            self.qr_code_label.pixmap().save(file_name, "PNG")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qr_code_generator = QRCodeGenerator()
    qr_code_generator.show()
    sys.exit(app.exec_())
