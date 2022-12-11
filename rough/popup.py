import pygame, sys
from pgu import gui

# original author: user nmicahaels https://stackoverflow.com/questions/3302973/making-popup-windows-in-pygame-with-pgu

WIDTH = 640
HEIGHT = 480


def init_pygame():
    pygame.display.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption('Testing PGU')
    return screen


class SimpleDialog(gui.Dialog):
    def __init__(self):
        title = gui.Label("Spam")
        main = gui.Container(width=20, height=20)
        # passing the 'height' parameter resulting in a typerror when paint was called
        super(SimpleDialog, self).__init__(title, main, width=40)  # , height=40)

    def close(self, *args, **kwargs):
        return super(SimpleDialog, self).close(*args, **kwargs)


def run():
    black = (0, 0, 0)
    screen = init_pygame()  # type: pygame.Surface
    refresh = pygame.display.update
    app = gui.App()

    dialog = SimpleDialog()
    # app.init(dialog)

    empty = gui.Container(width=WIDTH, height=HEIGHT)
    app.init(empty)

    app.paint(screen)
    pygame.display.flip()
    while True:
        screen.fill(black)
        app.paint(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # right mouse button
                    dialog.open()
                else:
                    app.event(event)
            elif event.type == pygame.QUIT:
                sys.exit()
            else:
                app.event(event)
    refresh()

run()