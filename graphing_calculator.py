import pygame
import sys

pygame.init()

#screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Graphing Calculator")

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# font
font = pygame.font.SysFont(None, 40)

#store coefficients and drawing flag
coefficients = {
    'a': '',
    'b': '',
    'c': ''
}

#track the current coefficient input field
current_coefficient = 'a'

#store the graph drawn flag
graph_drawn = False

#evaluate the parabola equation
def evaluate_parabola(a, b, c, x):
    return a * x * x + b * x + c

#draw the graph scaled and centered on the screen
def draw_graph(a, b, c):
    scale_factor = 0.04
    graph_width = screen_width * scale_factor
    graph_height = screen_height * scale_factor

    for x in range(screen_width):
        x_value = (x - screen_width / 2) / graph_width
        y = int(evaluate_parabola(a, b, c, x_value) * graph_height)
        pygame.draw.rect(screen, RED, (x, screen_height // 2 - y, 1, 1))

#clear the screen and reset coefficients
def clear_screen():
    screen.fill(BLACK)
    coefficients['a'] = ''
    coefficients['b'] = ''
    coefficients['c'] = ''

#main function
def main():
    global current_coefficient, graph_drawn

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if graph_drawn:
                        graph_drawn = False
                    else:
                        try:
                            a = float(coefficients['a'])
                            b = float(coefficients['b'])
                            c = float(coefficients['c'])
                            draw_graph(a, b, c)
                            graph_drawn = True
                        except ValueError:
                            print("Invalid input. Please enter numeric coefficients.")
                elif event.key == pygame.K_TAB:
                    if current_coefficient == 'a':
                        current_coefficient = 'b'
                    elif current_coefficient == 'b':
                        current_coefficient = 'c'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    coefficients[current_coefficient] = coefficients[current_coefficient][:-1]
                elif event.unicode.isnumeric() or event.unicode in ".-":
                    coefficients[current_coefficient] += event.unicode

        #clear screen
        screen.fill(BLACK)

        if not graph_drawn:
            #draw the number buttons and coefficients
            for i, coeff in enumerate(coefficients.keys()):
                pygame.draw.rect(screen, GRAY, (300, 100 + 70 * i, 200, 50))
                text = font.render(coeff + ": " + coefficients[coeff], True, BLACK)
                screen.blit(text, (320, 110 + 70 * i))

                #highlight current coefficient input field
                if coeff == current_coefficient:
                    pygame.draw.rect(screen, WHITE, (300, 100 + 70 * i, 200, 50), 3)

            #UI
            instruction_text = font.render("Enter coefficients 'a', 'b', and 'c'. Use Tab to move between fields. Press Enter to plot the graph. Press Esc to quit.", True, WHITE)
            screen.blit(instruction_text, (10, screen_height - 50))
        else:
            #draw graph
            a = float(coefficients['a'])
            b = float(coefficients['b'])
            c = float(coefficients['c'])
            draw_graph(a, b, c)

        pygame.display.flip()

if __name__ == "__main__":
    main()