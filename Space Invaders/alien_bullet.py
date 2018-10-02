from bullet import Bullet

class Alien_Bullet(Bullet):
    """A subclass of Bullet used exclusively for alien bullets"""

    def __init__(self, ai_settings, screen, alien):
        """Construct alien bullet"""
        # Construct super bullet class
        super().__init__(ai_settings, screen)
        
        # Move bullet to the location of alien
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        # Give ship bullet unique color and speed
        self.color = ai_settings.alien_bullet_color
        self.speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        """Move the alien bullet down the screen"""
        # Adjust y-coordinate position
        self.y += self.speed_factor

        # Set rect position equal to y position
        self.rect.y = self.y
