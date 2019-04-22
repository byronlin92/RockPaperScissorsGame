from rockpaperscissors.game import *
import pytest
import mock


def test_valid_prompt_player_name():
    valid_name = "bob"
    names = [valid_name]
    with mock.patch('builtins.input', side_effect=names):
        result = Game.prompt_player_name()
        assert result == "bob"


def test_prompt_player_name_empty_then_valid_name():
    valid_name = "bob"
    names = ["", valid_name]
    with mock.patch('builtins.input', side_effect=names):
        result = Game.prompt_player_name()
        assert result == valid_name


def test_valid_prompt_player_move():
    move = "r"
    moves = [move]
    with mock.patch('builtins.input', side_effect=moves):
        assert Game.prompt_player_move() == move


def test_prompt_player_move_empty_then_valid_move():
    valid_move = "s"
    move = ["", valid_move]
    with mock.patch('builtins.input', side_effect=move):
        assert Game.prompt_player_move() == valid_move


def test_prompt_player_move_invalid_then_valid_move():
    valid_move = "s"
    move = ["z", valid_move]
    with mock.patch('builtins.input', side_effect=move):
        assert Game.prompt_player_move() == valid_move


def test_display_winner_tie(capfd):
    Game.display_winner(None)
    out, err = capfd.readouterr()
    assert out == "Game is tied\n"


def test_display_winner_player(capfd):
    name = "Bob"
    player = Player(name)
    Game.display_winner(player)
    out, err = capfd.readouterr()
    assert out == name + " wins\n"


def test_get_random_move():
    assert Game.get_random_move() in Game.RPS


class TestCalculateWinner():
    @pytest.fixture(scope='module')
    def players(self):
        player1 = Player('bob')
        player2 = Player('mark')
        return player1, player2


    def test_calculate_winner_rock_and_rock(self, players):
        player1, player2 = players
        player1.set_move('r')
        player2.set_move('r')
        assert Game.calculate_winner(player1, player2) is None


    def test_calculate_winner_scissor_and_scissor(self, players):
        player1, player2 = players
        player1.set_move('s')
        player2.set_move('s')
        assert Game.calculate_winner(player1,player2) is None


    def test_calculate_winner_paper_and_paper(self, players):
        player1, player2 = players
        player1.set_move('p')
        player2.set_move('p')
        assert Game.calculate_winner(player1, player2) is None


    def test_calculate_winner_rock_and_scissor(self, players):
        player1, player2 = players
        player1.set_move('r')
        player2.set_move('s')
        assert Game.calculate_winner(player1, player2) is player1


    def test_calculate_winner_rock_and_paper(self, players):
        player1, player2 = players
        player1.set_move('r')
        player2.set_move('p')
        assert Game.calculate_winner(player1, player2) is player2


    def test_calculate_winner_scissor_and_rock(self, players):
        player1, player2 = players
        player1.set_move('s')
        player2.set_move('r')
        assert Game.calculate_winner(player1, player2) is player2


    def test_calculate_winner_scissor_and_paper(self, players):
        player1, player2 = players
        player1.set_move('s')
        player2.set_move('p')
        assert Game.calculate_winner(player1, player2) is player1


    def test_calculate_winner_paper_and_rock(self, players):
        player1, player2 = players
        player1.set_move('p')
        player2.set_move('r')
        assert Game.calculate_winner(player1, player2) is player1


    def test_calculate_winner_paper_and_scissor(self, players):
        player1, player2 = players
        player1.set_move('p')
        player2.set_move('s')
        assert Game.calculate_winner(player1, player2) is player2