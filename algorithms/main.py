from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.mergeSort import mergeSort
from algorithms.heapSort import heapSort
from algorithms.quickSort import quickSort
from algorithms.radixSort import radixSort
from algorithms.bucketSort import bucketSort
from algorithms.countSort import countSort

from buttons.optionBox import OptionBox
import random
import math
import numpy as np
from easygui import msgbox

import pygame
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton
from pygame.rect import Rect

pygame.init()

SORTING_ALGOS = ["Insertion sort","Bubble sort","Merge Sort","Heap Sort",
                "Quick sort","Radix Sort","Bucket Sort","Counting Sort",
                "Quinsert Sort", "8.1.4 Sort"]
WIDTH, HEIGHT = 1100,680

# class that will have window screen 
class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = WHITE

    GREY_GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    REG_FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans',30)

    SIDE_PADDING = 100
    TOP_PADDING = 150


    def __init__(self,width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width,height))
        
        pygame.display.set_caption("Sortilizer")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PADDING) / (self.max_val-self.min_val))
        self.start_x = self.SIDE_PADDING // 2

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

# draw function to render everything on screen
def draw(draw_info, algoName, ascending,options,manager, time_delta):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algoName} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 ,5))

    controls = draw_info.REG_FONT.render("G - Generate New | Space - Sort | A - Ascend | D - Descend", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 ,40))

    sorting = draw_info.REG_FONT.render("I - Insertion | B - Bubble", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 ,65))

    options.draw(draw_info.window)
    draw_list(draw_info) 
    manager.update(time_delta)
    manager.draw_ui(draw_info.window)
    pygame.display.update()

# draw the numbers in the shape of rectangle bars
def draw_list(draw_info, color_positions={}, clearBG=False):
    lst = draw_info.lst

    if clearBG:
        clearRect = (draw_info.SIDE_PADDING//2, 
                    draw_info.TOP_PADDING, 
                    draw_info.width - draw_info.SIDE_PADDING,
                    draw_info.height - draw_info.TOP_PADDING)

        pygame.draw.rect(draw_info.window,draw_info.BACKGROUND_COLOR, clearRect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val-draw_info.min_val) * draw_info.block_height

        color = draw_info.GREY_GRADIENTS[i % 3] # different color for adjacent blocks
        
        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x,y,draw_info.block_width,draw_info.height))

    if clearBG:
        pygame.display.update()

# random number list generator
def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

# file input number generator
def generage_list_file(location):

    result = np.loadtxt(location)
    # print(result.tolist())
    return result

# main code
def main():
    run = True
    clock = pygame.time.Clock()

    n=30
    min_val = 1
    max_val = 100
    lst = generate_starting_list(n,min_val,max_val)

    sorting=False
    ascending=True

    sortingAlgorithm = insertionSort
    sortingAlgoName = "Insertion Sort"
    sortingAlgoGenerator = None

    draw_info = DrawInformation(WIDTH,HEIGHT,lst)

    options = OptionBox(
    draw_info.width/2-200, 100, 200, 30, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
    SORTING_ALGOS)

    manager = pygame_gui.UIManager((800, 600))

    file_selection_button = UIButton(relative_rect=Rect(draw_info.width/2, 100, 200, 30),
                                 manager=manager, text='Select File')

    # main loop to run pygame
    while run:
        time_delta = clock.tick(30) / 1000.0

        # check if sorting to load sequence of generator objects
        if sorting:
            try:
                next(sortingAlgoGenerator)
            except StopIteration:
                sorting = False
        else:
            # render objects to draw on screen
            draw(draw_info,sortingAlgoName,ascending, options,manager,time_delta)
        
        # get all events
        event_list = pygame.event.get()

        # optionBox event
        # choosing different options and operation based on their returned index
        selected_option = options.update(event_list)
        if selected_option >= 0 and not sorting:
            if selected_option == 0:
                sortingAlgoName = "Insertion Sort"
                sortingAlgorithm = insertionSort
        
            if selected_option == 1:
                sortingAlgoName = "Bubble Sort"
                sortingAlgorithm = bubbleSort          

            if selected_option == 2:
                sortingAlgoName = "Merge Sort"
                sortingAlgorithm = mergeSort  

            if selected_option == 3:
                sortingAlgoName = "Heap Sort"
                sortingAlgorithm = heapSort  

            if selected_option == 4:
                sortingAlgoName = "Quick Sort"
                sortingAlgorithm = bubbleSort  

            if selected_option == 5:
                sortingAlgoName = "Radix Sort"
                sortingAlgorithm = radixSort  

            if selected_option == 6:
                sortingAlgoName = "Bucket Sort"
                sortingAlgorithm = bucketSort  

            if selected_option == 7:
                sortingAlgoName = "Counting Sort"
                sortingAlgorithm = countSort  

            if selected_option == 8:
                sortingAlgoName = "Quinsert Sort"
                sortingAlgorithm = bubbleSort  

            if selected_option == 9:
                sortingAlgoName = "8.1.4 Sort"
                sortingAlgorithm = bubbleSort  
    
        for event in event_list:
            # exit event
            if event.type == pygame.QUIT:
                run = False

            # file input event
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == file_selection_button:
                        file_selection = UIFileDialog(rect=Rect(draw_info.width//2, 0, 300, 300), manager=manager, allow_picking_directories=True)

                    if event.ui_element == file_selection.ok_button:
                        # print(file_selection.current_file_path)
                        lst = generage_list_file(file_selection.current_file_path)
                        if lst.any():
                            draw_info.set_list(lst)
                            sorting=False
                            msgbox(msg=f"Input loaded successfully : {lst}", title="Loaded", ok_button="Close")

            # handle file input change
            manager.process_events(event)

            # if no key pressed skip
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_g:
                lst = generate_starting_list(n,min_val,max_val)
                draw_info.set_list(lst)
                sorting=False

            elif event.key == pygame.K_SPACE and sorting==False:
                sorting = True
                sortingAlgoGenerator = sortingAlgorithm(draw_info,draw_list,ascending)

            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif (event.key == pygame.K_i) and not sorting:
                sortingAlgoName = "Insertion Sort"
                sortingAlgorithm = insertionSort
                options.selected = 0

            elif (event.key == pygame.K_b) and not sorting:
                sortingAlgoName = "Bubble Sort"
                sortingAlgorithm = bubbleSort
                options.selected = 1

            elif (event.key == pygame.K_m) and not sorting:
                sortingAlgoName = "Merge Sort"
                sortingAlgorithm = mergeSort
                options.selected = 2

            elif (event.key == pygame.K_h) and not sorting:
                sortingAlgoName = "Heap Sort"
                sortingAlgorithm = heapSort
                options.selected = 3

            elif (event.key == pygame.K_q) and not sorting:
                sortingAlgoName = "Quick Sort"
                sortingAlgorithm = quickSort
                options.selected = 4

            elif (event.key == pygame.K_r) and not sorting:
                sortingAlgoName = "Radix Sort"
                sortingAlgorithm = radixSort
                options.selected = 5

            elif (event.key == pygame.K_x) and not sorting:
                sortingAlgoName = "Bucket Sort"
                sortingAlgorithm = bucketSort
                options.selected = 6

            elif (event.key == pygame.K_c) and not sorting:
                sortingAlgoName = "Count Sort"
                sortingAlgorithm = countSort
                options.selected = 7

    pygame.quit()



# run the main function of this file
if __name__ == "__main__":
    main()