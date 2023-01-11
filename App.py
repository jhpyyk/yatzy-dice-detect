import tkinter
import PIL.Image, PIL.ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Detection import Detection
from Probabilities import Probabilities
import numpy as np
from threading import Thread
import time

class App:
    def __init__(self, window, window_title):
        #Initiate window
        self.window = window
        self.window.title(window_title)
        window.configure(bg='#333333')
        self.left_frame = tkinter.Frame(background='#333333')
        self.right_frame = tkinter.Frame(background='#333333')

        # Initiate dice detection and probability calculator
        self.detection = Detection()
        self.probabilities = Probabilities()
        self.throws_left = 3
        self.dice = np.zeros(5)
        self.prob_arr = self.probabilities.calc_probabilities(self.dice, self.throws_left)

        # Initiate plot
        self.fig = plt.figure(figsize=(6,8))
        self.fig.set_tight_layout(True)
        self.prob_plot = self.fig.add_subplot(111)
        self.plot_canvas = FigureCanvasTkAgg(self.fig, master = self.left_frame)
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
        self.create_plot()

        # Initiate video canvas
        self.video_canvas = tkinter.Canvas(self.right_frame,
                                           width = self.detection.video.width,
                                           height = self.detection.video.height)
        self.video_canvas.pack(side='top')

        # Initiate next throw button
        self.btn_end_turn = tkinter.Button(self.right_frame,
                                           text="End turn",
                                           width=20,
                                           command=self.end_turn)

        self.btn_end_turn.pack(side='bottom', pady=20)

        # Initiate next throw button
        self.btn_throw = tkinter.Button(self.right_frame,
                                           text="Throw",
                                           width=20,
                                           command=self.throw)

        self.btn_throw.pack(side='bottom', pady=20)

        # Initiate throws left label
        self.label_throws = tkinter.Label(self.right_frame, text='Throws left: 3')
        self.label_throws.pack(side='bottom', pady=20)

        # Initiate calculation in x label
        self.label_calc_text = tkinter.Label(self.right_frame, text='')
        self.label_calc_text.pack(side='bottom', pady=20)

        # Pack the frames into the window
        self.left_frame.pack(side='left')
        self.right_frame.pack(side='right')

        # update() will be called every delay milliseconds
        self.delay = 33
        self.update()

        self.window.mainloop()

    # Update loop
    def update(self):
        self.create_video_frame()
        self.window.after(self.delay, self.update)

    # Next throw button function
    def throw(self):
        counter_thread = Thread(target=self.throw_loop)
        counter_thread.start()

    def throw_loop(self):
        seconds = 5
        while (seconds > 0):
            self.label_calc_text.configure(text=f'Calculating new odds in {seconds}')
            self.label_calc_text.update()
            time.sleep(1)
            seconds -= 1
        self.label_calc_text.configure(text='')
        self.throws_left = self.throws_left -1
        self.label_throws.configure(text=f'Throws left: {self.throws_left}')
        self.calculate()

    def end_turn(self):
        self.throws_left = 3
        self.calculate()
        self.label_throws.configure(text=f'Throws left: {self.throws_left}')


    # Get videoframe and put it to the canvas
    def create_video_frame(self):
        img = self.detection.get_img()
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
        self.video_canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

    # Calculate probabilities for the plot
    def calculate(self):
        self.dice = self.detection.get_dice()
        self.prob_arr = self.probabilities.calc_probabilities(self.dice, self.throws_left)
        self.create_plot()

    # Create the plot and draw it on the canvas
    def create_plot(self):
        self.prob_plot.clear()
        bars = self.prob_plot.barh(y=self.plot_labels, width = self.prob_arr)
        self.prob_plot.bar_label(bars, labels=[f'{x:.2%}' for x in bars.datavalues])
        self.prob_plot.invert_yaxis()
        self.prob_plot.set_xlim(0, 1.2)
        throws_s = "s"
        if (self.throws_left == 1):
            throws_s = "" 
        self.prob_plot.title.set_text(f"Probabilities with {self.throws_left} throw{throws_s}")
        self.plot_canvas.draw()

 
# Create a window and pass it to the Application object
App(tkinter.Tk(), "Yatzy odds")