import random


class Player():
    def __init__(self, name):
        if name is None:
            raise ValueError("Player name is none")
        self._name = name


    def get_name(self):
        return self._name


    def set_move(self, move):
        if move is None:
            raise ValueError("Player move is none")
        self._move = move


    def get_move(self):
        return self._move



class Game():
    RPS = ("r", "s", "p")
    moves_beaten_by = {'r': 's',
                       'p': 'r',
                       's': 'p'}

    def __init__(self):
        print("Welcome to Tic Tac Toe")

        name = Game.prompt_player_name()
        player1 = Player(name)
        player2 = Player("Computer")
        print(player1.get_name() + ' has entered the game')
        print(player2.get_name() + ' has entered the game')

        move = Game.prompt_player_move()
        player1.set_move(move)
        player2.set_move(Game.get_random_move())
        print(player1.get_name() + "'s move: " + player1.get_move())
        print(player2.get_name() + "'s move: " + player2.get_move())

        player = Game.calculate_winner(player1, player2)
        Game.display_winner(player)


    @staticmethod
    def get_random_move():
        return random.choice(Game.RPS)


    @staticmethod
    def display_winner(player):
        if (player == None):
            print("Game is tied")
        else:
            print(player.get_name() + " wins")


    @staticmethod
    def prompt_player_move():
        move = input("Please choose Rock, Paper, or Scissors by typing letter 'r', 'p', or 's': ")
        while move not in Game.RPS:
            move = input("That move is incorrect, please choose Rock, Paper, or Scissors by typing letter 'r', 'p', or 's': ")
        return move


    @staticmethod
    def prompt_player_name():
        name = input("Please enter your name: ")
        while not name:
            name = input("Please enter a valid name (must include letters): ")
        return name


    @staticmethod
    def calculate_winner(player1, player2):
        if player1.get_move() == player2.get_move():
            return None
        elif player1.get_move() in Game.moves_beaten_by[player2.get_move()]:
            return player2
        elif player2.get_move() in Game.moves_beaten_by[player1.get_move()]:
            return player1


if __name__ == '__main__':
    game = Game()