from project.constants import constants

from project.model.board import Board, Movement, Position, Obstacle
from project.model.pattern import Pattern
from project.model.direction import Direction

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

OBSTACLE_CROSS_PATTERN_MAIN_1: Obstacle = Obstacle(position=Position(co_x=5, co_y=1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN_MAIN_2: Obstacle = Obstacle(position=Position(co_x=7, co_y=3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN_MAIN_3: Obstacle = Obstacle(position=Position(co_x=9, co_y=1), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN_MAIN_4: Obstacle = Obstacle(position=Position(co_x=11, co_y=3), pattern=CROSS_PATTERN)

OBSTACLE_CROSS_PATTERN_MAIN_5: Obstacle = Obstacle(position=Position(co_x=13, co_y=2), pattern=CROSS_PATTERN)

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

MAIN_START_POSITION: Position = Position(2, 2)

MAIN_GOAL_POSITION: Position = Position(16, 2)

TEST_START_POSITION: Position = Position(1, 2)

TEST_GOAL_POSITION: Position = Position(3, 2)

SQUARE_START_POSITION: Position = Position(5, 1)

SQUARE_GOAL_POSITION: Position = Position(6, 10)

MAIN_BOARD: Board = Board(width=constants.MAIN_BOARD_WIDTH, height=constants.MAIN_BOARD_HEIGHT,
                          position_start=MAIN_START_POSITION, position_goal=MAIN_GOAL_POSITION,
                          list_of_obstacle=[
                              OBSTACLE_CROSS_PATTERN_MAIN_1,
                              OBSTACLE_CROSS_PATTERN_MAIN_2,
                              OBSTACLE_CROSS_PATTERN_MAIN_3,
                              OBSTACLE_CROSS_PATTERN_MAIN_4,
                              OBSTACLE_CROSS_PATTERN_MAIN_5
                          ])

TEST_BOARD: Board = Board(width=constants.TEST_BOARD_WIDTH, height=constants.TEST_BOARD_HEIGHT,
                          position_start=TEST_START_POSITION, position_goal=TEST_GOAL_POSITION,
                          list_of_obstacle=[])

SQUARE_BOARD: Board = Board(width=constants.SQUARE_BOARD_WIDTH, height=constants.SQUARE_BOARD_HEIGHT,
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
