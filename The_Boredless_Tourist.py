destinations = ["Paris, France",
                "Shanghai, China",
                "Los Angeles, USA",
                "São Paulo, Brazil",
                "Cairo, Egypt"]

#test_traveler = ['name', 'destination', ['attraction tags']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

add_attraction("Los Angeles, USA", ['Venice Beach', ['Beach']])
add_attraction("Paris, France",["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interest = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interest)
    interests_string = "Hi " + traveler[0]
    interests_string += ", we think you'll like these places around "
    interests_string += traveler_destination + ': '
    for attraction in traveler_attractions:
        if attraction != traveler_attractions[-1]:
            interests_string += 'the ' + attraction + ', '
        else:
            interests_string += 'the ' + attraction + '.'
    print(interests_string)
    return

traveler = [input('Name: '), input('Destination: '), input('Attraction Tag List: ').split(' ')]

get_attractions_for_traveler(traveler)
