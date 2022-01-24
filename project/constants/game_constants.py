from project.constants import constants

from project.model.board import Board, Position, Obstacle
from project.model.position import Pattern, Movement, Direction
from project.model.square_type import SquareType

LEARNING_RATE: float = 0.6

DISCOUNT_FACTOR: float = 0.5
# DISCOUNT_FACTOR: float = 1

# EXPLORATION_RATE: float = 1.0
EXPLORATION_RATE: float = 0.0

DIMINUTION_RATE: float = 0.99

# DEFAULT_REWARD_VALUE: float = 10.0
DEFAULT_REWARD_VALUE: float = 0.0

REWARD_WITH_TYPE: {SquareType: int} = {
    SquareType.EMPTY: -5,
    SquareType.WALL: -50,
    SquareType.OBSTACLE: -1000,
    SquareType.GOAL: 5000
}

NUMBER_ROUND: int = 101

CHOSEN_BOARD: str = "BOARD_LEVEL_1"
# CHOSEN_BOARD: str = "BOARD_LEVEL_2"
# CHOSEN_BOARD: str = "BOARD_LEVEL_3"
# CHOSEN_BOARD: str = "SQUARE_BOARD"

# IS_AI_PLAYING: bool = False
IS_AI_PLAYING: bool = True

CROSS_PATTERN: Pattern = Pattern(list_of_movements=
                                 [Movement(direction=Direction.RIGHT),
                                  Movement(direction=Direction.LEFT),
                                  Movement(direction=Direction.UP),
                                  Movement(direction=Direction.DOWN),
                                  Movement(direction=Direction.LEFT),
                                  Movement(direction=Direction.RIGHT),
                                  Movement(direction=Direction.DOWN),
                                  Movement(direction=Direction.UP)])

UP_DOWN_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.UP),
                                                      Movement(direction=Direction.UP),
                                                      Movement(direction=Direction.UP),
                                                      Movement(direction=Direction.DOWN),
                                                      Movement(direction=Direction.DOWN),
                                                      Movement(direction=Direction.DOWN)])

RIGHT_LEFT_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.RIGHT),
                                                         Movement(direction=Direction.RIGHT),
                                                         Movement(direction=Direction.RIGHT),
                                                         Movement(direction=Direction.LEFT),
                                                         Movement(direction=Direction.LEFT),
                                                         Movement(direction=Direction.LEFT)])

SQUARE_PATTERN: Pattern = Pattern(list_of_movements=[Movement(direction=Direction.RIGHT),
                                                     Movement(direction=Direction.DOWN),
                                                     Movement(direction=Direction.LEFT),
                                                     Movement(direction=Direction.UP)
                                                     ])

OBSTACLE_UP_DOWN_PATTERN_1_BOARD_LEVEL_2 = Obstacle(position=Position(co_x=4, co_y=2), pattern=UP_DOWN_PATTERN)

