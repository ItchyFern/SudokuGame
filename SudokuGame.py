import tkinter as tk
import testingstuff2

GRID = testingstuff2.samplegrid1

class Sudoku():
    def __init__(self):
        self.window = tk.Tk()
        self.showGame()
        self.window.mainloop()

    def showGame(self):
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.frame2 = tk.Frame(self.window)
        self.frame2.pack(fill='x')

        self.gridvariable=[]
        quadrant=[]
        for row in range (3):
            temp=[]
            for col in range (3):
                frame = tk.Frame(self.frame, padx=2, pady=2, bg='black')
                frame.grid(row=row, column=col)
                temp.append(frame)
            quadrant.append(temp)

        for row in range (9):
            temp=[]
            for col in range (9):
                variable = tk.StringVar()
                variable.set(' ')
                temp.append(variable)

            self.gridvariable.append(temp)

            count=0
            for col in range (9):
                box=tk.Button(quadrant[row//3][col//3], textvariable=self.gridvariable[row][col],
                              height=1, width=2, relief='ridge',
                              command=lambda x=row, y=col: self.processGridButton(x,y))

                box.grid(row=row,column=col)

        solveButton=tk.Button(self.frame2, text="Solve", command=lambda:self.solve())
        checkButton=tk.Button(self.frame2, text="Check Answer", command=lambda:self.checkSolution())
        solveButton.pack(side='left')
        checkButton.pack(side='right')

        self.fillGame()

    def processGridButton(self, row, col):
        top=tk.Toplevel()
        top.title("Choose Value")

        rowcount=0
        colcount=0
        for x in range (9):
            tk.Button(top, text=str(x+1), height=3, width=6,
                      command=lambda ret=x+1:buttonPress(ret)).grid(row=rowcount,
                                                                    column=colcount)
            colcount+=1
            if ((x+1)/3==1 or (x+1)/3==2):
                rowcount+=1
                colcount=0
        tk.Button(top, text="Clear", height=1, width=6,
                      command=lambda: buttonPress(" ")).grid(row=3, column=2)
        def buttonPress(x):
            self.setGridButton(row, col, x)
            top.destroy()

    def setGridButton(self, row, col, val):
        self.gridvariable[row][col].set(val)


    def fillGame(self):
        for row in range (9):
            for col in range (9):
                if (not GRID[row][col] == 0):
                    self.gridvariable[row][col].set(str(GRID[row][col]))

    def fillGameSolved(self):
        grid=testingstuff2.solve(GRID)
        for row in range (9):
            for col in range (9):
                self.gridvariable[row][col].set(str(grid[row][col]))


    def checkSolution(self):
        grid=[]
        for row in range (9):
            temp=[]
            for col in range (9):
                temp.append(str(self.gridvariable[row][col].get()))
            grid.append(temp)

        if (testingstuff2.isValidSolution(grid)):
            print ("Congratulations")
        else:
            print ("Incorrect, keep trying")

    def solve(self):
        self.fillGameSolved()






game=Sudoku()
