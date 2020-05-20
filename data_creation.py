import random
import csv
import os

base_path = os.getcwd()
data_path = base_path + '\\datasets\\'
master_data_list = []

gender = ['Male', 'Female']

# todo add male and female with their own ranges and vary ranges by environment
# idea: add gender and new height and length ranges, maybe include weight? (randomized) then add environment and have that affect the measurements.
# add some over lap

def calculate_base_weight(length):
    # this calculation is based off a rather simple approximate ratio of a female blue whale's weight to her length,
    # the female blue whale is about 32 meters long and weighs about 180,000 KG
    # I recognize that this formula does not take into account the creature's height or limbs (e.g., wings)
    # however, as you would likely need the size of the wings to compute this, we'll leave that off for now
    creature_weight = (length/32) * 180
    return creature_weight


# functions to create data objects
def create_wyvern():
    max_count = 1812
    x = 0
    wings = [2, 4]

    while x <= max_count:
        wyvern = {}
        wyvern['Legs'] = 2
        wyvern['Wings'] = random.choice(wings)
        wyvern['Gender'] = random.choice(gender)
        if wyvern['Gender'] == 'Male':
            wyvern['Length'] = random.randrange(200, 425)
            wyvern['Height'] = random.randrange(125, 225)
        else:
            wyvern['Length'] = random.randrange(250, 600)
            wyvern['Height'] = random.randrange(150, 300)
        wyvern ['Weight'] = calculate_base_weight(wyvern['Length'])
        wyvern['Environment'] = 'volcanoes'
        wyvern['Classification'] = 'Wyvern'

        master_data_list.append(wyvern)
        x += 1


def create_serpent():
    max_count = 2034
    x = 0
    environment = ['air', 'water']

    while x <= max_count:
        serpent = {}
        serpent['Legs'] = 4
        serpent['Wings'] = 0
        serpent['Gender'] = random.choice(gender)
        if serpent['Gender'] == 'Male':
            serpent['Length'] = random.randrange(595, 1035)
            serpent['Height'] = random.randrange(65, 80)
        else:
            serpent['Length'] = random.randrange(695, 1175)
            serpent['Height'] = random.randrange(50, 75)
        serpent['Weight'] = calculate_base_weight(serpent['Length'])
        serpent['Environment'] = random.choice(environment)
        serpent['Classification'] = 'Serpent'

        master_data_list.append(serpent)
        x += 1


def create_flying_serpent():
    max_count = 1618
    x = 0

    while x <= max_count:
        flying_serpent = {}
        flying_serpent['Legs'] = 4
        flying_serpent['Wings'] = 2
        flying_serpent['Gender'] = random.choice(gender)
        if flying_serpent['Gender'] == 'Male':
            flying_serpent['Length'] = random.randrange(575, 925)
            flying_serpent['Height'] = random.randrange(75, 100)
        else:
            flying_serpent['Length'] = random.randrange(675, 1100)
            flying_serpent['Height'] = random.randrange(65, 85)
        flying_serpent['Weight'] = calculate_base_weight(flying_serpent['Length'])
        flying_serpent['Environment'] = 'air'
        flying_serpent['Classification'] = 'Flying Serpent'

        master_data_list.append(flying_serpent)
        x += 1


def create_dragon():
    max_count = 2575
    x = 0
    wings = [2, 4, 6]
    environment = ['mountain', 'volcanoes', 'cave']

    while x <= max_count:
        dragon = {}
        dragon['Legs'] = 4
        dragon['Wings'] = random.choice(wings)
        dragon['Gender'] = random.choice(gender)
        if dragon['Gender'] == 'Male':
            dragon['Length'] = random.randrange(395, 615)
            dragon['Height'] = random.randrange(200, 595)
        else:
            dragon['Length'] = random.randrange(500, 825)
            dragon['Height'] = random.randrange(250, 615)
        dragon['Weight'] = calculate_base_weight(dragon['Length'])
        dragon['Environment'] = random.choice(environment)
        dragon['Classification'] = 'Dragon'

        master_data_list.append(dragon)
        x += 1


def create_drake():
    max_count = 2302
    x = 0
    legs = [2, 4]
    environment = ['desert', 'volcanoes', 'air', 'woods', 'mountain', 'cave']

    while x <= max_count:
        drake = {}
        drake['Legs'] = random.choice(legs)
        drake['Wings'] = 2
        drake['Gender'] = random.choice(gender)
        if drake['Gender'] == 'Male':
            drake['Length'] = random.randrange(175, 225)
            drake['Height'] = random.randrange(90, 150)
        else:
            drake['Length'] = random.randrange(215, 265)
            drake['Height'] = random.randrange(110, 175)
        drake['Weight'] = calculate_base_weight(drake['Length'])
        drake['Environment'] = random.choice(environment)
        drake['Classification'] = 'Drake'

        master_data_list.append(drake)
        x += 1


def create_wyrm():
    max_count = 2021
    x = 0
    environment = ['cave', 'swamp']

    while x <= max_count:
        wyrm = {}
        wyrm['Legs'] = 0
        wyrm['Wings'] = 0
        wyrm['Gender'] = random.choice(gender)
        if wyrm['Gender'] == 'Male':
            wyrm['Length'] = random.randrange(825, 1250)
            wyrm['Height'] = random.randrange(45, 65)
        else:
            wyrm['Length'] = random.randrange(950, 1375)
            wyrm['Height'] = random.randrange(35, 50)
        wyrm['Weight'] = calculate_base_weight(wyrm['Length'])
        wyrm['Environment'] = random.choice(environment)
        wyrm['Classification'] = 'Wyrm'

        master_data_list.append(wyrm)
        x += 1


# function to assign numbers to each creature
def add_numbers(some_list):
    creature_count = 0
    for item in some_list:
        creature_count += 1
        item['Number'] = creature_count


# function to save data to a csv
def create_excel(some_file, some_list):
    with open(data_path + some_file, 'w+', newline='') as f:
        writer = csv.DictWriter(f, ['Number', 'Legs', 'Wings', 'Gender', 'Length', 'Height', 'Weight', 'Environment', 'Classification'])
        writer.writeheader()

        for item in some_list:
            writer.writerow(item)


# calling all functions
create_wyvern()
create_serpent()
create_flying_serpent()
create_dragon()
create_drake()
create_wyrm()

# shuffle the data and split it into a training and test set
random.shuffle(master_data_list)
test_list = master_data_list[-50:]
test_list2 = master_data_list[-35:]
del master_data_list[-50:]

add_numbers(master_data_list)
add_numbers(test_list)
add_numbers(test_list2)

# store the data in spreadsheets
create_excel('creatures_data_set.csv', master_data_list)
create_excel('creatures_test_set.csv', test_list)
create_excel('creatures_test_set2.csv', test_list2)

