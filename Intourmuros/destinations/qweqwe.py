import math
from tkinter import Tk, Label, Button, Checkbutton, IntVar, Radiobutton, StringVar

def calculate_distance(coordinates1, coordinates2):
    latitude1, longitude1 = coordinates1
    latitude2, longitude2 = coordinates2
    distance = math.sqrt((latitude2 - latitude1) ** 2 + (longitude2 - longitude1) ** 2)
    return distance

def tsp_nearest_neighbor(locations, selected_starting_point, selected_places):
    path = [selected_starting_point]
    unvisited = set(selected_places)

    while unvisited:
        current_location = path[-1]
        nearest_location = None
        nearest_distance = float('inf')

        for neighbor in unvisited:
            distance = calculate_distance(locations[current_location], locations[neighbor])
            if distance < nearest_distance:
                nearest_location = neighbor
                nearest_distance = distance

        path.append(nearest_location)
        unvisited.remove(nearest_location)

    path.append(selected_starting_point)
    return path

def calculate_path():
    selected_starting_point = list(locations.keys())[starting_point_var.get() - 1]
    selected_places = [list(locations.keys())[index - 1] for index, value in enumerate(visit_places_vars, start=1) if value.get() == 1]
    path = tsp_nearest_neighbor(locations, selected_starting_point, selected_places)

    print("\nThe optimal path for visiting the selected places:")
    for place in path:
        print(place)

# Locations dictionary (unchanged)
locations = {
    'Lyceum of the Philippines University':(14.5916, 120.9778),
    'Mapua University':(14.5905, 120.9779),
    'Pamantasan ng Lungsod ng Maynila':(14.5868, 120.9762),
    'Colegio de San Juan de Letran':(14.5938, 120.9769),
    'Manila Cathedral':(14.5917, 120.9734),
    'Fort Santiago':(14.5942, 120.9704),
    'Baluarte de San Diego':(14.5854, 120.9756),
    'Casa Manila':(14.5894, 120.9753),
    'Museo de Intramuros':(14.5899, 120.9734),
    'Light and Sound Museum':(14.5882, 120.9741),
    'Bahay Tsinoy':(14.5908, 120.975),
    'San Agustin Church':(14.5892, 120.9752),
}

# Create GUI window
window = Tk()
window.title("Intramuros Tour Planner")

# Starting point selection
Label(window, text="Select a starting point:").pack()

starting_point_var = IntVar()
for i, location in enumerate(locations, start=1):
    Radiobutton(window, text=location, variable=starting_point_var, value=i).pack()

# Visiting places selection
Label(window, text="Select the places you want to visit:").pack()

visit_places_vars = []
for i, location in enumerate(locations, start=1):
    var = IntVar()
    Checkbutton(window, text=location, variable=var).pack()
    visit_places_vars.append(var)

# Calculate path button
Button(window, text="Calculate Path", command=calculate_path).pack()
print(starting_point_var)

window.mainloop()
