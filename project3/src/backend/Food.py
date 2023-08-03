class Food:
    def __init__(
        self, name, brand, url, servingSize, energy, fat, sugar, protein, fiber, sodium
    ):
        self.name = name
        self.brand = brand
        self.url = url
        self.servingSize = servingSize
        self.energy = energy
        self.fat = fat
        self.sugar = sugar
        self.protein = protein
        self.fiber = fiber
        self.sodium = sodium
        self.dailyfatpercent = 0
        self.dailyproteinpercent = 0
        self.dailyfiberpercent = 0
        self.dailysodiumpercent = 0

    def to_dict(self):
        foodDict = {"name" : self.name, "brand": self.brand, "url" : self.url, 
                    "serving_size" : self.servingSize, "energy" : self.energy,
                    "fat" : self.fat, "sugar" : self.sugar, "protein" : self.protein,
                    "fiber" : self.fiber, "sodium" : self.sodium, "dailyfatpercent" : self.dailyproteinpercent,
                    "dailyproteinpercent" : self.dailyproteinpercent,"dailyfiberpercent" : self.dailyfiberpercent,
                    "dailysodiumpercent" : self.dailysodiumpercent,}

        return foodDict

