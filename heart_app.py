import sys
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Plot3D(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сердечко на PyQt5")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)

        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)
        self.plot_graph()

    def f1(self, x, y):
        denominator = (80 / (80 * x**2 + 9 * y**2))**(1 / 3)
        discriminant = 1 - 4 * denominator**2 * (x**2 + (9 / 4) * y**2 - 1)
        if discriminant < 0:
            return np.nan
        return (1 + np.sqrt(discriminant)) / (2 * denominator)

    def f2(self, x, y):
        denominator = (80 / (80 * x**2 + 9 * y**2))**(1 / 3)
        discriminant = 1 - 4 * denominator**2 * (x**2 + (9 / 4) * y**2 - 1)
        if discriminant < 0:
            return np.nan
        return (1 - np.sqrt(discriminant)) / (2 * denominator)

    def plot_graph(self):
        ax = self.canvas.figure.add_subplot(111, projection="3d")
        
        u = np.linspace(-1.2, 1.2, 500)
        v = np.linspace(-1.2, 1.2, 500)
        x, y = np.meshgrid(u, v)

        z1 = np.vectorize(self.f1)(x, y)
        z2 = np.vectorize(self.f2)(x, y)

        ax.plot_surface(x, y, z1, cmap="viridis",  alpha=0.7)
        ax.plot_surface(x, y, z2, cmap="plasma",  alpha=0.7)

        ax.set_title("Тут можно подписать график")
        # ax.set_xlabel("X")
        # ax.set_ylabel("Y")
        # ax.set_zlabel("Z")
        ax.view_init(20, 90)

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Plot3D()
    window.show()
    sys.exit(app.exec_())
