# TODO: описать базовый класс
class OnlineShooter:
    """
    Базовый класс для онлайн-шутеров.
    """

    def __init__(self, title, developer, release_year,
                 platforms, player_count=0):
        """
        Конструктор класса OnlineShooter.

        Args:
            title: Название игры.
            developer: Разработчик игры.
            release_year: Год выпуска игры.
            platforms: Список платформ,
                       на которых доступна игра.
            player_count: Количество игроков онлайн
                          (по умолчанию 0).
        """
        self.title = title
        self.developer = developer
        self.release_year = release_year
        self.platforms = platforms
        self._player_count = player_count

    def __str__(self):
        """
        Возвращает строковое представление
        объекта OnlineShooter.
        """
        return (f"{self.title} ({self.release_year}), "
                f"разработчик: {self.developer}, "
                f"платформы: {', '.join(self.platforms)}, "
                f"игроков онлайн: {self._player_count}")

    def __repr__(self):
        """
        Возвращает представление
        объекта OnlineShooter в виде
        строки для разработчиков.
        """
        return (
            f"OnlineShooter(title='{self.title}', "
            f"developer='{self.developer}', "
            f"release_year={self.release_year}, "
            f"platforms={self.platforms}, "
            f"player_count={self._player_count})"
        )

    def get_player_count(self):
        """Возвращает текущее количество
        игроков онлайн."""
        return self._player_count

    def increase_players(self, count):
        """Увеличивает количество игроков онлайн."""
        self._player_count += count

    def decrease_players(self, count):
        """Уменьшает количество игроков онлайн."""
        if self._player_count - count > 0:
            self._player_count -= count
        else:
            self._player_count = 0


# TODO: описать дочерний класс
class TacticalShooter(OnlineShooter):
    """
    Дочерний класс для тактических шутеров,
    наследуется от OnlineShooter.
    """

    def __init__(self, title, developer,
                 release_year, platforms,
                 player_count=0, team_size=5,
                 game_mode="5v5"):
        """
        Конструктор класса TacticalShooter.
        Расширяет конструктор базового класса.

        Args:
            title: Название игры.
            developer: Разработчик игры.
            release_year: Год выпуска игры.
            platforms: Список платформ,
                       на которых доступна игра.
            player_count: Количество игроков онлайн
                          (по умолчанию 0).
            team_size: Размер команды в игре.
            game_mode: Игровой режим.
        """
        super().__init__(title, developer,
                         release_year, platforms,
                         player_count)
        self.team_size = team_size
        self.game_mode = game_mode

    def __str__(self):
        """
        Возвращает строковое представление
        объекта TacticalShooter.
        Перегружает метод __str__ базового
        класса, добавляя специфичную
        информацию.
        """
        return (f"{super().__str__()} (тактический "
                f"шутер, режим: {self.game_mode}, "
                f"размер команды: {self.team_size})")

    def __repr__(self):
        """
        Возвращает представление
        объекта TacticalShooter в виде
        строки для разработчиков.
        Перегружает метод __repr__ базового
        класса, добавляя специфичную
        информацию.
        """
        return (
            f"TacticalShooter(title='{self.title}', "
            f"developer='{self.developer}', "
            f"release_year={self.release_year}, "
            f"platforms={self.platforms}, "
            f"player_count={self._player_count}, "
            f"team_size={self.team_size}, "
            f"game_mode='{self.game_mode}')"
        )

    def get_team_size(self):
        """Возвращает размер команды."""
        return self.team_size

    def increase_players(self, count):
        """
        Увеличивает количество игроков онлайн.
        Перегружает метод базового класса,
        добавляя специфичную логику
        (проверка размера команды).

        Причина перегрузки:
        Необходимо проверить, что после
        добавления игроков их количество
        останется кратным размеру команды.
        Если количество игроков не кратно
        размеру команды, количество онлайн
        игроков сбрасывается.
        """
        new_count = self._player_count + count
        if new_count % self.team_size == 0:
            self._player_count = new_count
        else:
            self._player_count = 0
