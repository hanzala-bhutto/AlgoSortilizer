from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.mergeSort import mergeSort
from algorithms.heapSort import heapSort
from algorithms.quickSort import quickSort
from algorithms.radixSort import radixSort
from algorithms.bucketSort import bucketSort
from algorithms.countSort import countSort
from algorithms.quinsertSort import quinsertSort
from algorithms.rangeQuery import rangeQuery

from utils.checkInteger import checkInteger
from utils.info import infoAlgoMsg
from utils.constants import *
from utils.plot import matplotWindow

from buttons.Button import Button
from buttons.optionBox import OptionBox

import time
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

# class that will have window screen 
class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    GREY = 150,150,150
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
def draw(draw_info, algoName, ascending,optionsAlgo,optionsFPS,manager,infoButton,plotButton, sorting,sortedd,time_delta):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algoName} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 ,5))

    controls = draw_info.REG_FONT.render("G - Generate New Array | R - Reset Array | Space - Sort | A - Ascend | D - Descend", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 ,40))

    sort = draw_info.REG_FONT.render("1 - Insertion | 2 - Bubble | 3 - Merge | 4 - Heap | 5 - Quick | 6 - Radix | 7 - Bucket | 8 - Count | 9 - Quinsert", 1, draw_info.BLACK)
    draw_info.window.blit(sort, (draw_info.width/2 - sort.get_width()/2 ,65))

    timer_draw(draw_info,sorting,sortedd)
    optionsFPS.draw(draw_info.window)
    optionsAlgo.draw(draw_info.window)
    infoButton.draw(draw_info.window)
    plotButton.draw(draw_info.window)
    draw_list(draw_info) 
    manager.update(time_delta)
    manager.draw_ui(draw_info.window)
    pygame.display.update()

def drawRange(draw_info, color_positions={},clearBG=False):
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

# timer count down to calculate the time comlexity
def timer_draw(draw_info,sorting,sortedd=False):
    if sorting:
        global counting_string
        draw_info.window.fill(pygame.Color("white"), (draw_info.width-180, 15, 200, 30))

        counting_time = pygame.time.get_ticks() - start_time

        # change milliseconds into seconds
        counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)

        counting_string = "%s ms" % (counting_seconds)

        counting_text = draw_info.REG_FONT.render(str(counting_string), 1, (draw_info.GREEN),None)
        draw_info.window.blit(counting_text,(draw_info.width-150,15))

    if sortedd:
        counting_text = draw_info.REG_FONT.render(str(counting_string), 1, (draw_info.GREEN),None)
        draw_info.window.blit(counting_text,(draw_info.width-150,15))
    
    if not sortedd and not sorting:
        counting_string= "0 ms"
        counting_text = draw_info.REG_FONT.render(str(counting_string), 1, (draw_info.GREEN),None)
        draw_info.window.blit(counting_text,(draw_info.width-150,15))

# random number list generator
def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    global retainList
    retainList = lst.copy()
    return lst

# file input number generator
def generage_list_file(location):

    try:
        input = np.loadtxt(location)

        # if numbers are integers, then convert them into integers    
        input_int = input.astype(int)
        safe_conversion = (input - input_int) == 0
        # if we can convert the whole array to integers, do that
        if np.all(safe_conversion):
            input = input_int.tolist()
            
        # convert numpy into list
        input = list(input)

        for number in input:
            if number <= 0:
                msgbox("0 or negative number detected. Cannot visualize them",title="Invalid Input",ok_button="Close")
                input = []
                return input
            
        if len(input) < 5:
                msgbox("Please input atleast 5 numbers to visualize them",title="Insufficient Input",ok_button="Close")
                input = []
                return input
    except Exception as e:
        msgbox(str(e),title="Exception",ok_button="Close")
    
    global retainList
    retainList = input.copy()
    return input

