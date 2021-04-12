from .DB import DB
from .conversions import convert
from mysql.connector import errors

class DBQuery(DB):

    def __init__(self, mysql):
        super().__init__(mysql)

    def getAllMeasurments(self):
        measurements = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM measurement''')
            measurements = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return measurements
    
    def getUser(self, id, username):
        user = {}
        try:
            self._start_conn()
            query = "SELECT * FROM user WHERE Email=%(Email)s or user_id=%(id)s"
            self.cur.execute(query, {'Email':Email, 'id':id})
            user = self.cur.fetchone()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return user

    def getRecipesOfCalCount(self):
        recipes = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM recipe''')
            recipes = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return recipes

    def getRecipe(self, recipeId):
        recipe = {}
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM recipe WHERE recipe_id={}'''.format(recipeId))
            recipe = self.cur.fetchone()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return recipe

    def getRecipeByName(self, recipeName):
        recipes = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM recipe WHERE recipe_name like '%{}%' ORDER BY LIMIT 50 '''.format(recipeName))
            recipes = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return recipes

    def getNRecipes(self, start, end):
        recipes = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM recipe LIMIT {},{}'''.format(start, end))
            recipes = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return recipes

    def getInstructionForRecipe(self, recipeId):
        instructions = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM instruction WHERE recipe_id={}'''.format(recipeId))
            instructions = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return instructions

    

    def getUserById(self, userId):
        user = {}
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM user WHERE user_id={}'''.format(userId))
            user = self.cur.fetchone()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return user

    def getMealsForDate(self, userId, date):
        meals = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM meal_plan JOIN recipe ON meal_plan.recipe_id=recipe.recipe_id\
                                WHERE user_id={} AND consumption_date='{}' '''.format(userId,date))
            meals = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return meals

    def getMealInRange(self, userId, startDate, endDate):
        meals = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM meal_plan JOIN recipe ON meal_plan.recipe_id=recipe.recipe_id WHERE user_id={}\
                                AND consumption_date >= '{}' AND consumption_date <= '{}' ORDER BY consumption_date,type_of_meal ASC  '''.\
                            format(userId, startDate, endDate))
            meals = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return meals

    def getMaxRecipeId(self):
        self._start_conn()
        self.cur.execute('''SELECT MAX(recipe_id) AS recipe_id FROM recipe''')
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe['recipe_id']

    def getMaxUserId(self):
        self._start_conn()
        self.cur.execute('''SELECT MAX(user_id) AS user_id FROM user''')
        recipe = self.cur.fetchone()
        self._close_conn()
        return recipe['user_id']

    def getMyStock(self, userId):
        stock = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT * from Kitchen_Stock JOIN ingredient ON kitchen_stock.ing_id=food_item.ing_id \
            WHERE Kitchen_Stock.user_id={}'''.format(userId))
            stock = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return stock

    def getCalCount(self,recipeId):
        ingredients = []
        try:
            ingredients = self.getIngredientsForRecipe(recipeId)
            calCount = 0
            for ing in ingredients:
                calCount += convert(ing['units'],float(ing['quantity']),float(ing['calories_per_ml']),float(ing['calories_per_g']))
        except errors.Error as e:
            print(e)
        finally:
            return calCount

    def generateSupermarketList(self,recipeId):
        foods = []
        try:
            self._start_conn()
            self.cur.execute('''SELECT food_item.food_name FROM ingredients_in_recipes JOIN food_Item ON ingredients_in_recipes.food_id=\
                    food_item.food_id WHERE ingredients_in_recipes.recipe_id={}'''.format(recipeId))
            foods = self.cur.fetchall()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return foods

    def getRandomRecipe(self):
        recipe = {}
        try:
            self._start_conn()
            self.cur.execute('''SELECT * FROM recipe ORDER BY RAND() LIMIT 1''')
            recipe = self.cur.fetchone()
            self._close_conn()
        except errors.Error as e:
            print(e)
        finally:
            return recipe