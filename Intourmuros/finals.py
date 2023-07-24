from tkinter import * # import everying in tkinter
from tkinter import messagebox
import customtkinter as ctk
import folium
import webbrowser

My_Window = Tk()
My_Window.geometry("700x867+750+80") #1920x1080
My_Window.resizable(width=False, height=False)
My_Window.title("Intourmuros")
My_Window.iconbitmap("icon.ico")

# Home Page
def Home():

    # add background
    file_bg_page1 = PhotoImage(file="home.png", master=My_Window)
    bg_page1 = Label(My_Window, image=file_bg_page1, borderwidth=0)
    bg_page1.place(x=0, y=0)

    # get started button 
    button_getstarted= Button(My_Window, text="GET STARTED", font=('Arial', 15, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#E8B63F", width=17, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: Desti1())
    button_getstarted.place(x=110, y=610)

    # information/about button
    button_info = Button(My_Window, text="i", font=('Courier New', 12, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="white", width=2, height=1, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: About())
    button_info.place(x=30, y=810)


    My_Window.mainloop()

# Information/About Page
def About():

    # add background
    file_bg_page2 = PhotoImage(file="bgabout.png", master=My_Window)
    bg_page2 = Label(My_Window, image=file_bg_page2, borderwidth=0)
    bg_page2.place(x=0, y=0)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#EAEAEA", activebackground="#EAEAEA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    My_Window.mainloop()

# Destination Pages
def Desti1():
 
    # add background
    file_bg_desti = PhotoImage(file="desti1.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti2())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti12())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti1info())
    button_placeinfo.place(x=190, y= 595)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    My_Window.mainloop()

def desti1info():
    # add background
    file_bg_desti = PhotoImage(file="desti1info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti1())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti2():
 
    # add background
    file_bg_desti = PhotoImage(file="desti2.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti3())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti1())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti2info())
    button_placeinfo.place(x=190, y= 565)

    My_Window.mainloop()

def desti2info():
    # add background
    file_bg_desti = PhotoImage(file="desti2info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti2())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti3():
 
    # add background
    file_bg_desti = PhotoImage(file="desti3.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti4())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti2())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti3info())
    button_placeinfo.place(x=190, y= 595)

    My_Window.mainloop()

def desti3info():
    # add background
    file_bg_desti = PhotoImage(file="desti3info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti3())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti4():
 
    # add background
    file_bg_desti = PhotoImage(file="desti4.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti5())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti3())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti4info())
    button_placeinfo.place(x=190, y= 595)

    My_Window.mainloop()

def desti4info():
    # add background
    file_bg_desti = PhotoImage(file="desti4info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti4())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti5():
 
    # add background
    file_bg_desti = PhotoImage(file="desti5.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti6())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti4())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    
    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti5info())
    button_placeinfo.place(x=190, y= 565)

    button_back.place(x=25, y=32)

    My_Window.mainloop()

def desti5info():
    # add background
    file_bg_desti = PhotoImage(file="desti5info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti5())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti6():
 
    # add background
    file_bg_desti = PhotoImage(file="desti6.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti7())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti5())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti6info())
    button_placeinfo.place(x=190, y= 565)

    My_Window.mainloop()

def desti6info():
    # add background
    file_bg_desti = PhotoImage(file="desti6info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti6())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti7():
 
    # add background
    file_bg_desti = PhotoImage(file="desti7.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti8())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti6())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti7info())
    button_placeinfo.place(x=190, y= 565)



    My_Window.mainloop()

def desti7info():
    # add background
    file_bg_desti = PhotoImage(file="desti7info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti7())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti8():
 
    # add background
    file_bg_desti = PhotoImage(file="desti8.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti9())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti7())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti8info())
    button_placeinfo.place(x=190, y= 565)

    My_Window.mainloop()

def desti8info():
    # add background
    file_bg_desti = PhotoImage(file="desti8info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti8())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti9():
 
    # add background
    file_bg_desti = PhotoImage(file="desti9.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti10())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti8())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti9info())
    button_placeinfo.place(x=190, y= 565)

    My_Window.mainloop()

def desti9info():
    # add background
    file_bg_desti = PhotoImage(file="desti9info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti9())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti10():
 
    # add background
    file_bg_desti = PhotoImage(file="desti10.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti11())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti9())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti10info())
    button_placeinfo.place(x=190, y= 595)

    My_Window.mainloop()

def desti10info():
    # add background
    file_bg_desti = PhotoImage(file="desti10info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti10())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti11():
 
    # add background
    file_bg_desti = PhotoImage(file="desti11.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti12())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti10())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti11info())
    button_placeinfo.place(x=190, y= 565)

    My_Window.mainloop()

def desti11info():
    # add background
    file_bg_desti = PhotoImage(file="desti11info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti11())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

def Desti12():
 
    # add background
    file_bg_desti = PhotoImage(file="desti12.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # add arrows to navigate between different destinations
    file_arrowright = PhotoImage(file="arrowright.png", master=My_Window)
    button_arrowright = Button(My_Window, image=file_arrowright, bg="#F8F8F8", activebackground="#F8F8F8", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti1())
    button_arrowright.place(x=380, y=400)

    file_arrowleft = PhotoImage(file="arrowleft.png", master=My_Window)
    button_arrowleft = Button(My_Window, image=file_arrowleft, bg="#F9F9F9", activebackground="#F9F9F9", width=25, height=35, bd=0, borderwidth=0,
                               command=lambda: Desti11())
    button_arrowleft.place(x=15, y=400)

    # explore button 
    button_explore= Button(My_Window, text="Explore", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                            fg="white", activeforeground="#3699F2", width=14, height=2, bd=0, borderwidth=0, relief=FLAT,
                            command=lambda: StartingPage())
    button_explore.place(x=140, y=660)

    # back button to page one
    file_backbutton = PhotoImage(file="backbutton.png", master=My_Window)
    button_back = Button(My_Window, image=file_backbutton, width=55, height=35, background="#DADADA", activebackground="#DADADA", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Home())
    button_back.place(x=25, y=32)

    # place info button
    button_placeinfo = Button(My_Window, text="show info", font=('Arial', 7, 'underline'), bg="#F8F8F8", activebackground="#F8F8F8",
                              fg="black", activeforeground="blue", width=7, height=1, bd=0, borderwidth=0, relief=FLAT,
                              command=lambda: desti12info())
    button_placeinfo.place(x=190, y= 565)

    My_Window.mainloop()

def desti12info():
    # add background
    file_bg_desti = PhotoImage(file="desti12info.png", master=My_Window)
    bg_desti = Label(My_Window, image=file_bg_desti, borderwidth=0)
    bg_desti.place(x=0, y=0)

    # close button
    file_closebutton = PhotoImage(file="close.png", master=My_Window)
    button_close = Button(My_Window, image=file_closebutton, width=35, height=35, background="#D5D5D5", activebackground="#D5D5D5", bd=0, borderwidth=0, relief=FLAT,
                         command=lambda: Desti12())
    button_close.place(x=365, y=390)

    My_Window.mainloop()

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

    show_map_button = Button(My_Window, text="Show Map", font=('Arial', 10, 'bold'), bg="#202020", activebackground="black",
                             fg="white", activeforeground="#3699F2", width=37, height=2, bd=0, borderwidth=0, relief=FLAT,
                             command=lambda: display_map(path))
    show_map_button.place(x=60, y=750)

    show_maps_button = Button(My_Window, text="Show Directions using Google Maps", font=("Arial", 10, "bold"), bg="#202020",
                              activebackground="black", fg="white", activeforeground="#3699F2", width=37, height=2,
                              bd=0, borderwidth=0, relief=FLAT, command=lambda: show_directions_on_google_maps(locations, path))
    show_maps_button.place(x=60, y=795)

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
        ctk.CTkRadioButton(My_Window, text=location, font=("Arial", 18), bg_color="#FFFAF3", fg_color="#3699F2", radiobutton_height=16, radiobutton_width=16,
                             border_width_checked=4 ,variable=starting_point, value=i).place(x=30, y=170+i*42)

    # next button
    button_next= Button(My_Window, text="Next", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
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
            Checkbutton(My_Window, text=location, font=("Arial", 14), bg="#FFFAF3", activebackground="#FFFAF3", foreground="#1C1C1C", 
                        activeforeground="#1C1C1C", variable=var).place(x=30, y=165+i*42)
            visit_places.append(var)

        # show path button
        button_next= Button(My_Window, text="Show Path", font=('Arial', 13, 'bold'), bg="#202020", activebackground="black",
                                fg="white", activeforeground="#3699F2", width=16, height=2, bd=0, borderwidth=0, relief=FLAT,
                                command=lambda: calculate_path())
        button_next.place(x=140, y=750)

        My_Window.mainloop()

    
Home()