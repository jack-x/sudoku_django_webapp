from django.shortcuts import render
from sudoku import Solver
from sudoku import puzzler as Puzzler
from sudoku import builder as Builder

import random


from django.http import HttpResponse
# Create your views here.
solutionGlobal = []
differenceDict = dict()
sudokuDictionaryResponse = dict()

def index(request):
    global solutionGlobal
    global differenceDict
    global sudokuDictionaryResponse

    if request.method == 'POST':
        gettingValue = request.POST.get('solveButton')
        checkingValue = request.POST.get('Submit')
        hintbuttonPress = request.POST.get('hintButton')

        veryEasyButton = request.POST.get('veryEasyButton')
        easyButton = request.POST.get('easyButton')
        mediumButton = request.POST.get('mediumButton')
        hardButton = request.POST.get('hardButton')


        if hintbuttonPress == 'Pressed':
            keyList = list(differenceDict.keys())
            if len(keyList) != 0:
                choice = random.choice(keyList)
                print("replacing this choice {}".format(choice))
                sudokuDictionaryResponse[choice] = differenceDict[choice]

                del differenceDict[choice]
            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)




        if gettingValue == '100GO':

            sudokuWebKeyGen = 'cell'
            sudokuDictionaryResponse = dict()

            for x in range(0,9):
                for y in range(0,9):
                    newKey = sudokuWebKeyGen+str(x)+str(y)
                    if solutionGlobal[x][y] == 0:
                        sudokuDictionaryResponse[newKey] = ' '
                    else:
                        sudokuDictionaryResponse[newKey] = solutionGlobal[x][y]
            sudokuDictionaryResponse["UserSolutionMessage"] = "Full Sudoku Solution Displayed!!"
            sudokuDictionaryResponse['LevelName'] = 'Sudoku Solved'
            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

        if checkingValue == 'submitSudoku':
            print("User has submitted")
            userSolution = dict()
            #extract value from page
            for x in range(0,9):
                for y in range(0,9):
                    userSolution['cell'+str(x)+str(y)] = request.POST.get('cell'+str(x)+str(y))
            print(userSolution)

            #comparison
            flag = True
            for x in range(0,9):
                for y in range(0,9):
                    # print(solutionGlobal)
                    solutionvalue = solutionGlobal[x][y]
                    useranswer = userSolution['cell' + str(x) + str(y)]
                    if str(solutionvalue) != str(useranswer):
                        flag = False
                        break
            if flag == True:
                #user correct solution
                print("User solution is correct")
                sudokuWebKeyGen = 'cell'
                sudokuDictionaryResponse["UserSolutionMessage"] = "Great Job you did it!!"
                for x in range(0,9):
                    for y in range(0,9):
                        newKey = sudokuWebKeyGen+str(x)+str(y)
                        if solutionGlobal[x][y] == 0:
                            sudokuDictionaryResponse[newKey] = ' '
                        else:
                            sudokuDictionaryResponse[newKey] = solutionGlobal[x][y]
                return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

            else:
                print("User solution is false")
                sudokuDictionaryResponse["UserSolutionMessage"] = "Wrong Input! Please try again!!"
                return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)


        if veryEasyButton == 'Pressed':
            levelList = [10,11,12,13,14,15]
            #Clean up the global variables
            solutionGlobal = []
            differenceDict = dict()
            sudokuDictionaryResponse = dict()


            print("Page has been reloaded")
            print("Generating new Puzzle")
            newPuzzle = Puzzler.createSudokuPuzzleWithSolution(random.choice(levelList))

            puzzle = newPuzzle[0]
            solution = newPuzzle[1]
            # global solutionGlobal
            solutionGlobal = solution

            print("Loading Differences")
            #load differences

            for x in range(0,9):
                for y in range(0,9):
                    if puzzle[x][y] == 0:
                        differenceDict['cell'+str(x)+str(y)] = solution[x][y]




            sudokuWebKeyGen = 'cell'

            sudokuDictionaryResponse = dict()

            for x in range(0,9):
                for y in range(0,9):
                    newKey = sudokuWebKeyGen+str(x)+str(y)
                    if puzzle[x][y] == 0:
                        sudokuDictionaryResponse[newKey] = ' '
                    else:
                        sudokuDictionaryResponse[newKey] = puzzle[x][y]
            # print(differenceDict)
            # print(sudokuDictionaryResponse)
            sudokuDictionaryResponse['LevelName'] = 'Level: Very Easy'
            sudokuDictionaryResponse["UserSolutionMessage"] = "Sudoku Load Complete!!"
            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

        if easyButton == 'Pressed':
            levelList = [14,15,16,17,18,19,20,21,22]
            #Clean up the global variables
            solutionGlobal = []
            differenceDict = dict()
            sudokuDictionaryResponse = dict()


            print("Page has been reloaded")
            print("Generating new Puzzle")
            newPuzzle = Puzzler.createSudokuPuzzleWithSolution(random.choice(levelList))

            puzzle = newPuzzle[0]
            solution = newPuzzle[1]
            # global solutionGlobal
            solutionGlobal = solution

            print("Loading Differences")
            #load differences

            for x in range(0,9):
                for y in range(0,9):
                    if puzzle[x][y] == 0:
                        differenceDict['cell'+str(x)+str(y)] = solution[x][y]




            sudokuWebKeyGen = 'cell'

            sudokuDictionaryResponse = dict()

            for x in range(0,9):
                for y in range(0,9):
                    newKey = sudokuWebKeyGen+str(x)+str(y)
                    if puzzle[x][y] == 0:
                        sudokuDictionaryResponse[newKey] = ' '
                    else:
                        sudokuDictionaryResponse[newKey] = puzzle[x][y]
            # print(differenceDict)
            # print(sudokuDictionaryResponse)
            sudokuDictionaryResponse['LevelName'] = 'Level: Easy'
            sudokuDictionaryResponse["UserSolutionMessage"] = "Sudoku Load Complete!!"
            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

        if mediumButton == 'Pressed':
            levelList = [21,22,23,24,25,26,27,28,29,30,31,32]
            #Clean up the global variables
            solutionGlobal = []
            differenceDict = dict()
            sudokuDictionaryResponse = dict()


            print("Page has been reloaded")
            print("Generating new Puzzle")
            newPuzzle = Puzzler.createSudokuPuzzleWithSolution(random.choice(levelList))

            puzzle = newPuzzle[0]
            solution = newPuzzle[1]
            # global solutionGlobal
            solutionGlobal = solution

            print("Loading Differences")
            #load differences

            for x in range(0,9):
                for y in range(0,9):
                    if puzzle[x][y] == 0:
                        differenceDict['cell'+str(x)+str(y)] = solution[x][y]




            sudokuWebKeyGen = 'cell'

            sudokuDictionaryResponse = dict()

            for x in range(0,9):
                for y in range(0,9):
                    newKey = sudokuWebKeyGen+str(x)+str(y)
                    if puzzle[x][y] == 0:
                        sudokuDictionaryResponse[newKey] = ' '
                    else:
                        sudokuDictionaryResponse[newKey] = puzzle[x][y]
            # print(differenceDict)
            # print(sudokuDictionaryResponse)
            sudokuDictionaryResponse['LevelName'] = 'Level: Medium'
            sudokuDictionaryResponse["UserSolutionMessage"] = "Sudoku Load Complete!!"
            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

        if hardButton == 'Pressed':
            levelList = [27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
            #Clean up the global variables
            solutionGlobal = []
            differenceDict = dict()
            sudokuDictionaryResponse = dict()


            print("Page has been reloaded")
            print("Generating new Puzzle")
            newPuzzle = Puzzler.createSudokuPuzzleWithSolution(random.choice(levelList))

            puzzle = newPuzzle[0]
            solution = newPuzzle[1]
            # global solutionGlobal
            solutionGlobal = solution

            print("Loading Differences")
            #load differences

            for x in range(0,9):
                for y in range(0,9):
                    if puzzle[x][y] == 0:
                        differenceDict['cell'+str(x)+str(y)] = solution[x][y]




            sudokuWebKeyGen = 'cell'

            sudokuDictionaryResponse = dict()

            for x in range(0,9):
                for y in range(0,9):
                    newKey = sudokuWebKeyGen+str(x)+str(y)
                    if puzzle[x][y] == 0:
                        sudokuDictionaryResponse[newKey] = ' '
                    else:
                        sudokuDictionaryResponse[newKey] = puzzle[x][y]
            # print(differenceDict)
            # print(sudokuDictionaryResponse)

            sudokuDictionaryResponse['LevelName'] = 'Level: Hard'
            sudokuDictionaryResponse["UserSolutionMessage"] = "Sudoku Load Complete!!"
            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

    #Clean up the global variables
    solutionGlobal = []
    differenceDict = dict()
    sudokuDictionaryResponse = dict()


    print("Page has been reloaded")
    print("Generating new Puzzle")
    newPuzzle = Puzzler.createSudokuPuzzleWithSolution(random.choice([10,11,12,13]))

    puzzle = newPuzzle[0]
    solution = newPuzzle[1]
    # global solutionGlobal
    solutionGlobal = solution

    print("Loading Differences")
    #load differences

    for x in range(0,9):
        for y in range(0,9):
            if puzzle[x][y] == 0:
                differenceDict['cell'+str(x)+str(y)] = solution[x][y]




    sudokuWebKeyGen = 'cell'

    sudokuDictionaryResponse = dict()

    for x in range(0,9):
        for y in range(0,9):
            newKey = sudokuWebKeyGen+str(x)+str(y)
            if puzzle[x][y] == 0:
                sudokuDictionaryResponse[newKey] = ' '
            else:
                sudokuDictionaryResponse[newKey] = puzzle[x][y]
    # print(differenceDict)
    # print(sudokuDictionaryResponse)
    sudokuDictionaryResponse['LevelName'] = 'Level: Easy'
    sudokuDictionaryResponse["UserSolutionMessage"] = "Sudoku Load Complete!!"

    return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

def newHome(request):
    return HttpResponse('Hello Boyz!!')
