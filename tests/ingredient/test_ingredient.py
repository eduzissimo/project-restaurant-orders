from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501

INGREDIENT_RESTRICTION = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == INGREDIENT_RESTRICTION
    assert repr(ingredient) == "Ingredient('queijo mussarela')"
    assert hash(ingredient) == hash("queijo mussarela")

    ingredient2 = Ingredient("farinha")
    ingredient3 = Ingredient("farinha")
    ingredient4 = Ingredient("bacon")
    assert ingredient2 == ingredient3
    assert ingredient2 != ingredient4
