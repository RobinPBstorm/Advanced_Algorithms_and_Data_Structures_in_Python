import curses
import asyncio
import random
from collections import deque

async def main(screen: curses.window):
    SIZE = 20
    SNAKE_SYMBOLE = '*'
    FOOD_SYMBOLE = '0'

    snake = deque()
    snake.append((0,0))
    snake.append((0,1))
    snake.append((0,2))
    snake.append((0,3))

    dir_x, dir_y = (0,1)
    is_running = True

    food_position = None

    def print_area():
        screen.addstr(0,0, f'╔{'═' * SIZE }╗')
        for i in range(1, SIZE+1):
            screen.addstr(i,0, f'║{' ' * SIZE }║')
        screen.addstr(SIZE + 1,0, f'╚{'═' * SIZE }╝')

    def print_snake():
        for item in snake:
            screen.addstr(item[1] + 1, item[0] + 1, SNAKE_SYMBOLE)

    def print_food():
        screen.addstr(food_position[1] + 1, food_position[0] + 1, FOOD_SYMBOLE)

    def print_global():
        screen.clear()
        curses.curs_set(False)
        print_area()
        print_snake()
        print_food()
        screen.refresh()

    def generate_food():
        nonlocal food_position
        cases_remaining = set((line,col) for line in range(0, SIZE) for col in range(0,SIZE)) - set(snake)
        food_position = random.choice(list(cases_remaining))

    async def move():
        nonlocal dir_x, dir_y, snake, food_position
        while is_running:
            await asyncio.sleep(0.2)
            # déplacement simple
            head = snake[-1]
            snake.append(((head[0] + dir_x) % SIZE, (head[1] + dir_y) % SIZE))
            # déplacement si tête est sur la nourriture
            head = snake[-1]
            if head == food_position:
                generate_food()
            elif head in list(snake)[:-1:]:
                screen.addstr(0,0, 'GAME OVER')
                screen.refresh()
                break
            else:
                snake.popleft()
            print_global()

    def key_input():
        nonlocal dir_x, dir_y, is_running
        while is_running:
            key = screen.getch()
            if key == 27:
                is_running = False
            elif key == curses.KEY_UP:
                dir_y, dir_x = (-1, 0)
            elif key == curses.KEY_DOWN:
                dir_y, dir_x = (1, 0)
            elif key == curses.KEY_LEFT:
                dir_y, dir_x = (0, -1)
            elif key == curses.KEY_RIGHT:
                dir_y, dir_x = (0, 1)
    
    generate_food()

    print_global()

    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, key_input)

    await move()


curses.wrapper(lambda screen: asyncio.run(main(screen)))