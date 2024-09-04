class Button(pygame.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.smallFont.render(text, True, window.colors["black"])
        self.image = pygame.Surface((self.text_surf.get_width()+40,
                                 self.text_surf.get_height()+20))
        self.image.fill(window.colors["green"])
        # Now blit the text onto the self.image.
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)
