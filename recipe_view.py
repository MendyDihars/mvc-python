class RecipeView:

  def display_list(self, recipes):
    print recipes
    if recipes:
      for recipe in recipes:
        print "ID: %s | %s - %s" % (recipe.id, recipe.name, recipe.content)

  def ask_user_creation(self):
    print "What's your recipe's name"
    name = raw_input("Name: ")
    print "What's your recipe's content"
    content = raw_input("Content: ")
    return { "name": name, "content": content }
