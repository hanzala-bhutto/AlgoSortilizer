import pygame
import pygamepopup
from pygamepopup.menu_manager import MenuManager
from pygamepopup.components import Button, InfoBox, TextElement

pygame.init()
pygamepopup.init()

def create_menu(menu_manager):
    other_menu = InfoBox(
        "Smaller menu",
        [
            [
                TextElement(
                    text="The text content of a menu is automatically splitted in multiple "
                    "part "
                    "to fit in the box. To add a new paragraph, just create another "
                    "TextElement."
                )
            ]
        ],
        width=300,
    )
    menu_manager.open_menu(other_menu)

def main():
    run = True
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800,600))

    menu_manager = MenuManager(screen)
    create_menu(menu_manager)
    # main loop to run pygame
    while run:
        clock.tick(60)
    
        for event in pygame.event.get():
            # exit event
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.K_r:
                menu_manager.motion(event.pos)
                menu_manager.display()

            elif event.type == pygame.MOUSEMOTION:
                menu_manager.motion(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    menu_manager.display()
        
        menu_manager.display()
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()