# # import sys
# # import threading
# # from PyQt5.QtCore import Qt
# # from PyQt5.QtGui import QMovie
# # from PyQt5.QtWidgets import QApplication, QLabel
# #
# # def gifff():
# #     while getattr(gif_thread, "do_run", True):
# #     app = QApplication(sys.argv)
# #     w = QLabel()
# #     w.setWindowFlags(Qt.FramelessWindowHint)  # transparent window
# #     w.setAttribute(Qt.WA_TranslucentBackground)
# #     w.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
# #
# #     movie = QMovie('gifka.gif')
# #     w.setMovie(movie)
# #     movie.start()
# #
# #
# # # center
# #     w.adjustSize()  # update w.rect() now
# #     w.move(1500, 900)
# #     w.show()
# #     sys.exit(app.exec_())
# # gifff()
# import os
# from threading import Thread
# from tkinter import Tk, Button, DISABLED, mainloop
# from playsound import playsound
#
#
# # class Player(Tk):                                     # объявление класса
# #     path = r'C:\Users\USER\Desktop\uu'                                # путь поиска музыки
# #     def __init__(self):
# #         super().__init__()                            # наледование нашим классом класса Tk
# #         self.initUI()                                 # вызов функции
# #
# #     def initUI(self):                                 # функция построения интерфейса
# #         self.play_button = Button(self, text="Запустить проигрыватель",
# #             command=self.run)                         # создаём кнопку при нажатии на которую происходит вызов функции self.run
# #         exit_button = Button(self, text="Выйти", command=self.quit) # кнопка выхода
# #         self.play_button.pack()                       # размещение кнопок в окне "смотри документацию tkinter"
# #         exit_button.pack()
# #
# #
# #     def run(self):
# #         self.play_button["state"] = DISABLED
# #         def play():                                   # создаём функцию для воспроизведения муз. файлов
# #             for sound in os.listdir(self.path):       # получаем список всех муз. файлов в директории
# #                 playsound('%s/%s' % (self.path, sound)) # вызов функции с параметрами
# #         thread = Thread(target=play)                    # создание потока
# #         thread.daemon = True                            # поток умрёт вместе с основным
# #         thread.start()                                  # запуск потока
# #
# #     def quit(self):
# #         quit()
# #
# # if __name__ == "__main__":
# #     player = Player()
# #     player.mainloop()
#
#
#
#
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.Qt import *
#
#
# # class WorkThread(QtCore.QThread):
# #     threadSignal = QtCore.pyqtSignal(int)
# #
# #     def __init__(self, numStart, numEnd):
# #         super().__init__()
# #         self.numStart = numStart
# #         self.numEnd = numEnd
# #         self.threadStop = False
# #
# #     def run(self):
# #         # имитируем какую-то работу в потоке
# #         for i in range(self.numStart, self.numEnd):
# #             self.msleep(100)
# #             if self.threadStop:
# #                 break
# #             self.threadSignal.emit(i)
# #         self.finished.emit()
# #
# #
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.thread = None
# #         self.movie = None
# #         self.numStart = 0
# #         self.numEnd = 1_000
# #
# #         self.centralWidget = QtWidgets.QWidget()
# #         self.centralWidget.setObjectName("centralWidget")
# #         self.setCentralWidget(self.centralWidget)
# #
# #         self.button = QPushButton(self)
# #         self.button.setObjectName("button")
# #         self.button.setCheckable(True)
# #         self.button.setIcon(QIcon('off.png'))
# #         self.button.setIconSize(QSize(70, 70))
# #         self.button.clicked.connect(self.button_clicked)
# #
# #         self.label = QtWidgets.QLabel(alignment=Qt.AlignCenter)
# #         self.label.setObjectName("label")
# #         self.layout = QGridLayout(self.centralWidget)
# #         self.layout.addWidget(self.label, 0, 0, 3, 1)
# #         self.layout.addWidget(self.button, 1, 1, 1, 1)
# #         self.layout.setColumnStretch(0, 1)
# #
# #     def button_clicked(self):
# #         if self.button.isChecked():
# #             self.button.setIcon(QIcon('on.png'))
# #             self.show_movie()
# #         else:
# #             self.button.setIcon(QIcon('off.png'))
# #             if self.thread: self.thread.threadStop = True
# #
# #     def show_movie(self):
# #         self.label_movie = QtWidgets.QLabel()
# #         self.label_movie.setAttribute(
# #             QtCore.Qt.WA_TranslucentBackground, True)
# #         self.label_movie.setWindowFlags(
# #             self.windowFlags() |
# #             QtCore.Qt.FramelessWindowHint |
# #             QtCore.Qt.WindowStaysOnTopHint
# #         )
# #         self.label.setText('Ожидайте заавершения операции ...')
# #         self.movie = QtGui.QMovie('loading.gif')  # тут ваша .gif
# #         self.label_movie.setMovie(self.movie)
# #         self.movie.start()
# #         self.label_movie.show()
# #
# #         if self.thread is None:
# #             self.thread = WorkThread(self.numStart, self.numEnd)
# #             self.thread.threadSignal.connect(self.on_threadSignal)
# #             self.thread.finished.connect(self.threadFinished)
# #             self.thread.start()
# #         else:
# #             self.label_movie.close()
# #             self.thread.terminate()
# #             self.thread = None
# #
# #     def on_threadSignal(self, num):
# #         self.label.setText(f'Ожидайте заавершения операции... {num}')
# #         self.numStart = num + 1
# #
# #     def threadFinished(self):
# #         self.movie.stop()
# #         self.label_movie.close()
# #         self.thread = None
# #         self.button.setIcon(QIcon('off.png'))
# #         if self.numStart + 1 == self.numEnd:
# #             self.numStart = 0
# #             self.button.click()
# #
# #     def closeEvent(self, event):
# #         if self.movie:
# #             self.movie.stop()
# #             self.label_movie.close()
# #         self.thread = None
# #
# #
# # Stylesheet = '''
# # #centralWidget {
# #     background-color: rgb(54, 54, 54);
# # }
# # #label {
# #     background-color: rgb(84, 74, 54);
# #     color: #D9AC00;
# #     font-size: 24px;
# # }
# # #button {
# #     border: rgb(0, 0, 0);
# # }
# # '''
# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     app.setStyle(QStyleFactory.create("fusion"))
# #     app.setStyleSheet(Stylesheet)
# #     w = MainWindow()
# #     w.resize(600, 400)
# #     w.show()
# #     sys.exit(app.exec_())
#
# import sys
# from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
# from PyQt6.QtGui import QMovie
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("GIF Player")
#
#         # Создаем виджет QLabel для отображения GIF
#         self.gif_label = QLabel(self)
#         self.gif_label.setMovie(QMovie("melkay.gif"))  # Укажите путь к вашему GIF
#
#         # Создаем кнопку для управления воспроизведением
#         self.button = QPushButton("Play/Pause", self)
#         self.button.setCheckable(True)  # Делаем кнопку переключаемой
#         self.button.clicked.connect(self.toggle_gif)
#
#         # Устанавливаем макет
#         layout = QVBoxLayout()
#         layout.addWidget(self.gif_label)
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#
#     def toggle_gif(self):
#         if self.button.isChecked():
#             self.gif_label.movie().start()  # Начинаем воспроизведение GIF
#             self.button.setText("Pause")  # Меняем текст кнопки на "Пауза"
#         else:
#             self.gif_label.movie().close()  # Останавливаем воспроизведение GIF
#             self.button.setText("Play")  # Меняем текст кнопки на "Играть"
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())
# mass()
# print()