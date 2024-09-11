import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QWidget, QLabel

class TabWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Widget Demo')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")
        self.tab_widget.addTab(self.tab3, "Tab 3")

        self.layout.addWidget(self.tab_widget)

        self.initTab1()
        self.initTab2()
        self.initTab3()

    def initTab1(self):
        layout = QVBoxLayout(self.tab1)
        label = QLabel("Content of Tab 1")
        layout.addWidget(label)

    def initTab2(self):
        layout = QVBoxLayout(self.tab2)
        label = QLabel("Content of Tab 2")
        layout.addWidget(label)

    def initTab3(self):
        layout = QVBoxLayout(self.tab3)
        label = QLabel("Content of Tab 3")
        layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabWidgetApp = TabWidgetApp()
    tabWidgetApp.show()
    sys.exit(app.exec())
