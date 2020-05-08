class House:
    def __init__(self, household_type, total_area):
        self.household_type = household_type
        self.total_area = total_area
        self.remaining_area = total_area
        self.furniture_list = []

    def __str__(self):
        
        return f'House type: {self.household_type}, total are: {self.total_area} square meters,\
 remaining area: {self.remaining_area} square meters, furniture: {self.furniture_list}.'

    def add_item(self, item):
        if item.area > self.remaining_area:
            print(f'{item.name} is too large to add')
        else:
            self.furniture_list.append(item.name)
            self.remaining_area -= item.area

class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    
    def __str__(self):
        return f'The {self.name} occupies {self.area} square meters'




elite_appartement = House('flat', 60)

bed = Furniture('Bed', 4)
wardrobe = Furniture('Wardrobe', 2)
table = Furniture('Table', 1.5)

elite_appartement.add_item(bed)
elite_appartement.add_item(wardrobe)
elite_appartement.add_item(table)

print(table)
print(wardrobe)
print(bed)
print(elite_appartement)
        