class TaTeTi():
    def __init__(self, piece='', board=[], valid=[]):
        self.piece = piece
        self.board = board
        self.valid = valid

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, value):
        self._piece = value

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = {'1.1': '1.1', '1.2': '1.2', '1.3': '1.3',
                       '2.1': '2.1', '2.2': '2.2', '2.3': '2.3',
                       '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'}

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3']

    def __str__(self):
        return "%s|%s|%s\n---+---+---\n%s|%s|%s\n---+---+---\n%s|%s|%s" % (
                self.board['1.1'], self.board['1.2'], self.board['1.3'],
                self.board['2.1'], self.board['2.2'], self.board['2.3'],
                self.board['3.1'], self.board['3.2'], self.board['3.3'])
    
    def input_position(self):
        bandera = True
        while(bandera):
            posicion = str(input('ingrese una posición'))
            if posicion in self.valid:
                print('Ingreso valido')
                self.valid.remove(posicion)
                break
            print('Ingreso invalido')
        return posicion
    
    def win(self):
        tablero = {0: self.board['1.1'], 1: self.board['1.2'], 2: self.board['1.3'],
                   3: self.board['2.1'], 4: self.board['2.2'], 5: self.board['2.3'],
                   6: self.board['3.1'], 7: self.board['3.2'], 8: self.board['3.3']}
        if tablero[0]!='1.1' and tablero[0]==tablero[4] and tablero [4]==tablero[8]:
            return True
        if tablero[2]!='1.3' and tablero[2]==tablero[4] and tablero [4]==tablero[6]:
            return True
        for i in range (0,3):
            if tablero[i] == ' x ' or tablero[i] == ' o ':
                if tablero[i]==tablero[i+3] and tablero[i]==tablero[i+6]:
                    return True
        for i in range (0,7,3):
            if tablero[i] == ' x ' or tablero[i] == ' o ':
                if tablero[i] == tablero[i+1] and tablero[i] == tablero[i+2]:
                    return True
        return False

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            winner = 'Ninguno'
        return winner


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())
