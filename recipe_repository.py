class RecipeRepository:

  def __init__(self):
    self.recipes = []
    self.next_id = 1

  def add(self, recipe):
    recipe.get_id(self.next_id)
    self.recipes.append(recipe)
    self.next_id += 1

  def all(self):
    self.recipes

  def find(self, id):
    for recipe in self.recipes:
      if recipe.id == id: return recipe