OBSTACLE_CROSS_PATTERN_1_BOARD_LEVEL_3: Obstacle = Obstacle(position=Position(co_x=4, co_y=1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN_2_BOARD_LEVEL_3: Obstacle = Obstacle(position=Position(co_x=6, co_y=1), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_1: Obstacle = Obstacle(position=Position(co_x=4, co_y=4), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_2: Obstacle = Obstacle(position=Position(co_x=7, co_y=7), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_3: Obstacle = Obstacle(position=Position(co_x=4, co_y=7), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_4: Obstacle = Obstacle(position=Position(co_x=7, co_y=4), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_5: Obstacle = Obstacle(position=Position(co_x=9, co_y=2), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_6: Obstacle = Obstacle(position=Position(co_x=2, co_y=9), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_SQUARE_PATTERN_7: Obstacle = Obstacle(position=Position(co_x=5, co_y=5), pattern=SQUARE_PATTERN)

OBSTACLE_SQUARE_UP_DOWN_PATTERN_8: Obstacle = Obstacle(position=Position(co_x=2, co_y=7), pattern=UP_DOWN_PATTERN)

OBSTACLE_SQUARE_UP_DOWN_PATTERN_9: Obstacle = Obstacle(position=Position(co_x=9, co_y=7), pattern=UP_DOWN_PATTERN)

OBSTACLE_SQUARE_RIGHT_LEFT_PATTERN_10: Obstacle = Obstacle(position=Position(co_x=4, co_y=2),
                                                           pattern=RIGHT_LEFT_PATTERN)

OBSTACLE_SQUARE_RIGHT_LEFT_PATTERN_11: Obstacle = Obstacle(position=Position(co_x=4, co_y=9),
                                                           pattern=RIGHT_LEFT_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_12: Obstacle = Obstacle(position=Position(co_x=2, co_y=2), pattern=CROSS_PATTERN)

OBSTACLE_SQUARE_CROSS_PATTERN_13: Obstacle = Obstacle(position=Position(co_x=9, co_y=9), pattern=CROSS_PATTERN)

BOARD_LEVEL_1_START_POSITION: Position = Position(2, 2)

BOARD_LEVEL_1_GOAL_POSITION: Position = Position(6, 2)

BOARD_LEVEL_2_START_POSITION: Position = Position(2, 2)

BOARD_LEVEL_2_GOAL_POSITION: Position = Position(6, 2)

BOARD_LEVEL_3_START_POSITION: Position = Position(2, 2)

BOARD_LEVEL_3_GOAL_POSITION: Position = Position(8, 2)

SQUARE_START_POSITION: Position = Position(1, 5)

SQUARE_GOAL_POSITION: Position = Position(10, 6)

BOARD_LEVEL_1: Board = Board(name="BOARD_LEVEL_1",
                             width=constants.BOARD_LEVEL_1_WIDTH, height=constants.BOARD_LEVEL_1_HEIGHT,
                             position_start=BOARD_LEVEL_1_START_POSITION, position_goal=BOARD_LEVEL_1_GOAL_POSITION,
                             list_of_obstacle=[])

BOARD_LEVEL_2: Board = Board(name="BOARD_LEVEL_2",
                             width=constants.BOARD_LEVEL_2_WIDTH, height=constants.BOARD_LEVEL_2_HEIGHT,
                             position_start=BOARD_LEVEL_2_START_POSITION, position_goal=BOARD_LEVEL_2_GOAL_POSITION,
                             list_of_obstacle=[
                                 OBSTACLE_UP_DOWN_PATTERN_1_BOARD_LEVEL_2
                             ])

BOARD_LEVEL_3: Board = Board(name="BOARD_LEVEL_3",
                             width=constants.BOARD_LEVEL_3_WIDTH, height=constants.BOARD_LEVEL_3_HEIGHT,
                             position_start=BOARD_LEVEL_3_START_POSITION, position_goal=BOARD_LEVEL_3_GOAL_POSITION,
                             list_of_obstacle=[
                                 OBSTACLE_CROSS_PATTERN_1_BOARD_LEVEL_3,
                                 OBSTACLE_CROSS_PATTERN_2_BOARD_LEVEL_3
                             ])

SQUARE_BOARD: Board = Board(name="SQUARE_BOARD", width=constants.SQUARE_BOARD_WIDTH,
                            height=constants.SQUARE_BOARD_HEIGHT,
                            position_start=SQUARE_START_POSITION, position_goal=SQUARE_GOAL_POSITION,
                            list_of_obstacle=[
                                OBSTACLE_SQUARE_CROSS_PATTERN_1,
                                OBSTACLE_SQUARE_CROSS_PATTERN_2,
                                OBSTACLE_SQUARE_CROSS_PATTERN_3,
                                OBSTACLE_SQUARE_CROSS_PATTERN_4,
                                OBSTACLE_SQUARE_CROSS_PATTERN_5,
                                OBSTACLE_SQUARE_CROSS_PATTERN_6,
                                OBSTACLE_SQUARE_SQUARE_PATTERN_7,
                                OBSTACLE_SQUARE_UP_DOWN_PATTERN_8,
                                OBSTACLE_SQUARE_UP_DOWN_PATTERN_9,
                                OBSTACLE_SQUARE_RIGHT_LEFT_PATTERN_10,
                                OBSTACLE_SQUARE_RIGHT_LEFT_PATTERN_11,
                                OBSTACLE_SQUARE_CROSS_PATTERN_12,
                                OBSTACLE_SQUARE_CROSS_PATTERN_13
                            ])

BOARD_WITH_NAME: {str: Board} = {
    BOARD_LEVEL_1.name: BOARD_LEVEL_1,
    BOARD_LEVEL_2.name: BOARD_LEVEL_2,
    BOARD_LEVEL_3.name: BOARD_LEVEL_3,
    SQUARE_BOARD.name: SQUARE_BOARD,
}
