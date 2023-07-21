def get_drink_by_profession(param):
    x = {"Jabroni": "Patron Tequila",
         "School Counselor": "Anything with Alcohol",
         "Programmer": "Hipster Craft Beer",
         "Bike Gang Member": "Moonshine",
         "Politician": "Your tax dollars",
         "Rapper": "Cristal"}

    return x[param.title()] if param.title() in x else 'Beer'
