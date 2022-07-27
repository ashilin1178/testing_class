from player import Player
import pytest


class TestPlayer:
    def test_change_name(self):
        player = Player('old_name')
        player.change_name('new_name')
        assert player.get_name() == 'new_name', "Ошибка смены имени"

    def test_add_points(self):
        player = Player('1')
        player.add_points(1)
        assert player.get_points() == 1, "Ошибка ошибка добавления очков"

    def test_add_points_zero(self):
        player = Player('2')
        player.add_points(0)
        assert player.get_points() == 0, "Ошибка ошибка добавления очков"

    def test_add_points_minus(self):
        with pytest.raises(TypeError):
            player = Player('3')
            player.add_points('1')
