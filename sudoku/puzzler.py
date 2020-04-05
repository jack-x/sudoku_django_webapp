from sudoku.builder import buildSudoku
from sudoku.Solver import solveSudokuConcise,displayGridcmd, positionalListGenerator,displayGridcmdBlankSpace
import random

def createSudokuCopy(sudoku):

    copySudoku = [0]*9
    line = [0,0,0,0,0,0,0,0,0]
    for x in range(0,9):
        copySudoku[x] = list(line)

    for row in range(0,9):
        for column in range(0,9):
            copySudoku[row][column] = sudoku[row][column]

    return copySudoku

def createSudokuPuzzleWithSolution(blanks=10):

    sudoku = buildSudoku()
    # print("NEW SUDOKU")
    # displayGridcmd(sudoku)


    comparisonSudoku = createSudokuCopy(sudoku)

    removedList = []
    numberList = [0,1,2,3,4,5,6,7,8]
    x = 0
    while x < blanks:
        randomRow = random.choice(numberList)
        randomColumn = random.choice(numberList)

        pair = (randomRow,randomColumn)

        if pair in removedList:
            continue
        removedList.append(pair)

        temp = sudoku[randomRow][randomColumn]
        sudoku[randomRow][randomColumn] = 0


        calculationSudoku = createSudokuCopy(sudoku)
        generatePositionList = positionalListGenerator(calculationSudoku)
        solvedSudoku = solveSudokuConcise(generatePositionList)

        if solvedSudoku == comparisonSudoku:
            # sudoku[randomRow][randomColumn] = 0
            #success
            x+=1
            continue
        else:
            #failure
            #rollback
            print("rollback")
            # input()
            removedList.remove(pair)
            sudoku[randomRow][randomColumn] = temp
            continue

    return (sudoku,solvedSudoku)



def createSudokuPuzzle(blanks=10):

    sudoku = buildSudoku()
    # print("NEW SUDOKU")
    # displayGridcmd(sudoku)


    comparisonSudoku = createSudokuCopy(sudoku)

    removedList = []
    numberList = [0,1,2,3,4,5,6,7,8]
    x = 0
    while x < blanks:
        randomRow = random.choice(numberList)
        randomColumn = random.choice(numberList)

        pair = (randomRow,randomColumn)

        if pair in removedList:
            continue
        removedList.append(pair)

        temp = sudoku[randomRow][randomColumn]
        sudoku[randomRow][randomColumn] = 0


        calculationSudoku = createSudokuCopy(sudoku)
        generatePositionList = positionalListGenerator(calculationSudoku)
        solvedSudoku = solveSudokuConcise(generatePositionList)

        if solvedSudoku == comparisonSudoku:
            # sudoku[randomRow][randomColumn] = 0
            #success
            x+=1
            continue
        else:
            #failure
            #rollback
            print("rollback")
            # input()
            removedList.remove(pair)
            sudoku[randomRow][randomColumn] = temp
            continue

    return sudoku


def main():
    newPuzzle = createSudokuPuzzle(57)

    print("NEW PUZZLE")
    displayGridcmdBlankSpace(newPuzzle)

    # displayGridcmd(createSudokuPuzzle(10))

    print("SOLVING THE SUDOKU")
    solution = solveSudokuConcise(positionalListGenerator(newPuzzle))
    displayGridcmd(solution)


if __name__ == "__main__":
    main()
