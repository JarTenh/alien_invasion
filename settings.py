class Settings:
    """
    A class to store all settings for Alien Invasion.
    """

    def __init__(self) -> None:
        """
        Initialize the game settings.
        """
        # Screen settings.
        self.screen_width = 1050
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.speed = 2.5

        # Bullet settings.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
