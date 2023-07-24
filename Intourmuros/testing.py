from tkinter import * # import everying in tkinter
from tkinter import messagebox
import customtkinter as ctk
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
def tsp_nearest_neighbor(locations, selected_starting_point, selected_places):
    path = [selected_starting_point] # the path(list) will store the order in which the place will be visited 
    unvisited = set(selected_places)  # the unvisited(set) will keep track of the places that is not visited yet

    while unvisited:    # loop until all places have been visited
        current_location = path[-1] # retrieves the last element(current location) from path(list)
        nearest_location = None # store the nearest unvisited location to current location
        nearest_distance = float('inf') # store the distance to the nearest unvisited location

        for neighbor in unvisited:
            distance = calculate_distance(locations[current_location], locations[neighbor]) # calculate the distance between current location and current unvisited location
            if distance < nearest_distance: # check if calculated distance is smaller than current nearest distance
                nearest_location = neighbor # store the neighbor to nearest location
                nearest_distance = distance # store the distance to nearest distance

        path.append(nearest_location) # add nearest location to path(list)
        unvisited.remove(nearest_location) # nearest location to unvisited(set)

    path.append(selected_starting_point)# Add the starting point to the path(starting point also as end point)
    return path

def show_directions_on_google_maps(locations, path):
    base_url = "https://www.google.com/maps/dir/"
    for i in range(len(path) - 1):
        origin = locations[path[i]]
        destination = locations[path[i + 1]]
        url_params = f"{origin[0]},{origin[1]}/{destination[0]},{destination[1]}/"
        base_url += url_params

    webbrowser.open(base_url)



# ----- FUNCTION TO ACCESS THE LOCATION AND PRINT THE OUTPUT ----- #
def calculate_path():
    # add background
    file_bg_path = PhotoImage(file="path.png", master=My_Window)
    bg_path = Label(My_Window, image=file_bg_path, borderwidth=0)
    bg_path.place(x=0, y=0)

    selected_starting_point = list(locations.keys())[starting_point.get() - 1]# retrieves the selected starting point
    selected_places = [list(locations.keys())[index - 1] for index, value in enumerate(visit_places, start=1) if value.get() == 1]# retrieves the selected places 
    path = tsp_nearest_neighbor(locations, selected_starting_point, selected_places) # call the tsp function

    # show the path list
    y_offset = 210
    for index, place in enumerate(path, start=1):
        place_text = f"{index}. {place}"
        place_label = Label(My_Window, text=place_text, font=("Arial", 14), bg="#FFFAF3", foreground="#1C1C1C")
        place_label.place(x=30, y=y_offset)
        y_offset += 40
    
    show_maps_button = Button(My_Window, text="Show Google Maps", font=("Arial", 13, "bold"), bg="#202020",
                              activebackground="black", fg="white", activeforeground="#3699F2", width=16, height=2,
                              bd=0, borderwidth=0, relief=FLAT, command=lambda: show_directions_on_google_maps(locations, path))
    show_maps_button.place(x=140, y=770)



    My_Window.mainloop()


# ----- LOCATIONS AVAILABLE WITH ITS COORDINATES ----- #
locations = {
    'Pamantasan ng Lungsod ng Maynila':(14.5868, 120.9762),
    'Colegio de San Juan de Letran':(14.5938, 120.9769),
    'Manila Cathedral':(14.5917, 120.9734),
    'Mapua University':(14.5905, 120.9779),
    'Fort Santiago':(14.5942, 120.9704),
    'Lyceum of the Philippines University':(14.5916, 120.9778),
    'Baluarte de San Diego':(14.5854, 120.9756),
    'Casa Manila':(14.5894, 120.9753),
    'Museo de Intramuros':(14.5899, 120.9734),
    'Light and Sound Museum':(14.5882, 120.9741),
    'Bahay Tsinoy':(14.5908, 120.975),
    'San Agustin Church':(14.5892, 120.9752),
}

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
        ctk.CTkRadioButton(My_Window, text=location, font=("Arial", 18), bg_color="#FFFAF3", fg_color="#3699F2", radiobutton_height=16, radiobutton_width=16,
                             border_width_checked=4 ,variable=starting_point, value=i).place(x=30, y=170+i*42)
        

    # next button
    button_next= Button(My_Window, text="Next", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=15, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: check_startingplace())
    button_next.place(x=140, y=750)
    
    My_Window.mainloop()

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
            Checkbutton(My_Window, text=location, font=("Arial", 14), bg="#FFFAF3", activebackground="#FFFAF3", foreground="#1C1C1C", 
                        activeforeground="#1C1C1C", variable=var).place(x=30, y=165+i*42)
            visit_places.append(var)

        # show path button
        button_next= Button(My_Window, text="Show Path", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                                fg="white", activeforeground="#3699F2", width=16, height=2, bd=0, borderwidth=0, relief=FLAT,
                                command=lambda: calculate_path())
        button_next.place(x=140, y=750)

        My_Window.mainloop()
    
StartingPage()