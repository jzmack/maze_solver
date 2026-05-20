from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver")
        self.canvas = Canvas(master=self.root_widget, bg="white",height=self.height, width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

def main():
    app_window = Window(800, 600)
    app_window.wait_for_close()

if __name__ == "__main__":
    main()
    