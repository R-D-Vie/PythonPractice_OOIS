class Chef:
  def __init__(self, name, cuisine, stars):
    self.name = name
    self.cuisine = cuisine
    self.michelin_stars = stars
    
  def compare(self, other_chef):
   if self.michelin_stars > other_chef.michelin_stars:
       return f"{self.name}, who specialises in {self.cuisine} food, has more michelin stars than {other_chef.name}."
   else:
       return f"{self.name}, who specialises in {self.cuisine} food, does not have more michelin stars than {other_chef.name}."

marco = Chef('Marco Pierre White', 'French, British', 3)
rene = Chef('Rene Redzepi', 'Nordic', 2)

print(marco.compare(rene))
print(rene.compare(marco))