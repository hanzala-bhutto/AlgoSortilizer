import pygame

pygame.init()

screen = pygame.display.set_mode( (800,600) )

font = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()

start_time = pygame.time.get_ticks() 

paused  = False
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        counting_time = pygame.time.get_ticks() - start_time

        # change milliseconds into minutes, seconds, milliseconds
        counting_seconds = str( (counting_time%60000)/1000 ).zfill(2)

        counting_string = "%s" % (counting_seconds)

        counting_text = font.render(str(counting_string), 1, (255,255,255))
        counting_rect = counting_text.get_rect(center = screen.get_rect().center)

    screen.fill( (0,0,0) )
    screen.blit(counting_text, counting_rect)

    pygame.display.update()

    clock.tick(60)