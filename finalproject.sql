DROP DATABASE IF EXISTS mealdb;

CREATE DATABASE mealdb;

USE  mealdb;

create table `User`(
    UserId int auto_increment not null,
    Fname varchar(20),
    Lname varchar(20),
    email VARCHAR(30),
    `password` VARCHAR(30),
    address VARCHAR(255),
    primary key(UserId)
    );

create table MealPlan(
    MPID int auto_increment not null,
    UserId int,
    primary key(MPID, UserId),
    Constraint foreign key(UserId) references User(UserId) on delete cascade on update cascade
    );

create table Measurements(
    MeasuremeId int auto_increment not null,
    Quantity int,
    MeasureID int,
    primary key(MeasureID),  
    
);

create table Ingredients(
    IngId int auto_increment not null,
    IngredientId int,
    Calories int,
    primary key(IngId)

);
create table ShoppingList(
    SLID int auto_increment not null,
    IngId int,
    MeasureID int,
    primary key(SLID, IngId)
    Constraint foreign key(IngId) references Ingredients(IngId) on delete cascade on update cascade
);

create table KitchenStock(
    KSID int,
    IngId int,
    MeasureID int,
    primary key(KSID, IngId, MeasureID)
    Constraint foreign key(IngId) references Ingredients(IngId) on delete cascade on update cascade
    Constraint foreign key(MeasureID) references Measurements(MeasureID) on delete cascade on update cascade
    );


create table Meal(
    MealId int auto_increment not null,
    Image varbinary(max),
    primary key(MealId)
    );

create table Recipe(
    RecipeID int auto_increment not null,
    RecipeName varchar(35),
    Total_calories int,
    Description varchar(100),
    Date_Created Date,
    primary key(RecipeID)

    );

create table RecipeInstruction(
    RecipeID int,
    StepNumber int,
    Instruction varchar(200)
    primary key(RecipeID)
    Constraint foreign key(RecipeID) references Recipe(RecipeID) on delete cascade on update cascade

    );





