import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

# Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
import numpy as np

def matplotWindow(data):

    root = tkinter.Tk()
    root.wm_title("Sorting Algorithms Time Complexity")
    root.geometry("1000x600")
    # root.eval('tk::PlaceWindow . center')

    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    ax = fig.add_subplot()
    # line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
    # data = {'milk': 60, 'water': 10}
    names = list(data.keys())
    values = list(data.values())

    ax.bar(range(len(data)), values, tick_label=names)
    ax.set_xlabel("Algorithms")
    ax.set_ylabel("time [ms]")

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()

    # pack_toolbar=False will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()

    # canvas.mpl_connect(
    #     "key_press_event", lambda event: print(f"you pressed {event.key}"))
    # canvas.mpl_connect("key_press_event", key_press_handler)

    button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)

    # slider_update = tkinter.Scale(root, from_=1, to=5, orient=tkinter.HORIZONTAL,
    #                             command=update_frequency, label="Frequency [Hz]")

    # Packing order is important. Widgets are processed sequentially and if there
    # is no space left, because the window is too small, they are not displayed.
    # The canvas is rather flexible in its size, so we pack it last which makes
    # sure the UI controls are displayed as long as possible.
    button_quit.pack(side=tkinter.BOTTOM)
    # slider_update.pack(side=tkinter.BOTTOM)
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

    tkinter.mainloop()
    
# matplotWindow({"Insertion Sort":6.5,"Bubble Sort": 7})