# main code
def main():
    global start,start_time,end,FPS
        
    run = True
    clock = pygame.time.Clock()

    data = {}

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

    optionsAlgo = OptionBox(
    draw_info.width/2-200, 100, 200, 30, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
    SORTING_ALGOS)

    optionsFPS = OptionBox(
    draw_info.width//2+5, 100, 100, 30, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
    FPSOPTIONS)

    manager = pygame_gui.UIManager((800, 600))

    file_selection_button = UIButton(relative_rect=Rect(0, 100, 130, 33),
                                 manager=manager, text='Select File')
    
    infoButton = Button((150, 150, 150),0,15,100,30,pygame.font.SysFont('comicsans', 20),text="Info")

    plotButton = Button((150, 150, 150),draw_info.width-100,100,100,30,pygame.font.SysFont('comicsans', 20),text="plot")

    sortedd = False

    # main loop to run pygame
    while run:
        time_delta = clock.tick(FPS) / 1000.0
        timer_draw(draw_info,sorting,sortedd)
        # check if sorting to load sequence of generator objects
        if sorting:
            try:
                next(sortingAlgoGenerator)
            except StopIteration:
                end = time.time()
                timeComplex = round(end-start,3)
                sorting = False
                sortedd=True
                data[sortingAlgoName] = timeComplex
                msgbox(title="Sorted Successfully",msg=f"Original list: {retainList}\n\nSorted List: {lst}\n\nTime Taken: {timeComplex}",ok_button="OK")
                
        else:
            # render objects to draw on screen
            draw(draw_info,sortingAlgoName,ascending, optionsAlgo,optionsFPS,manager,infoButton,plotButton,sorting,sortedd,time_delta)
        
        # get all events
        event_list = pygame.event.get()

        # optionAlgo event
        # choosing different optionsAlgo and operation based on their returned index
        selected_option = optionsAlgo.update(event_list)
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
                sortingAlgoName = "Count Sort"
                sortingAlgorithm = countSort  

            if selected_option == 8:
                sortingAlgoName = "Quinsert Sort"
                sortingAlgorithm = quinsertSort  

            if selected_option == 9:
                sortingAlgoName = "Range Query"
                sortingAlgorithm = rangeQuery   
    
        # optionFPS event
        # choosing different optionsFPS and operation based on their returned index
        selected_optionFPS = optionsFPS.update(event_list)
        if selected_optionFPS >= 0 and not sorting:
            if selected_optionFPS == 0:
                FPS = 60
            if selected_optionFPS == 1:
                FPS = 30
            if selected_optionFPS == 2:
                FPS = 10
        

        for event in event_list:
            pos = pygame.mouse.get_pos()
            
            # exit event
            if event.type == pygame.QUIT:
                run = False
                
            # info button event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if infoButton.isOver(pos):
                    msgbox(msg=infoAlgoMsg(sortingAlgoName),title="Information Panel", ok_button="OK")

                if plotButton.isOver(pos):
                    matplotWindow(data)
                    # pass

            if event.type == pygame.MOUSEMOTION:
                if (infoButton.isOver(pos)):
                    infoButton.color = (100, 200, 255)
                else:                    
                    infoButton.color = (draw_info.GREY)
                    
                if (plotButton.isOver(pos)):
                    plotButton.color = (100, 200, 255)
                else:                    
                    plotButton.color = (draw_info.GREY)

            # file input event
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        
                    if event.ui_element == file_selection_button:
                        file_selection = UIFileDialog(rect=Rect(100, 0, 600, 400), manager=manager, allow_picking_directories=True)

                    if event.ui_element == file_selection.ok_button:
                        lst = generage_list_file(file_selection.current_file_path)
                        if lst:
                            draw_info.set_list(lst)
                            sorting=False
                            sortedd=False
                            msgbox(msg=f"Input loaded successfully : {lst}", title="Successfully Loaded", ok_button="Ok")

            # handle file input change
            manager.process_events(event)

            # if no key pressed skip
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_g:
                lst = generate_starting_list(n,min_val,max_val)
                draw_info.set_list(lst)
                sorting=False
                sortedd=False
                msgbox(msg=f"random numbers generated successfully: {lst}",title="Successfully Loaded", ok_button="Ok")


            elif event.key == pygame.K_r:
                lst = retainList.copy()
                draw_info.set_list(lst)
                sorting=False
                sortedd=False
                msgbox(msg=f"original numbers generated successfully: {lst}",title="Successfully Loaded", ok_button="Ok")


            elif event.key == pygame.K_i:
                msgbox(msg=infoAlgoMsg(sortingAlgoName),title="Information Panel", ok_button="OK")


            elif event.key == pygame.K_SPACE and sorting==False:
                isIntLst = checkInteger(lst)
                if (not isIntLst) and (sortingAlgoName == "Radix Sort" or sortingAlgoName == "Count Sort"):
                    msgbox("Count Or Radix Sort doesnot work on float numbers inputted",title="Float Validation", ok_button="Close")
                else:
                    sorting = True
                    start = time.time()
                    start_time = pygame.time.get_ticks()
                    if sortingAlgoName == "Range Query":
                        sortingAlgoGenerator = sortingAlgorithm(draw_info,draw_list,drawRange,ascending)
                    else:
                        sortingAlgoGenerator = sortingAlgorithm(draw_info,draw_list,ascending)                        
                    
            elif event.key == pygame.K_a and not sorting:
                ascending = True

            elif event.key == pygame.K_d and not sorting:
                ascending = False

            elif (event.key == pygame.K_1) and not sorting:
                sortingAlgoName = "Insertion Sort"
                sortingAlgorithm = insertionSort
                optionsAlgo.selected = 0

            elif (event.key == pygame.K_2) and not sorting:
                sortingAlgoName = "Bubble Sort"
                sortingAlgorithm = bubbleSort
                optionsAlgo.selected = 1

            elif (event.key == pygame.K_3) and not sorting:
                sortingAlgoName = "Merge Sort"
                sortingAlgorithm = mergeSort
                optionsAlgo.selected = 2

            elif (event.key == pygame.K_4) and not sorting:
                sortingAlgoName = "Heap Sort"
                sortingAlgorithm = heapSort
                optionsAlgo.selected = 3

            elif (event.key == pygame.K_5) and not sorting:
                sortingAlgoName = "Quick Sort"
                sortingAlgorithm = quickSort
                optionsAlgo.selected = 4

            elif (event.key == pygame.K_6) and not sorting:
                sortingAlgoName = "Radix Sort"
                sortingAlgorithm = radixSort
                optionsAlgo.selected = 5

            elif (event.key == pygame.K_7) and not sorting:
                sortingAlgoName = "Bucket Sort"
                sortingAlgorithm = bucketSort
                optionsAlgo.selected = 6

            elif (event.key == pygame.K_8) and not sorting:
                sortingAlgoName = "Count Sort"
                sortingAlgorithm = countSort
                optionsAlgo.selected = 7


            elif (event.key == pygame.K_9) and not sorting:
                sortingAlgoName = "Quinsert Sort"
                sortingAlgorithm = quinsertSort
                optionsAlgo.selected = 8

            elif (event.key == pygame.K_0) and not sorting:
                sortingAlgoName = "Range Query"
                sortingAlgorithm = rangeQuery   
                optionsAlgo.selected = 9

    pygame.quit()



# run the main function of this file
if __name__ == "__main__":
    main()