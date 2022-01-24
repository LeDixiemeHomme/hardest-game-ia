from typing import List

import pygame
import datetime
import matplotlib.pyplot as plt

from project.logger.logger import Logger
from project.constants import constants, game_constants
from project.constants.game_constants import Movement, Board, BOARD_LEVEL_1, BOARD_LEVEL_2, BOARD_LEVEL_3, SQUARE_BOARD

from project.model.agent import Agent

from project.model.q_table import Pickle, QTable
from project.model.square_type import SquareType

logger: Logger = Logger(name=__name__, log_file_name="main_log")
stdout_logger = logger.stdout_log
pickle_singleton: Pickle = Pickle()

if __name__ == '__main__':
    stdout_logger.debug("Tip arrow keys to move, tip q to quit.")

    data_name: str = 'common_qtable_file, lr = ' + str(game_constants.LEARNING_RATE) + \
                     ', df = ' + str(game_constants.DISCOUNT_FACTOR) + \
                     ', reward_goal = ' + str(game_constants.REWARD_WITH_TYPE.get(SquareType.GOAL))

    is_ai_playing = constants.IS_AI_PLAYING

    file_name: str = '../' + constants.STORAGE_DIR_NAME + '/' + data_name + '.dat'
    # file_name: str = '../generated_q_tables/common_qtable_file, lr = 0.2, df = 0.5, reward_goal = 2000.dat'
    # file_name: str = '../generated_q_tables/common_qtable_file, lr = 0.2, df = 0.5, reward_goal = 5000.dat'
    # file_name: str = '../generated_q_tables/common_qtable_file, lr = 0.4, df = 0.5, reward_goal = 2000.dat'
    # file_name: str = '../generated_q_tables/common_qtable_file, lr = 0.4, df = 0.5, reward_goal = 5000.dat'

    # choose the level you want to play
    board: Board = BOARD_LEVEL_1
    # board: Board = BOARD_LEVEL_2
    # board: Board = BOARD_LEVEL_3
    # board: Board = SQUARE_BOARD

    qtable: QTable = pickle_singleton.load(filename=file_name)

    history: List[int] = []
    number_of_win: int = 0

    for iteration in range(101):
        time_start_ite = datetime.datetime.now()
        running = True
        lose = win = over = False

        board.instantiate_singleton_viewer()
        agent: Agent = Agent(board=board, qtable=qtable,
                             learning_rate=game_constants.LEARNING_RATE,
                             discount_factor=game_constants.DISCOUNT_FACTOR)
        stdout_logger.debug("Start drawing board ...")
        agent.board.draw_board()

        while running and not win and not lose:
            agent.board.viewer.screen.update()
            agent.draw_image_on_current_position()
            agent.board.move_obstacles()
            movement_next = Movement()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key is pygame.K_q:
                        over = True
                    if not is_ai_playing:
                        movement_next: Movement = Movement(
                            direction=board.viewer.direction_from_key_down_value(key_down=event.key))
                        agent.move_agent_if_possible(requested_movement=movement_next,
                                                     should_qtable_be_updated=is_ai_playing)

            if is_ai_playing:
                # agent find the best movement to do
                movement_next: Movement = Movement(direction=agent.best_action())
                agent.move_agent_if_possible(requested_movement=movement_next, should_qtable_be_updated=is_ai_playing)

            if agent.is_position_on_goal_square():
                win = True
                stdout_logger.info("You win ++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                number_of_win += 1
            if agent.is_position_on_obstacle_square():
                lose = True
                stdout_logger.info("You lose")

            average: float = sum(history) / len(history) if len(history) != 0 else 1
            rewards = game_constants.REWARD_WITH_TYPE
            agent.display_info_on_screen(rectangle=(board.width, board.height), font_name="arial", font_size=25,
                                         txt=[
                                             "action : " + str(movement_next.direction.name),
                                             "score : " + str(agent.score),
                                             "timer : " + str(datetime.datetime.now() - time_start_ite),
                                             "iteration : " + str(iteration),
                                             "win : " + str(number_of_win) + "/" + str(iteration),
                                             "average score : " + "%.2f" % (
                                                 sum(history) / len(history) if len(history) != 0 else 1),
                                             "qtable size : " + str(len(agent.qtable.table)),
                                             "exploration rate : " + "%.8f" % agent.qtable.exploration,
                                             "lr : " + str(game_constants.LEARNING_RATE) +
                                             ", df : " + str(game_constants.DISCOUNT_FACTOR) +
                                             ", dim r: " + str(game_constants.DIMINUTION_RATE),
                                             "rewards :" +
                                             " Ept : " + str(rewards.get(SquareType.EMPTY)) +
                                             ", W : " + str(rewards.get(SquareType.WALL)),
                                             "Eni : " + str(rewards.get(SquareType.OBSTACLE)) +
                                             ", G : " + str(rewards.get(SquareType.GOAL))
                                         ])

        stdout_logger.info(str(iteration) + " - Your score : " + str(agent.score))
        qtable = agent.qtable

        if over:
            break
        else:
            history.append(agent.score)

    plt.plot(history)
    plt.title("level name : " + board.name +
              ", qtable size : " + str(len(qtable.table)))
    # plt.show()

    txt = ""
    while txt != "y" and txt != "n":
        txt = input(" -> Save the qtable at " + file_name + " \n -> y or n \n -> ").lower()
        print(txt)

    if txt == "y":
        # time = datetime.datetime.now()
        # data_name = board.name + "/" + time.strftime("max_score=" + str(max(history)) + " time=%Y-%m-%d_%H:%M:%S")
        # file_name: str = '../' + constants.STORAGE_DIR_NAME + '/' + data_name + '.dat'
        pickle_singleton.save(filename=file_name, qtable=qtable)
