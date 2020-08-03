import pygame
import random
import time
from threading import Timer

pygame.font.init()

win_width = 1000
win_height = 710
screen = pygame.display.set_mode((win_width, win_height))

moles = []
score_check = 0

font = pygame.font.Font('freesansbold.ttf', 32)
score = pygame.font.Font('freesansbold.ttf', 32)
score_text = 'Score: 0'.rjust(3)
clock = pygame.time.Clock()


def counters(var_count):
    counter1 = var_count
    return main(counter1)


def modes():
    global sc
    mode = True
    count_txt = pygame.font.Font('freesansbold.ttf', 50)
    normal_txt = pygame.font.SysFont('comicsans', 40)
    set = "Set Timer"
    count_txt_width, count_txt_height = count_txt.size(set)
    check = sc[-1]
    aim = pygame.image.load("aim.png")
    while mode:
        # colours -------------
        green = (0, 200, 0)
        bright_green = (0, 255, 0)
        red = (200, 0, 0)
        bright_red = (255, 0, 0)

        # colours end ---------
        ax, ay = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pos()
        screen.fill((51, 187, 255))
        pygame.display.set_caption("Modes")
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                quit()
            # ---------------------------start timers ---------------------------
            # 15 secs -------------------------------------

            if (win_width / 8) + 100 > mouse[0] > (win_width / 8) and (win_height / 1.7) + 50 > mouse[1] > (
                    win_height / 1.7):
                pygame.draw.rect(screen, bright_red, ((win_width / 8), (win_height / 1.7), 100, 50))

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    counters(15)
            else:
                pygame.draw.rect(screen, red, ((win_width / 8), (win_height / 1.7), 100, 50))

            # 20 secs -----------------------------------
            if (win_width / 3.3) + 100 > mouse[0] > (win_width / 3.3) and (win_height / 1.7) + 50 > mouse[1] > (
                    win_height / 1.7):
                pygame.draw.rect(screen, bright_red, ((win_width / 3.3), (win_height / 1.7), 100, 50))

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    counters(20)
            else:
                pygame.draw.rect(screen, red, ((win_width / 3.3), (win_height / 1.7), 100, 50))

            # 30 secs ------------------------------------
            if (win_width / 2) + 100 > mouse[0] > (win_width / 2) and (win_height / 1.7) + 50 > mouse[1] > (
                    win_height / 1.7):
                pygame.draw.rect(screen, bright_red, ((win_width / 2), (win_height / 1.7), 100, 50))

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    counters(30)
            else:
                pygame.draw.rect(screen, red, ((win_width / 2), (win_height / 1.7), 100, 50))

            # 45 secs ------------------------------------
            if (win_width / 1.4) + 100 > mouse[0] > (win_width / 1.4) and (win_height / 1.7) + 50 > mouse[1] > (
                    win_height / 1.7):
                pygame.draw.rect(screen, bright_red, ((win_width / 1.4), (win_height / 1.7), 100, 50))

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    counters(45)
            else:
                pygame.draw.rect(screen, red, ((win_width / 1.4), (win_height / 1.7), 100, 50))

            # end timers -----------------------------------

            # -------------------------------------------------------------------------------

            # back button ----------------------------------
            if (win_width / 15) + 100 > mouse[0] > (win_width / 15) and (win_height / 1.12) + 50 > mouse[1] > (
                    win_height / 1.12):
                pygame.draw.rect(screen, bright_green, ((win_width / 15), (win_height / 1.12), 100, 50))

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    temp_main_menu(check)
            else:
                pygame.draw.rect(screen, green, ((win_width / 15), (win_height / 1.12), 100, 50))
            # button texts --------------------------------
            screen.blit(normal_txt.render("15 secs".rjust(3), True, (0, 0, 0)), ((win_width / 8), (win_height / 1.65)))
            screen.blit(normal_txt.render("20 secs".rjust(3), True, (0, 0, 0)), ((win_width / 3.3), (win_height / 1.65)))
            screen.blit(normal_txt.render("30 secs".rjust(3), True, (0, 0, 0)), ((win_width / 2), (win_height / 1.65)))
            screen.blit(normal_txt.render("45 secs".rjust(3), True, (0, 0, 0)), ((win_width / 1.4), (win_height / 1.65)))
            screen.blit(normal_txt.render("Back".rjust(3), True, (0, 0, 0)), ((win_width / 12), (win_height / 1.1)))
            # --------------------- end button texts --------------------------------------

            screen.blit(aim, ((ax - 32), (ay - 32)))
            screen.blit(count_txt.render(set, True, (0, 0, 0)),
                        (((win_width / 2) - (count_txt_width / 2)), (win_height/15)))

            pygame.display.flip()
            clock.tick(90)


