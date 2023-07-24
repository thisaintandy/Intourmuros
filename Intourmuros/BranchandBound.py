from tkinter import *  # import everying in tkinter
from tkinter import messagebox
import customtkinter as ctk
import folium
import webbrowser


My_Window = Tk()
My_Window.geometry("423x867+750+80")
My_Window.resizable(width=False, height=False)
My_Window.title("Intourmuros")
My_Window.iconbitmap("icon.ico")


# ----- FUNCTION TO CALCULATE DISTANCE USING EUCLIDIAN ----- #
def calculate_distance(coordinates1, coordinates2):
    # assign the latitude and longitude of a place as coordinates
    latitude1, longitude1 = coordinates1
    latitude2, longitude2 = coordinates2

    # get the euclidian distance between 2 coordinates
    # distance(p,q) = squareroot [ (q1-p1)^2 + (q2-p2)^2 ]
    squared_sum = (latitude2 - latitude1) ** 2 + (longitude2 - longitude1) ** 2
    distance = squared_sum ** 0.5
    return distance


# ----- FUNCTION TO USE NEAREST NEIGHBOR ALGORITHM ----- #
def tsp_branch_and_bound(locations, selected_starting_point, selected_places):
    places = [selected_starting_point] + selected_places
    n = len(places)
    min_distance = float('inf')
    best_path = None

    def calculate_mst_distance(graph):
        # Calculate the Minimum Spanning Tree (MST) distance using Prim's algorithm.
        mst = []
        visited = {place: False for place in graph}
        visited[selected_starting_point] = True
        current_place = selected_starting_point

        for _ in range(n - 1):
            nearest_distance = float('inf')
            nearest_place = None
            for neighbor, weight in graph[current_place].items():
                if not visited[neighbor] and weight < nearest_distance:
                    nearest_distance = weight
                    nearest_place = neighbor

            if nearest_place is not None:
                mst.append(nearest_distance)
                visited[nearest_place] = True
                current_place = nearest_place

        return sum(mst)

    def branch_and_bound(path, unvisited, graph):
        nonlocal min_distance, best_path
        if not unvisited:
            # Add the selected starting point again to complete the path
            path.append(selected_starting_point)

            distance = 0
            for i in range(len(path) - 1):
                distance += calculate_distance(locations[path[i]], locations[path[i + 1]])

            if distance < min_distance:
                min_distance = distance
                best_path = path[:]
        else:
            lower_bound = calculate_mst_distance(graph)
            if lower_bound < min_distance:
                for i in range(len(unvisited)):
                    next_place = unvisited[i]
                    path.append(next_place)
                    cloned_unvisited = unvisited[:]
                    cloned_unvisited.remove(next_place)
                    branch_and_bound(path, cloned_unvisited, graph)
                    path.pop()

    graph = {place: {} for place in places}

    # Calculate distances between selected places to construct the graph
    for i in range(n):
        for j in range(i + 1, n):
            place1, place2 = places[i], places[j]
            distance = calculate_distance(locations[place1], locations[place2])
            graph[place1][place2] = distance
            graph[place2][place1] = distance

    branch_and_bound([selected_starting_point], selected_places, graph)

    return best_path


# ----- FUNCTION TO DISPLAY MARKERS OF THE PLACES WITH DISPLACEMENT ----- #
def display_map(path):
    # Create a map centered at the first location in the path
    map_obj = folium.Map(location=locations[path[0]], zoom_start=15)

    # Add markers for each location in the path
    for index, place in enumerate(path, start=1):
        folium.Marker(locations[place], popup=f"{index}. {place}").add_to(map_obj)

    # Add a line to connect the places in the path
    folium.PolyLine([locations[place] for place in path], color="blue", weight=2.5).add_to(map_obj)

    # Save the map to an HTML file
    map_obj.save("path_map.html")

    # Open the HTML file in a web browser to display the map
    import webbrowser
    webbrowser.open("path_map.html")


# ----- FUNCTION TO DISPLAY THE DIRECTIONS IN THE GOOGLE MAPS ----- #

def show_directions_on_google_maps(locations, path):
    base_url = "https://www.google.com/maps/dir/"

    # Add the first location to the URL
    origin = locations[path[0]]
    url_params = f"{origin[0]},{origin[1]}/"
    base_url += url_params

    for i in range(len(path) - 1):
        origin = locations[path[i]]
        destination = locations[path[i + 1]]
        url_params = f"{destination[0]},{destination[1]}/"
        base_url += url_params

    webbrowser.open(base_url)


