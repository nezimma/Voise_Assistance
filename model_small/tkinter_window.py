import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно с Кнопками")
        self.setGeometry(100, 100, 300, 300)

        # Основной виджет и горизонтальный слой
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)  # Горизонтальный компоновщик

        # Кнопка с изображением модели
        self.model_button = QPushButton(self)
        self.model_button.setText("Модель")
        self.model_button.setIcon(QIcon("path/to/your/model_image.png"))  # путь к изображению модели
        self.model_button.setIconSize(self.model_button.size() * 0.8)  # Устанавливаем размер иконки
        self.model_button.setStyleSheet("font-size: 24px;")  # Увеличиваем размер шрифта
        self.model_button.setFixedSize(150, 200)  # Фиксированный размер кнопки
        layout.addWidget(self.model_button)

        # Кнопка с значком Telegram
        self.telegram_button = QPushButton(self)
        self.telegram_button.setText("Telegram")
        self.telegram_button.setIcon(QIcon("path/to/your/telegram_icon.png"))  # путь к значку Telegram
        self.telegram_button.setIconSize(self.telegram_button.size() * 0.8)  # Устанавливаем размер иконки
        self.telegram_button.setStyleSheet("font-size: 24px;")  # Увеличиваем размер шрифта
        self.telegram_button.setFixedSize(150, 200)  # Фиксированный размер кнопки
        layout.addWidget(self.telegram_button)

        # Соединяем кнопку с функцией обработки нажатия
        self.telegram_button.clicked.connect(self.open_input_dialog)

        # Устанавливаем выравнивание по центру
        layout.setAlignment(self.model_button, Qt.AlignCenter)
        layout.setAlignment(self.telegram_button, Qt.AlignCenter)

    def open_input_dialog(self):
        text, ok = QInputDialog.getText(self, 'Введите текст', 'Введите сообщение:')

        if ok and text:
            QMessageBox.information(self, 'Ваш текст', f'Вы ввели: {text}')
        elif ok:
            QMessageBox.warning(self, 'Предупреждение', 'Вы ничего не ввели.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
