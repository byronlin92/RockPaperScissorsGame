from rockpaperscissors.game import Player
import pytest

class TestPlayer():
    @pytest.fixture(scope='module')
    def player(self):
        player = Player('bob')
        return player


    def test_get_name(self, player):
        assert player.get_name() == 'bob'


    def test_move(self, player):
        player.set_move('p')
        assert player.get_move() == 'p'


    def test_set_empty_move(self, player):
        with pytest.raises(ValueError):
            value = None
            player.set_move(value)


    def test_set_empty_name(self):
        with pytest.raises(ValueError):
            value = None
            Player(value)


