# Python tic-tac-toe
# 2/8/2022

import tkinter as tk

# Globals
player = 1
buttons = []
playerLabel = tk.Label()

board = [""]*9
idx = 0

# Game Logic
class Logic():

    def checkHorizontal(self):
        global board

        rowOne, rowTwo, rowThree = False, False, False

        if ('' not in board[:3]):
            rowOne = board[0] == board[1] == board[2]
            if (rowOne):
                return True
        if ('' not in board[3:6]):
            rowTwo = board[3] == board[4] == board[5]
            if (rowTwo):
                return True
        if ('' not in board[6:8]):
            rowThree = board[6] == board[7] == board[8]
            if (rowThree):
                return True

        return False

    def checkVertical(self):
        global board

        tmp = [board[0], board[3], board[6]]

        if ('' not in tmp):
            if (tmp[0] == tmp[1] == tmp[2]):
                return True

        tmp = [board[1], board[4], board[7]]

        if ('' not in tmp):
            if (tmp[0] == tmp[1] == tmp[2]):
                return True
                
        tmp = [board[2], board[5], board[8]]

        if ('' not in tmp):
            if (tmp[0] == tmp[1] == tmp[2]):
                return True

        return False

    def checkDiagonal(self):
        global board

        tmp = [board[0], board[4], board[8]]
        if ('' not in tmp):
                if (tmp[0] == tmp[1] == tmp[2]):
                    return True

        tmp = [board[2], board[4], board[6]]
        if ('' not in tmp):
                if (tmp[0] == tmp[1] == tmp[2]):
                    return True

        return False
    
    def checkWinner(self):
        global player

        h = self.checkHorizontal()
        v = self.checkVertical()
        d = self.checkDiagonal()

        if (h or d or v):
            return True
        elif ("" not in board):
            player = 3

        return False

# GUI
class App(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        global idx
        global playerLabel

        playerLabel = tk.Label(text="Player 1 (X)")
        restart = tk.Button(text='R', height=1, width=2, command=lambda: App.restart())
        quit = tk.Button(text='Q', height=1, width=2, command=self.quit)

        # Buttons for X & O
        for x in range(3):
            for y in range(3):
                buttons.append(tk.Button(text="",
                    height=4, width=8,
                    command=lambda btn=idx: App.changeVal(btn)
                    ))
                buttons[idx].grid(row=x+1, column=y, pady=2, padx=2)
                idx += 1

        playerLabel.grid(row=0, column=1)   
        restart.grid(row=0, column=0, pady=4)
        quit.grid(row=0, column=2, pady=4)

    # Change current grid value based on player
    def changeVal(button):
        global player
        global playerLabel

        # Taken spots are skipped
        if (board[button] == ""):
            if (player == 1):
                board[button] = "X"
                buttons[button].configure(text='X')
                player = 2
                playerLabel.configure(text="Player 2 (O)")

            else:
                board[button] = "O"
                buttons[button].configure(text='O')
                player = 1
                playerLabel.configure(text="Player 1 (X)")
        
            # Check for winner or a tie
            l = Logic()
            if (l.checkWinner()):
                for i in buttons:
                    i['state'] = tk.DISABLED

                if (player == 2):
                    playerLabel.configure(text="Player 1 Won!")

                elif (player == 1):
                    playerLabel.configure(text="Player 2 Won!")

                else:
                    playerLabel.configure(text="It's a tie!")

    # Restart the game board
    def restart():
        global player
        global board

        player = 1
        playerLabel.configure(text="Player 1 (X)")
        for i in buttons:
            i['state'] = tk.ACTIVE
            i['text'] = ""
        for i in range(9):
            board[i] = ""

def main():
    app = App()
    app.master.title('Tic-Tac-Toe')
    app.mainloop()

if __name__ == "__main__":
    main()