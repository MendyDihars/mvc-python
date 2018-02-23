from recipe import Recipe

class RecipesController:

  def __init__(self, repository, view):
    self.repository = repository
    self.view = view

  def list(self):
    print self.repository.all()
    self.view.display_list(self.repository.all())

  def create(self):
    hash_recipe = self.view.ask_user_creation()
    recipe = Recipe({ "name": hash_recipe["name"], "content": hash_recipe["content"] })
    self.repository.add(recipe)
