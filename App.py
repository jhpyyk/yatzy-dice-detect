import tkinter
import PIL.Image, PIL.ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Detection import Detection
from Probabilities import Probabilities
import numpy as np

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        window.configure(bg='#333333')

        self.detection = Detection()
        self.probabilities = Probabilities()
        self.throws_left = 3
        self.dice = np.zeros(5)
        self.prob_arr = self.probabilities.calc_probabilities(self.dice, self.throws_left)

        self.left_frame = tkinter.Frame(background='#333333')
        self.right_frame = tkinter.Frame(background='#333333')

        self.fig = plt.figure(figsize=(6,8))
        self.fig.set_tight_layout(True)
        self.prob_plot = self.fig.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(self.fig, master = self.left_frame)
        # placing the canvas on the Tkinter window
        self.plot_canvas.get_tk_widget().pack(side='top')
        self.plot_labels = ['Ones',
                            'Twos',
                            'Threes',
                            'Fours',
                            'Fives',
                            'Sixes',
                            'Pair',
                            'Two Pairs',
                            'Three-of-a-kind',
                            'Four-of-a-kind',
                            'Small Straight',
                            'Large Straight',
                            'Full House',
                            'Chance',
                            'Yatzy']

        # Create a canvas that can fit the above video source size
        self.video_canvas = tkinter.Canvas(self.right_frame,
                                           width = self.detection.video.width,
                                           height = self.detection.video.height)
        self.video_canvas.pack(side='top')

        self.btn_next_throw = tkinter.Button(self.right_frame,
                                           text="Next throw",
                                           width=20,
                                           command=self.next_throw)

        self.btn_next_throw.pack(side='bottom', pady=20)

        self.label_throws = tkinter.Label(self.right_frame, text='Throws left: 3')
        self.label_throws.pack(side='bottom', pady=20)

        self.left_frame.pack(side='left')
        self.right_frame.pack(side='right')

        # update() will be called every delay milliseconds
        self.delay = 33
        self.update()

        self.window.mainloop()

    def update(self):
        img = self.detection.get_img()

        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
        self.video_canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.prob_plot.clear()
        bars = self.prob_plot.barh(y=self.plot_labels, width = self.prob_arr)
        self.prob_plot.bar_label(bars, labels=[f'{x:.2%}' for x in bars.datavalues])
        self.prob_plot.invert_yaxis()
        self.prob_plot.set_xlim(0, 1.2)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.plot_canvas.draw()

        self.window.after(self.delay, self.update)

    def next_throw(self):
        self.throws_left = self.throws_left -1
        if (self.throws_left == 0):
            self.throws_left = 3

        self.label_throws.configure(text=f'Throws left: {self.throws_left}')
        self.dice = self.detection.get_dice()
        self.prob_arr = self.probabilities.calc_probabilities(self.dice, self.throws_left)
 
# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter")