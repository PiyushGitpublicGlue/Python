class Recipe:
    def __init__(self, recipe_name):
        self.recipe_name=recipe_name
        self.ingredients  = {}

    def add_ingredient(self, name, amount):
        self.ingredients[name]  = amount

    def scale_recipe(self, factor):
        for name in self.ingredients:
            self.ingredients[name] *= factor

    def show_recipe(self):
        print(self.recipe_name,self.ingredients)

pancakes = Recipe("Pancakes")
pancakes.add_ingredient("Flour (cups)", 1.5)
pancakes.add_ingredient("Eggs", 2)

print("--- Original ---")
pancakes.show_recipe()

print("\n--- Doubled ---")
pancakes.scale_recipe(2)
pancakes.show_recipe()
# Flour should now be 3.0, Eggs should be 4