def mole_spawn_easy():
    molex = random.randint(50, 950)
    moley = random.randint(450, 676)
    moles.append((molex, moley))


best = []
sc = []


def temp_main_menu(x):
    global best
    global sc
    score_check_new = x
    best.append(score_check_new)
    sc.append(score_check_new)
    #print(best)
    main_menu()


def main(counter):
    FPS = 90
    pygame.display.set_caption("Mole Shooter")

    run = True

    background = pygame.transform.scale(pygame.image.load('back_land.png'), (win_width, win_height))

    aim = pygame.image.load("aim.png")
    mole = pygame.image.load("mole.png")
    text = 'Time Left:' + str(counter).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    global font
    global score
    global score_text
    global moles
    global score_check
    global clock
    score_text = ("Score: 0").rjust(3)
    while run:

        ax, ay = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT:
                counter -= 1
                text = ("Time Left: " + str(counter)).rjust(3)
                if counter > 0:
                    mole_spawn_easy()
                else:
                    temp_main_menu(score_check)

            if event.type == pygame.MOUSEBUTTONDOWN:

                mx = mole.get_width()
                my = mole.get_height()
                for i in moles:
                    if ax in range(i[0], i[0] + int(mx)) and ay in range(i[1], i[1] + int(my)):
                        # print("hit")
                        score_check += 1
                        score_text = ("Score: " + str(score_check)).rjust(3)

        screen.blit(background, [0, 0])

        for pos in moles:
            screen.blit(mole, pos)
            # print(pos)
            if len(moles) >= 2:
                del (moles[0])

        screen.blit(aim, ((ax - 32), (ay - 32)))

        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        screen.blit(score.render(score_text, True, (0, 0, 0)), (800, 48))
        clock.tick(FPS)

        pygame.display.flip()


def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


def rules():
    help = True

    while help:
        green = (0, 200, 0)
        mouse = pygame.mouse.get_pos()

        bright_green = (0, 255, 0)
        screen.fill((51, 187, 255))
        pygame.display.set_caption("Rules")
        rules_text = pygame.font.Font('freesansbold.ttf', 50)
        rule = pygame.font.Font('freesansbold.ttf', 32)
        objective_text = "Shoot as many Moles as possible"
        ob_width, ob_height = rule.size(objective_text)
        objective = "Objective"
        head_ob_width, head_ob_height = rules_text.size(objective)
        how_text = "How to Play"
        how_width, how_height = rules_text.size(how_text)
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                quit()
            screen.blit(rules_text.render(objective, True, (0, 0, 0)),
                        (((win_width / 2) - (head_ob_width/2)), ((win_height / 2) - 300)))

            screen.blit(rule.render(objective_text, True, (0, 0, 0)),
                        (((win_width / 2) - (ob_width/2)), ((win_height /2) - 200)))

            screen.blit(rules_text.render(how_text, True, (0, 0, 0)),
                        (((win_width / 2) - (how_width/2)), (win_height / 2) - 100))

            screen.blit(rule.render("1) Move the cross-hair using the mouse ", True, (0, 0, 0)),
                        (((win_width / 2) - 300), (win_height / 2)))

            screen.blit(rule.render("2) Target the mole, click to shoot", True,
                                    (0, 0, 0)), (((win_width / 2) - 300), ((win_height / 2) + 50)))
            screen.blit(rule.render("3) Click multiple times on the same mole", True,
                                    (0, 0, 0)), (((win_width / 2) - 300), ((win_height / 2) + 100)))

            if 470 + 100 > mouse[0] > 470 and 510 + 50 > mouse[1] > 510:
                pygame.draw.rect(screen, bright_green, (470, 510, 100, 50))

                if eve.type == pygame.MOUSEBUTTONDOWN:
                    main_menu()
            else:
                pygame.draw.rect(screen, green, (470, 510, 100, 50))

            screen.blit(rule.render("Back".rjust(3), True, (0, 0, 0)), (482, 518))
            pygame.display.update()
            clock.tick(60)


