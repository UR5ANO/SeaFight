class Ship:

    def __init__(self, paluby):
        self.num_palub = len(paluby)
        self.paluby = paluby
        self.alive = [True] * self.num_palub

    def proverka_celostnosti(self):
        pass

    def vystrel(self,cell):
        if cell in self.paluby:
            self.alive[self.paluby.index(cell)] = False

    def status(self):
        if all(self.alive):
            return 'Giv'
        elif any(self.alive):
            return 'Ranen'
        else:
            return 'Ubit'


class Board:

    def __init__(self):
        self.field = [[False] * 10] * 10
        self.ships = []
        self.pologenie = {}
        self.count = {i: 5-i for i in range(1, 5)}

    def add_ship(self, ship: Ship):
        if self.count[ship.num_palub] > 0:
            self.count[ship.num_palub] -= 1
            self.ships.append(ship)
            for p in ship.paluby:
                self.pologenie[p] = len(self.ships) - 1


board = Board()

ship1 = Ship(['b2','c2','c3','b3'])
board.add_ship(ship1)
ship2 = Ship(['e1'])
