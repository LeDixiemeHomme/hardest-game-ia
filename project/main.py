import pygame

from project.logger.logger import Logger
from project.constants.game_constants import Movement, Board, MAIN_BOARD, SQUARE_BOARD, TEST_BOARD

from project.model.agent import Agent
from project.model.direction import Direction

logger: Logger = Logger(name=__name__, log_file_name="main_log")
stdout_logger = logger.stdout_log


if __name__ == '__main__':
    running = True
    lose = win = False

    # board: Board = MAIN_BOARD
    board: Board = SQUARE_BOARD
    # board: Board = TEST_BOARD

    board.instantiate_singleton_viewer()

    agent: Agent = Agent(board=board)

    stdout_logger.debug("Start drawing board ...")
    agent.board.draw_board()

    while running and not win and not lose:
        agent.board.viewer.screen.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                movement_next: Movement = Movement(
                    direction=board.viewer.direction_from_key_down_value(key_down=event.key))
                agent.move_agent_if_possible(requested_movement=movement_next)

        agent.board.move_obstacles()
        agent.draw_image_on_current_position()

        best_direction: Direction = agent.best_action()
        reward: int = agent.move_agent_with_qtable_update(requested_movement=Movement(direction=best_direction))

        if agent.is_position_on_goal_square():
            win = True
        if agent.is_position_on_obstacle_square():
            lose = True

    if win:
        stdout_logger.debug("You win")
    if lose:
        stdout_logger.debug("You lose")
