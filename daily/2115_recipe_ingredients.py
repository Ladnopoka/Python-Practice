from typing import List

# Solution class with findAllRecipes method
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        my_recipes = recipes.copy()
        recipes_to_remove = set()
        supplies_set = set(supplies)

        while True:
            found_new_recipe = False

            for i in range(len(my_recipes)):
                in_supplies = True
                my_recipe = my_recipes[i]
                
                for ingredient in ingredients[i]:
                    if ingredient not in supplies_set:
                        in_supplies = False
                        break
            
                if in_supplies:
                    found_new_recipe = True
                    supplies_set.add(my_recipe)
                    recipes_to_remove.add(my_recipe)

            my_recipes = [r for r in my_recipes if r not in recipes_to_remove]
            recipes_to_remove.clear()

            if not found_new_recipe:
                break

        return [recipe for recipe in recipes if recipe in supplies_set]


# Main function
def main():
    # recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
    # ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
    # supplies = ["f","hveml","cpivl","d"]

    recipes = ["burger", "sandwich", "bread"]
    ingredients = [["sandwich","meat","bread"], ["bread","meat"], ["yeast","flour"]]
    supplies = ["yeast","flour","meat"]
    
    # Output: ["bread","sandwich","burger"]

    # Create Solution instance without arguments and call method with arguments
    sol = Solution()
    result = sol.findAllRecipes(recipes, ingredients, supplies)
    print(result)

# Run the script
if __name__ == "__main__":
    main()