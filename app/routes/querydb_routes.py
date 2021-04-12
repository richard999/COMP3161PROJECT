from flask import Blueprint
from ..database_functions import Query

import datetime

query_db = Blueprint("query_db", __name__)

start_index = 0
increment_by = 25


@query_db.route('/get_n_recipes')
def get_n_recipes():
    global start_index
    recipes = Query.getNRecipes(start_index, increment_by)
    start_index += increment_by
    return str([recipe['recipe_name'] for recipe in recipes])

@query_db.route('/reset_index')
def reset_index():
    global start_index
    start_index = 0
    return 'Reset'


@query_db.route('/get_all_measurements')
def get_all_measurements():
    query = Query(DBQuery(mysql))
    measurements = Query.getAllMeasurements()
    return str(measurements)

@query_db.route('/get_recipe')
def get_recipe():
   return str(Query.getRecipeByName('low fat berry blue frozen dessert'))

@query_db.route('/get_meal_plan')
def get_meal_plan():

    user = 1
    startDate = datetime.datetime(2021,4,1)
    endDate = datetime.datetime(2021, 4, 1)

    return str(Query.getMealPlan(user,startDate,endDate))

@query_db.route('/generate_lst')
def generate_lst():

    user = 1
    startDate = datetime.datetime(2021,4,1)
    endDate = datetime.datetime(2021, 4, 15)

    return str(Query.generateSupermarketList(user,startDate,endDate))

@query_db.route('/get_ing')
def get_ing():

    return str(Query.getIngredients(38))

@query_db.route('/get_inst')
def get_inst():

    return str(Query.getInstructions(38))

@query_db.route('/get_lst')
def get_lst():

    return str(Query.genLst(38))

