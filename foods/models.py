from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):

    ingredients_list = (
        ('Sourdough', 'Sourdough'),
        ('Chocolate Chips', 'Chocolate Chips'),
        ('Biscuit Dough', 'Biscuit Dough'),
        ('Penaut Butter', 'Penaut Butter'),
        ('Almond Butter', 'Almond Butter'),
        ('Rice Krispies', 'Rice Krispies'),
        ('Macarpone Cream', 'Macarpone Cream'),
        ('Cinnammon', 'Cinnammon'),
        ('Espresso', 'Espresso'),
        ('Baking Powder', 'Baking Powder'),
        ('Baking Soda', 'Baking Soda'),
        ('Vanilla Ice Cream', 'Vanilla Ice Cream'),
        ('Sprinkles', 'Sprinkles'),
        ('Coconut Flakes', 'Coconut Flakes'),
        ('Coconut Oil', 'Coconut Oil'),
        ('Vanilla Extract', 'Vanilla Extract'),
        ('Bananas', 'Bananas'),
        ('Oats', 'Oats'),
        ('Eggs', 'Eggs'),
        ('BlueBerry', 'Blueberry'),
        ('Carrots', 'Carrots'),
        ('Scoth Bonnet', 'Scoth Bonnet'),
        ('Custard', 'Custard'),
        ('Apples', 'Apples'),
        ('Pumkin', 'Pumkin'),
        ('Basil', 'Basil'),
        ('Cheese', 'Cheese'),
        ('Cornstarch', 'Cornstarch'),
        ('Tequila', 'Tequila'),
        ('Limes', 'Limes'),
        ('Milk', 'Milk'),
        ('Whole Milk', 'Whole Milk'),
        ('Skim Milk', 'Skim Milk'),
        ('Almond Milk', 'Almond Milk'),
        ('Food Coloring', 'Food Coloring'),
        ('Pecans', 'Pecans'),
        ('Avocados', 'Avocados'),
        ('Maple Syrup', 'Maple Syrup'),
        ('Taco Shells', 'Taco Shells'),
        ('Minced Beef', 'Minced Beef'),
        ('Pork Roast', 'Pork Roast'),
        ('Pork Chops', 'Pork Chops'),
        ('Pork Belly', 'Pork Belly'),
        ('Pork Tenderloin', 'Pork Tenderloin'),
        ('Pork Ribs', 'Pork Ribs'),
        ('Beef Ribs', 'Beef Ribs'),
        ('Potato', 'Potato'),
        ('Sliced Ham', 'Sliced Ham'),
        ('Breadcrumbs', 'Breadcrumbs'),
        ('Honey', 'Honey'),
        ('Cream Cheese', 'Cream Cheese'),
        ('Olive Oil', 'Olive Oil'),
        ('Mozzarella', 'Mozzarella'),
        ('Red Pepper Flakes', 'Red Pepper Flakes'),
        ('Ground Black Pepper', 'Ground Black Pepper'),
        ('Garlic', 'Garlic'),
        ('Ginger', 'Ginger'),
        ('Thyme', 'Thyme'),
        ('Cumin', 'Cumin'),
        ('Onion', 'Onion'),
        ('Tomatoes', 'Tomatoes'),
        ('Crushed Tomatoes', 'Crushed Tomatoes'),
        ('Jalapeño', 'Jalapeño'),
        ('Brie', 'Brie'),
        ('Gouda', 'Gouda'),
        ('Provolone', 'Provolone'),
        ('Parmasean', 'Parmasean'),
        ('Feta', 'Feta'),
        ('Cheese Mix', 'Cheese Mix'),
        ('Bell Peppers', 'Bell Peppers'),
        ('Tortilla', 'Tortilla'),
        ('Baguettes', 'Baguettes'),
        ('Sweet Potato', 'Sweet Potato'),
        ('Condensed Milk', 'Condensed Milk'),
        ('Heavy Cream', 'Heavy Cream'),
        ('Wafer Cookies', 'Wafer Cookies'),
        ('Sugar', 'Sugar'),
        ('Salt', 'Salt'),
        ('Walnuts', 'Walnuts'),
        ('Granola', 'Granola'),
        ('Parsley', 'Parsley'),
        ('Chicken Breast','Chicken Breast'),
        ('Chicken Thigh','Chicken Thigh'),
        ('Chicken Legs','Chicken Legs'),
        ('Chicken Wings','Chicken Wings'),
        ('Oysters','Oysters'),
        ('Shrimp','Shrimp'),
        ('Salmon','Salmon'),
        ('Icing Sugar','Icing Sugar'),
        ('Lemons','Lemons'),
        ('Fondant','Fondant'),
        ('Tumeric','Tumeric'),
        ('Edible Flowers', 'Edible Flowers'),
        ('All Purpose Flour','All Purpose Flour'),
        ('Whole Wheat Flour','Whole Wheat Flour'),
        ('Cake Flour','Cake Flour'),
        ('Pastry Flour','Pastry Flour'),
        ('Almond Flour','Almond Flour'),
        ('Butter', 'Butter'),
        ('Sativa', 'Sativa'),
        ('Gluten Free Flour', 'Gluten Free Flour'),
        ('Basmati Rice', ' Basmati Rice'),
        ('White Rice', ' White Rice'),
        ('Whole Wheat Rice', ' Whole Wheat Rice'),
        ('Spaghetti', ' Spaghetti'),
        ('Rice', ' Rice'),
        ('Ham', ' Ham'),
        ('Jamón ibérico', ' Jamón ibérico'),
        ('Thai Green Curry Paste', ' Thai Green Curry Paste'),
        ('Raisins', 'Raisins'),
        ('Warm Water', 'Warm Water'),
        ('Dry Yeast', 'Dry Yeast'),
        ('Sea Salt', 'Sea Salt'),

    )

    prep_time_list = (
        ('10 Minutes', '10 Minutes'),
        ('15 Minutes', '15 Minutes'),
        ('20 Minutes', '20 Minutes'),
        ('30 Minutes', '30 Minutes'),
        ('40 Minutes', '40 Minutes'),
        ('50 Minutes', '50 Minutes'),
        ('60 Minutes', '60 Minutes'),
        ('1 hr 10 minutes', '1 hr 10 minutes'),
    )

    category = (
        ('Cakes', 'Cakes'),
        ('Salads', 'Salads'),
        ('Desserts', 'Desserts'),
        ('Breakfast', 'Breakfast'),
        ('Dinner', 'Dinner'),
        ('Workouts', 'Workouts'),
        ('for_kids', 'for_kids'),
    )

    recipe_title = models.CharField(max_length=300)
    description = RichTextField()
    description1 = RichTextField(default="")
    description2 = RichTextField(default="", blank=True)
    description3 = RichTextField(default="", blank=True)
    description4 = RichTextField(default="", blank=True)
    article_title = models.CharField(max_length=300, default="")
    description_short = RichTextField(default="")
    food_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    food_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    food_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    owner = models.CharField(max_length=200)
    igredients = MultiSelectField(choices=ingredients_list)
    prep_time = models.CharField(choices=prep_time_list, max_length=200, default="")
    is_salad = models.BooleanField(default=False)
    is_cake = models.BooleanField(default=False)
    is_dessert = models.BooleanField(default=False)
    is_breakfast = models.BooleanField(default=False)
    is_dinner = models.BooleanField(default=False)
    is_workout = models.BooleanField(default=False)
    is_lunch = models.BooleanField(default=False)
    is_for_kids = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_for_home_page = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    is_holiday_recipe = models.BooleanField(default=False)
    is_featured_for_home_page = models.BooleanField(default=False)
    is_for_slider = models.BooleanField(default=False)
    is_for_slider2 = models.BooleanField(default=False)
    is_for_home_page_side = models.BooleanField(default=False)

    def __str__(self):
        return self.recipe_title

class Dashboard(models.Model):
    food_title = models.CharField(max_length=300, default="", editable=False)
    user_id = models.IntegerField()
    food_id = models.IntegerField()
    food_photo = models.ImageField(blank=True)
    food_description = models.TextField(null=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __int__(self):
        return self.food_title

class Comment(models.Model):

    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=200,  blank=True)
    food_id = models.IntegerField()
    comments = models.TextField()
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
