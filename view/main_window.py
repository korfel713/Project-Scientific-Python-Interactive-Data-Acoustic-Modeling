from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QLabel, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("RT60 Analyzer")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        #buttons
        self.load_button = QPushButton("Load Audio File")
        self.load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_button)

        #label results
        self.results_label = QLabel("Analysis Results Will Appear Here")
        self.layout.addWidget(self.results_label)

        #plot canvas
        self.plot_canvas = FigureCanvas(Figure(figsize=(8, 6)))
        self.layout.addWidget(self.plot_canvas)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Audio Files (*.wav *.mp3 *.aac)")
        if file_path:
            self.controller.handle_file(file_path)

    def display_results(self, results):
        self.results_label.setText(results)

    def plot_waveform(self, time, amplitude):
        ax = self.plot_canvas.figure.subplots()
        ax.clear()
        ax.plot(time, amplitude, label="Waveform")
        ax.set_title("Waveform")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.legend()
        self.plot_canvas.draw()
