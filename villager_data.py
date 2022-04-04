"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    
    species = set()
    open_file = open(filename)
    for i in open_file:
        words = i.split('|')
        specie = words[1]
        species.add(specie)

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    open_file = open(filename)
    for line in open_file:
        words = line.split('|')
        name = words[0]
        specie = words[1] 
        if search_string == "All" or specie == search_string:
            villagers.append(name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
 
    hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    names = [[] for i in range(len(hobbies))] 
    open_file = open(filename)
   
    for line in open_file:
        words = line.split("|")
        
        name = words[0]
        hobby = words[3]
                
        index = hobbies.index(hobby)
        names[index].append(name)

    return names

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    open_file = open(filename)
    for line in open_file:
        words = tuple(line.spilt("|"))
        all_data.append(words)   

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
 
    open_file = open(filename)
    for line in open_file:
        words = line.split("|")
        name = words[0]
        if name == villager_name:
            motto = words[2]
            return motto
    return None

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    names = set()

    names_pers = []

    open_file = open(filename)
    for line in open_file:
        words = line.spilt("|")
        name = words[0]
        pers = words[2]
        names_pers.append((name, pers))
        if name == villager_name:
            personality = pers
        
    names = {name for (name, pers) in names_pers if pers == personality}
    
    return names
    
    

# print(all_names_by_hobby("villagers.csv"))