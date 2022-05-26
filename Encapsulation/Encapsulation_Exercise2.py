class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.name = name
        self.medium = medium
        self.style = style
        self.famous_artwork = famous_artwork

my_artist = Artist("Bill Watterson", "ink and paper", "cartoons", "Calvin and Hobbes")
print(my_artist.name)
