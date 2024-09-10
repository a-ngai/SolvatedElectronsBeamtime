from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabWidgetApp = Ui_MainWindow()
    w = MainWindow()

    tabWidgetApp.setupUi(w)

    sys.exit(app.exec())

