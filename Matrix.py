import math


class Rule:
    row: int
    column: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.column = col

    def to_string(self) -> str:
        return f"{self.row} - {self.column}"


class Matrix:
    _data: []
    _count_row: int
    _count_col: int
    _laps: int

    def __init__(self, row: int, column: int) -> None:
        self._count_row = row
        self._count_col = column
        self._laps = 0
        self._data = []
        for i in range(self._count_row * self._count_col):
            self._data.append(0)

    def get_count_row(self) -> int:
        return self._count_row

    def get_count_col(self) -> int:
        return self._count_col

    def get_laps(self) -> int:
        return self._laps

    def get_value(self, position_x: int, position_y: int) -> int:
        return self._data[((position_x - 1) * self._count_col) + position_y - 1]

    def set_value(self, position_x: int, position_y: int, value: int):
        self._data[((position_x - 1) * self._count_col) + position_y - 1] = value

    def _get_row(self, row_position: int) -> []:
        return self._data[row_position * self._count_col - 1]

    def _valid_position(self, position_x: int, position_y: int) -> bool:
        return ((1 <= position_x <= self._count_row) and
                (1 <= position_y <= self._count_col) and
                (self.get_value(position_x, position_y) == 0))

    def available_rules(self, position_row: int, position_col: int) -> []:
        list_rules = []
        if self._valid_position(position_row, position_col - 1):  # left
            list_rules.append(Rule(position_row, position_col - 1))
        if self._valid_position(position_row - 1, position_col - 1):  # upper left diagonal
            list_rules.append(Rule(position_row - 1, position_col - 1))
        if self._valid_position(position_row - 1, position_col):  # up
            list_rules.append(Rule(position_row - 1, position_col))
        if self._valid_position(position_row - 1, position_col + 1):  # upper right diagonal
            list_rules.append(Rule(position_row - 1, position_col + 1))
        if self._valid_position(position_row, position_col + 1):  # right
            list_rules.append(Rule(position_row, position_col + 1))
        if self._valid_position(position_row + 1, position_col + 1):  # lower right diagonal
            list_rules.append(Rule(position_row + 1, position_col + 1))
        if self._valid_position(position_row + 1, position_col):  # down
            list_rules.append(Rule(position_row + 1, position_col))
        if self._valid_position(position_row + 1, position_col - 1):  # lower left diagonal
            list_rules.append(Rule(position_row + 1, position_col - 1))
        return list_rules

    @staticmethod
    def choose_rule(rules: []) -> Rule:
        return rules.pop(0)

    @staticmethod
    def distance(row_position: int, col_position: int,
                 row_end_position: int, col_end_position: int) -> int:
        return int(math.sqrt(((row_end_position - row_position) ** 2) +
                             ((col_end_position - col_position) ** 2)))

    def _choose_rule_distance(self, rules: [], row_end_position: int, col_end_position: int) -> Rule:
        index = 0
        minor_distance = self.distance(rules[0].row, rules[0].column, row_end_position, col_end_position)
        for i in range(1, rules.__len__()):
            distance = self.distance(rules[i].row, rules[i].column, row_end_position, col_end_position)
            if distance < minor_distance:
                minor_distance = distance
                index = i
        return rules.pop(index)

    def _choose_knights_rule(self, rules: [], row_end_position: int, col_end_position: int):
        sw = not self._knights_target_position(rules[0].row, rules[0].column, row_end_position, col_end_position)
        index = 0
        i = 0
        length = len(rules)
        minor_distance = self.distance(rules[0].row, rules[0].column, row_end_position, col_end_position)
        while i < length and sw:
            sw = not self._knights_target_position(rules[i].row, rules[i].column, row_end_position, col_end_position)
            if sw:
                distance = self.distance(rules[i].row, rules[i].column, row_end_position, col_end_position)
                if distance < minor_distance:
                    minor_distance = distance
                    index = i
                i += 1
        return rules.pop(i) if not sw else rules.pop(index)

    @staticmethod
    def _knights_target_position(row_position: int, col_position: int,
                                 row_end_position: int, col_end_position: int) -> bool:
        return ((row_position - 1 == row_end_position and col_position - 2 == col_end_position) or
                (row_position - 2 == row_end_position and col_position - 1 == col_end_position) or
                (row_position - 2 == row_end_position and col_position + 1 == col_end_position) or
                (row_position - 1 == row_end_position and col_position + 2 == col_end_position) or
                (row_position + 1 == row_end_position and col_position + 2 == col_end_position) or
                (row_position + 2 == row_end_position and col_position + 1 == col_end_position) or
                (row_position + 2 == row_end_position and col_position - 1 == col_end_position) or
                (row_position + 1 == row_end_position and col_position - 2 == col_end_position))

    def _knights_applicable_rules(self, row_position: int, col_position: int):
        rules = []
        if self._valid_position(row_position - 1, col_position - 2):
            rules.append(Rule(row_position - 1, col_position - 2))
        if self._valid_position(row_position - 2, col_position - 1):
            rules.append(Rule(row_position - 2, col_position - 1))
        if self._valid_position(row_position - 2, col_position + 1):
            rules.append(Rule(row_position - 2, col_position + 1))
        if self._valid_position(row_position - 1, col_position + 2):
            rules.append(Rule(row_position - 1, col_position + 2))
        if self._valid_position(row_position + 1, col_position + 2):
            rules.append(Rule(row_position + 1, col_position + 2))
        if self._valid_position(row_position + 2, col_position + 1):
            rules.append(Rule(row_position + 2, col_position + 1))
        if self._valid_position(row_position + 2, col_position - 1):
            rules.append(Rule(row_position + 2, col_position - 1))
        if self._valid_position(row_position + 1, col_position - 2):
            rules.append(Rule(row_position + 1, col_position - 2))
        return rules

    def backtrack(self, pos_init_x: int, pos_init_y: int,
                  pos_final_x: int, pos_final_y: int) -> bool:
        self._laps = 0
        return self._backtrack(pos_init_x, pos_init_y, pos_final_x, pos_final_y, 1)

    def _backtrack(self, row_position: int, col_position: int,
                   row_end_position: int, col_end_position, steps: int) -> bool:
        self.set_value(row_position, col_position, steps)
        if row_position == row_end_position and col_position == col_end_position:
            return True
        rules = self._knights_applicable_rules(row_position, col_position)
        while len(rules) > 0:
            r = self._choose_knights_rule(rules, row_end_position, col_end_position)
            self.set_value(r.row, r.column, steps + 1)
            if self._backtrack(r.row, r.column, row_end_position, col_end_position, steps + 1):
                return True
            self._laps += 1
            self.set_value(r.row, r.column, 0)
        return False

    def to_string(self):
        s = ""
        for i in range(self._count_row):
            for j in range(self._count_col):
                elem = f"{self.get_value(i + 1, j + 1)}"
                space = " " * (4 - elem.__len__())
                s += elem + space
            s += "\n"
        return s