def main_menu():
    global best
    global counter
    global text
    global score_text
    global score_check
    global sc
    aim = pygame.image.load("aim.png")
    intro = True
    while intro:
        ax, ay = pygame.mouse.get_pos()
        sc_check = sc[-1]

        restart_text = pygame.font.Font('freesansbold.ttf', 28)
        help_text = pygame.font.Font('freesansbold.ttf', 28)
        game_name = pygame.font.Font('freesansbold.ttf', 40)
        mole = pygame.image.load("mole.png")
        screen.fill((51, 187, 255))
        pygame.display.set_caption("Main Menu")
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Main Menu", largeText)
        TextRect.center = ((win_width / 2), (win_height / 2) - 250)
        screen.blit(TextSurf, TextRect)
        screen.blit(mole, (((win_width / 2) - 17), ((win_height / 2) - 100)))
        screen.blit(game_name.render("Shoot-a-Mole", True, (0, 0, 0)),
                    (((win_width / 2) - 130), ((win_height / 2) - 200)))
        final_score = ('Your Score: ' + str(sc_check)).rjust(3)

        real_best = max(best)
        best_score = ('Your Best Score:' + str(real_best)).rjust(3)
        screen.blit(score.render(best_score, True, (0, 0, 0)), ((win_width / 3), ((win_height / 1.95) - 40)))
        # final_score = 0

        # colours----------

        green = (0, 200, 0)
        bright_green = (0, 255, 0)

        # colours end -----------
        mouse = pygame.mouse.get_pos()

        screen.blit(score.render(final_score, True, (0, 0, 0)), (((win_width / 2) - 98), (win_height / 1.9)))

        counter = 30
        score_check = 0
        text = 'Time Left: 30'.rjust(3)
        score_text = ('Score: '+ str(sc_check)).rjust(3)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # button1---start-------------------------------------------------------
            if 250 + 100 > mouse[0] > 250 and (win_height/1.45) + 50 > mouse[1] > (win_height/1.45):
                pygame.draw.rect(screen, bright_green, (250, (win_height/1.45), 100, 50))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    modes()
            else:
                pygame.draw.rect(screen, green, (250, (win_height/1.45), 100, 50))
            # button2------rules---------------------------------------------------
            if 650 + 100 > mouse[0] > 650 and (win_height/1.45) + 50 > mouse[1] > (win_height/1.45):
                pygame.draw.rect(screen, bright_green, (650, (win_height/1.45), 100, 50))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    rules()
            else:
                pygame.draw.rect(screen, green, (650, (win_height/1.45), 100, 50))

            # # button3-------------------------------------------------------
            # if 450 + 100 > mouse[0] > 450 and 450 + 50 > mouse[1] > 450:
            #     pygame.draw.rect(screen, bright_green, (450, 450, 100, 50))
            #
            #     if event.type == pygame.MOUSEBUTTONDOWN:
            #         modes()
            # else:
            #     pygame.draw.rect(screen, green, (450, 450, 100, 50))

            # end buttons----------------------------------------------------
            screen.blit(aim, ((ax - 32), (ay - 32)))
            screen.blit(restart_text.render("Start", True, (0, 0, 0)), (265, (win_height/1.42)))
            screen.blit(help_text.render("Rules".rjust(4), True, (0, 0, 0)), (658, (win_height / 1.42)))
            screen.blit(help_text.render("Made By: Rishi Bidani".rjust(4), True, (0, 0, 0)), (0, 0))
            pygame.display.update()
            clock.tick(90)

temp_main_menu(0)
