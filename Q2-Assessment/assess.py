#**Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
#input - Oral stories(String)//Determinants(length,moral lessons, age group)
#output- Translation of various stories
#process-Create a class called, create methods and create instances

class Story:
    def __init__(self,title):
        self.title=title
def tell_story(length,moral_lesson,):
        return (self.__class__.__name__)
def story(details):
        return "The story is of {self.length} and of {self.moral_lessons} and for {self.age_group}"

class StoryTeller(Story):
    def __init__(self,name):
     super()(title,moral_lessons)
def tell_story(story):
        return "The story is of {self.length} and of {self.moral_lessons} and for {self.age_group}"
class Translator(Story):
    def __init__(self,language):
        super()(length,moral_lessons,age_group):
        self.language
        if  {self.language}==English:
            return "{Self.language } changes to Kiswahili"
        else
         return "{self.language} remains the same"

story_telling=Story("long","values",4)
story_telling.tell_story("There one was an Ogre that lived in the forest")


# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.
# input- unique ingredients, preparation time, cooking method, nutritional information
# output- The resipes of various cuisines
# process- Create a class with a method of cooking and subclasess that return the recipes
 
unique_ingredients=[]
class African_cuisine:
   def __init__(self,unique_ingredients, preparation_time,cooking_method,nutrirtional_information):
      self.unique_ingredients=unique_ingredients
      self.preparation_time=preparation_time
      self.cooking_method=cooking_method
      self.nutritional_information=nutrirtional_information

def make_food(recipe):
     return(self.__class__.__name__)

class Moroccan_recipe(African_cuisine):
    def make_food(recipe):
        unique_ingredients.append("cumin","cheese")
        return "The type({self.constructor.name} is made of {self.unique_ingredients} with {self.preparation} and of {self.cooking_method} and has this {self.nutritiona_information})"
class Ethiopian_recipe(African_cuisine):
    def make_food(recipe):
        return "The type({self.constructor.name} is made of {self.unique_ingredients} with {self.preparation} and of {self.cooking_method} and has this {self.nutritiona_information})"
class Nigeraian_recipe(African_cuisine):
    def make_food(recipe):
        return "The type({self.constructor.name} is made of {self.unique_ingredients} with {self.preparation} and of {self.cooking_method} and has this {self.nutritiona_information})"

recipe=Moroccan_recipe("cheese",30 minutes,"grill","high vitamins")
recipe.make_food()

# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.
class Species:
    def __init__(self, diet, lifespan, migration):
        self.diet = diet
        self.lifespan = lifespan
        self.migration = migration

class Predator(Species):
    def __init__(self, diet, lifespan, migration, hunting):
        super().__init__(diet, lifespan, migration)
        self.hunting_style = hunting

class Prey(Species):
    def __init__(self, diet, lifespan, migration, herd_size):
        super().__init__(diet, lifespan, migration)
        self.herd_size = herd_size