# ----- FUNCTION TO ACCESS THE LOCATION AND PRINT THE OUTPUT ----- #
def calculate_path():
    # ... (other parts of the function remain the same)

    selected_starting_point = list(locations.keys())[starting_point.get() - 1]  # retrieves the selected starting point
    selected_places = [list(locations.keys())[index - 1] for index, value in enumerate(visit_places, start=1) if
                       value.get() == 1]  # retrieves the selected places
    path = tsp_branch_and_bound(locations, selected_starting_point, selected_places)  # call the tsp function

    if path is None:
        # Display an error message if no valid path is found
        messagebox.showerror("Error", "No valid path found to visit all selected places.")
        return

    # show the path list
    y_offset = 210
    for index, place in enumerate(path, start=1):
        place_text = f"{index}. {place}"
        place_label = Label(My_Window, text=place_text, font=("Arial", 14), bg="#FFFAF3", foreground="#1C1C1C")
        place_label.place(x=30, y=y_offset)
        y_offset += 40

    show_map_button = Button(My_Window, text="Show Map", font=('Arial', 10, 'bold'), bg="#202020",
                             activebackground="black",
                             fg="white", activeforeground="#3699F2", width=37, height=2, bd=0, borderwidth=0,
                             relief=FLAT,
                             command=lambda: display_map(path))
    show_map_button.place(x=60, y=750)

    show_maps_button = Button(My_Window, text="Show Directions using Google Maps", font=("Arial", 10, "bold"),
                              bg="#202020",
                              activebackground="black", fg="white", activeforeground="#3699F2", width=37, height=2,
                              bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: show_directions_on_google_maps(locations, path))
    show_maps_button.place(x=60, y=795)

    My_Window.mainloop()


# ----- LOCATIONS AVAILABLE WITH ITS COORDINATES ----- #
locations = {
    'Pamantasan ng Lungsod ng Maynila': (14.5868, 120.9762),
    'Colegio de San Juan de Letran': (14.5938, 120.9769),
    'Manila Cathedral': (14.5917, 120.9734),
    'Mapua University': (14.5905, 120.9779),
    'Fort Santiago': (14.5942, 120.9704),
    'Lyceum of the Philippines University': (14.5916, 120.9778),
    'Baluarte de San Diego': (14.5854, 120.9756),
    'Casa Manila': (14.5894, 120.9753),
    'Museo de Intramuros': (14.5899, 120.9734),
    'Light and Sound Museum': (14.5882, 120.9741),
    'Bahay Tsinoy': (14.5908, 120.975),
    'San Agustin Church': (14.5892, 120.9752),
}

# storage of inputs
starting_point = IntVar()
visit_places = []


# ----- PAGE TO GET THE STARTING POINT/PLACE ----- #
def StartingPage():
    # add background
    file_bg_starting = PhotoImage(file="starting.png", master=My_Window)
    bg_starting = Label(My_Window, image=file_bg_starting, borderwidth=0)
    bg_starting.place(x=0, y=0)

    # add radiobuttons for select starting place
    for i, location in enumerate(locations, start=1):
        ctk.CTkRadioButton(My_Window, text=location, font=("Arial", 18), bg_color="#FFFAF3", fg_color="#3699F2",
                           radiobutton_height=16, radiobutton_width=16,
                           border_width_checked=4, variable=starting_point, value=i).place(x=30, y=170 + i * 42)

    # next button
    button_next = Button(My_Window, text="Next", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                         fg="white", activeforeground="#3699F2", width=15, height=2, bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: check_startingplace())
    button_next.place(x=140, y=750)

    My_Window.mainloop()


# ----- ERROR WILL POP UP IF NO INPUT FOR STARTING ----- #
def check_startingplace():
    if starting_point.get() == 0:
        messagebox.showerror("Error", "Please select a starting place.")
    else:
        VisitingPage()


# ----- PAGE TO GET THE VISITING PLACES ----- #
def VisitingPage():
    # add background
    file_bg_visiting = PhotoImage(file="visiting.png", master=My_Window)
    bg_visiting = Label(My_Window, image=file_bg_visiting, borderwidth=0)
    bg_visiting.place(x=0, y=0)

    # add checkboxes for the places that will be visited
    for i, location in enumerate(locations, start=1):
        var = IntVar()
        Checkbutton(My_Window, text=location, font=("Arial", 14), bg="#FFFAF3", activebackground="#FFFAF3",
                    foreground="#1C1C1C",
                    activeforeground="#1C1C1C", variable=var).place(x=30, y=165 + i * 42)
        visit_places.append(var)

    # show path button
    button_next = Button(My_Window, text="Show Path", font=('Arial', 13, 'bold'), bg="#202020",
                         activebackground="black",
                         fg="white", activeforeground="#3699F2", width=16, height=2, bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: calculate_path())
    button_next.place(x=140, y=750)

    My_Window.mainloop()


StartingPage()