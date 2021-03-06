import controller as Controller


steps = 0


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# OLD
def ShowTableOld(data):
    colour_line = Bcolors.OKBLUE
    colour_column = Bcolors.OKBLUE
    colour_empty_cell = Bcolors.FAIL

    print(colour_line + ' - - - - - - - - - - - - - - - - - - -' + Bcolors.ENDC)
    idx_row = 0
    for row in data:
        idx_cell = 0
        idx_row += 1
        colour_line = Bcolors.OKBLUE
        if idx_row in [3, 6]:
            colour_line = Bcolors.HEADER
        for cell in row:
            idx_cell += 1
            colour_column = Bcolors.OKBLUE
            if idx_cell in [4, 7]:
                colour_column = Bcolors.HEADER
            if cell == '*':
                print(colour_column + ' | ' + colour_empty_cell + cell + Bcolors.ENDC, end='')
            else:
                print(colour_column + ' | ' + Bcolors.ENDC + cell, end='')
        print(colour_column + ' | ' + Bcolors.ENDC)
        print(colour_line + ' - - - - - - - - - - - - - - - - - - -' + Bcolors.ENDC)


# TODO : add line for each number added; write in a log file
# Show the current state of the sudoku
def ShowTable(data):
    if Controller.SudokuUnfinished:
        print('\n      Table')

        for row in data:
            print(' '.join(row))
        print('')


# Show the current possibilities
def ShowSuggestions(suggestions):
    if suggestions != {}:
        print('Row | Column | Candidates')

        for row in suggestions:
            print(' ', row[0] + 1, '    ', row[1] + 1, '   ', suggestions[row])

        print('')


def ShowStep(suggestion, row, column, message):
    print("Writing down : ", suggestion, " | Row : ", row, " | Column : ", column,
          " | ", message)


def NextStep():
    global steps
    print('\n--- Steps: ' + str(steps) + ' ---')
    steps = steps + 1
    return steps
