from recipe_repository import RecipeRepository
from recipe_view import RecipeView
from recipes_controller import RecipesController
from router import Router

view = RecipeView()
repository = RecipeRepository()
controller = RecipesController(repository, view)
router = Router(controller)

router.run()
