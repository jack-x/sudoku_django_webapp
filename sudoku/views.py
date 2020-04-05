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
        checkingValue = request.POST.get('checkPuzzle')
        hintbuttonPress = request.POST.get('hintButton')

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

            return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)


    newPuzzle = Puzzler.createSudokuPuzzleWithSolution(40)

    puzzle = newPuzzle[0]
    solution = newPuzzle[1]
    # global solutionGlobal
    solutionGlobal = solution

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
    print(differenceDict)
    print(sudokuDictionaryResponse)
    return render(request,'sudoku/home.html',context = sudokuDictionaryResponse)

def newHome(request):
    return HttpResponse('Hello Boyz!!')
