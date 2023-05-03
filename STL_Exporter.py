import os  
from tkinter import *
from tkinter.ttk import *

master = Tk()
master.title("Mesh_STL")
master.configure(bg="#3e3e42")  

stl_name = "Mesh"
path= stl_name + ".stl" 


triangle_image = PhotoImage(file="images/Triangle.png")
triangle_resized = triangle_image.subsample(4, 4)

square_image = PhotoImage(file="images/square.png")
square_resized = square_image.subsample(4, 4)

cube_image = PhotoImage(file="images/cube.png")
cube_resized = cube_image.subsample(4, 4)

pyramid_image = PhotoImage(file="images/pyramid.png")
pyramid_resized = pyramid_image.subsample(4, 4)


# Save File
'''if os.path.isfile(path):  
    print("\n File exist")  
    f = open(stl_name + ".stl", "r")
else:  
    print("File does not exist")
    f = open(stl_name + ".stl", "w")'''

Points=[]
Mesh_ID =[0]
Error_Alert = [0]

def Export_Mesh():
    
    global Points
    print(Mesh_ID)
    match Mesh_ID[0]:
        case 1:
            Triangle_Mesh()
        case 2:
            Square_Mesh()
        case 3:
            Pyramid_Mesh()
        case 4:
            Cube_Mesh()
    
    if Error_Alert[0] ==1:
        Log_Label.configure(text="LOG : " + "WARNING! INSERT ONLY NUMERIC VALUE!!!", foreground='#f00')
        return

    if Points == []:
        print("No Mesh selected")
        print(Points)
        return
    
    stl_name = export_name.get()
    lines = [0]
    normal = [0,0,0]
    lines[0] = "solid Exported from Python 3.11 \n"
    
    for el in range(len(Points)):
        normal[0] = Points[el][0][1]*Points[el][1][2] - Points[el][0][2]*Points[el][1][1]
        normal[1] = Points[el][0][0]*Points[el][1][2] - Points[el][0][2]*Points[el][1][1]
        normal[2] = Points[el][0][0]*Points[el][1][2] - Points[el][0][1]*Points[el][1][0]

        print(normal)
        lines.append("facet normal" +str(normal[0]) + " " + str(normal[1]) + " " + str(normal[2]) + "\n")
        lines.append("outer loop \n")
        lines.append("vertex " + str(Points[el][0][0]) + " " + str(Points[el][0][1]) + " " + str(Points[el][0][2]) + "\n")
        lines.append("vertex " + str(Points[el][1][0]) + " " + str(Points[el][1][1]) + " " + str(Points[el][1][2]) + "\n")
        lines.append("vertex " + str(Points[el][2][0]) + " " + str(Points[el][2][1]) + " " + str(Points[el][2][2]) + "\n")
        lines.append("endloop \n")
        lines.append("endfacet \n")
    lines.append("endsolid Exported from Python 3.11 \n")

    '''lines=f.readlines()
    print(lines)
    f.close()'''

    f = open(stl_name + ".stl", "w")
    f.writelines(lines)
    f.close()
    #print(lines)
    #print(lines[0])
    #print(len(lines))
    print("lines are" + str(lines))
    Log_Label.configure(text="LOG : " + "STL File was properly created", foreground='green')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def Mesh_Selected(mesh_type):
    global Dimension_1
    global Dimension_2
    global Dimension_3
    Dimension_1.delete(0,END)
    Dimension_2.delete(0,END)
    Dimension_3.delete(0,END)
    Dimension_1.config(state=DISABLED)
    Dimension_2.config(state=DISABLED)
    Dimension_3.config(state=DISABLED)
    if mesh_type == 1:
        Dimension_1.config(state=NORMAL)
        Dimension_1.insert(0,"1")
        export_name.delete(0,END)
        export_name.insert(0,"Triangle")
        Dimension_name.config(text="Triangle - Insert length of the edge")
        Mesh_ID[0] = mesh_type
    elif mesh_type == 2: 
        Dimension_1.config(state=NORMAL)
        Dimension_2.config(state=NORMAL)
        Dimension_1.insert(0,"1")
        Dimension_2.insert(0,"1")
        export_name.delete(0,END)
        export_name.insert(0,"Square")
        Dimension_name.config(text="Square - Insert length of the edge")
        Mesh_ID[0] = mesh_type
    elif mesh_type == 3:
        Dimension_1.config(state=NORMAL)
        Dimension_2.config(state=NORMAL)
        Dimension_3.config(state=NORMAL)
        Dimension_1.insert(0,"1")
        Dimension_2.insert(0,"1")
        Dimension_3.insert(0,"1")
        export_name.delete(0,END)
        export_name.insert(0,"Pyramid")
        Dimension_name.config(text="Pyramid - Insert lenght, width and height") 
        Mesh_ID[0] = mesh_type 
    elif mesh_type == 4:
        Dimension_1.config(state=NORMAL)
        Dimension_2.config(state=NORMAL)
        Dimension_3.config(state=NORMAL)
        Dimension_1.insert(0,"1")
        Dimension_2.insert(0,"1")
        Dimension_3.insert(0,"1")
        export_name.delete(0,END)
        export_name.insert(0,"Cube") 
        Dimension_name.config(text="Cube - Insert lenght, width and height") 
        Mesh_ID[0] = mesh_type


#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def Triangle_Mesh():
    global Points
    try:
        Triangle_l = float(Dimension_1.get()) 
        Error_Alert[0] = 0
    except:
        print("An exception occurred")
        Error_Alert[0] = 1
        return
    print(Triangle_l)
    Points = [[(-Triangle_l,Triangle_l,0.0),(-Triangle_l,0.0,0.0),(0,0.0,0.0)]]
    
def Square_Mesh():
    global Points
    try:
        Square_l = float(Dimension_1.get()) 
        Square_w = float(Dimension_2.get()) 
        Error_Alert[0] = 0
    except:
        print("An exception occurred")
        Error_Alert[0] = 1
        return
    Points = [[(-Square_l,Square_w,0.0),(-Square_l,0.0,0.0),(0,0.0,0.0)],[(0.0,Square_w,0.0),(-Square_l,Square_w,0.0),(0.0,0.0,0.0)]]

def Pyramid_Mesh():
    global Points
    try:
        Pyr_b = float(Dimension_1.get()) * 0.5
        Pyr_w = float(Dimension_2.get()) * 0.5
        Pyr_h = float(Dimension_3.get()) 
        Error_Alert[0] = 0
    except:
        print("An exception occurred")
        Error_Alert[0] = 1
        return
    Pyr_A = (-Pyr_b,Pyr_w,0.0)
    Pyr_B = (-Pyr_b,-Pyr_w,0.0)
    Pyr_C = (Pyr_b,-Pyr_w,0.0)
    Pyr_D = (Pyr_b,Pyr_w,0.0)
    Pyr_E = (0.0,0.0,Pyr_h)
    Points = [[(Pyr_A),(Pyr_E),(Pyr_B)],[(Pyr_B),(Pyr_E),(Pyr_C)],[(Pyr_C),(Pyr_E),(Pyr_D)],
              [(Pyr_A),(Pyr_D),(Pyr_E)],[(Pyr_A),(Pyr_B),(Pyr_C)],[(Pyr_A),(Pyr_D),(Pyr_C)]]

def Cube_Mesh():
    global Points
    try:
        Cube_l = float(Dimension_1.get()) * 0.5
        Cube_w = float(Dimension_2.get()) * 0.5
        Cube_h = float(Dimension_3.get()) 
        Error_Alert[0] = 0
    except:
        print("An exception occurred")
        Error_Alert[0] = 1
        return   
    Cube_A = (-Cube_l,Cube_w,0)
    Cube_B = (-Cube_l,-Cube_w,0)
    Cube_C = (Cube_l,-Cube_w,0)
    Cube_D = (Cube_l,Cube_w,0)
    Cube_E = (-Cube_l,Cube_w,Cube_h)
    Cube_F = (-Cube_l,-Cube_w,Cube_h)
    Cube_G = (Cube_l,-Cube_w,Cube_h)
    Cube_H = (Cube_l,Cube_w,Cube_h)
    Points = [[(Cube_A),(Cube_B),(Cube_C)],[(Cube_A),(Cube_C),(Cube_D)],[(Cube_B),(Cube_C),(Cube_G)],[(Cube_B),(Cube_G),(Cube_F)],
              [(Cube_G),(Cube_C),(Cube_D)],[(Cube_D),(Cube_H),(Cube_G)],[(Cube_H),(Cube_D),(Cube_A)],[(Cube_A),(Cube_H),(Cube_E)],
              [(Cube_E),(Cube_A),(Cube_F)],[(Cube_F),(Cube_A),(Cube_B)],[(Cube_E),(Cube_H),(Cube_G)],[(Cube_E),(Cube_G),(Cube_F)]]
     

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

triangle_btn = Button(text="Create Triangle", image = triangle_resized, compound = LEFT, command=lambda :Mesh_Selected(1))

triangle_btn.grid(row=0, column = 0, sticky=W+E+N+S, padx= 10, pady = 10 )

square_btn = Button(text="Create Square", image = square_resized,compound = LEFT,command=lambda :Mesh_Selected(2))

square_btn.grid(row=0, column = 1,sticky=W+E+N+S, padx= 10, pady= 10 )

triangle_btn = Button(text="Create Pyramid", image = pyramid_resized,compound = LEFT, command=lambda :Mesh_Selected(3))

triangle_btn.grid(row=0, column = 2, sticky=W+E+N+S,padx= 10, pady= 10 )

triangle_btn = Button(text="Create Cube", image = cube_resized,compound = LEFT, command=lambda :Mesh_Selected(4))

triangle_btn.grid(row=0, column = 3, sticky=W+E+N+S,padx= 10, pady= 10 )

triangle_btn = Button(text="Export", command=lambda :Export_Mesh())

triangle_btn.grid(row=4, column = 3, sticky=W+E, padx=10, pady=1)

Dimension_name = Label(text="Select a figure")

Dimension_name.grid(row=2, column = 0, sticky=W+E)

Dimension_1 = Entry(state=DISABLED)

Dimension_1.grid(row=2, column = 1, sticky=W+E, padx= 10)

Dimension_2 = Entry(state=DISABLED)
Dimension_3 = Entry(state=DISABLED)
STL_name = Label(text="Insert Name of the file")
export_name = Entry(text = "Insert Text")
Log_Label = Label(text="LOG :")




Dimension_2.grid(row=2, column = 2, sticky=W+E, padx= 10)
Dimension_3.grid(row=2, column = 3,sticky=W+E, padx= 10)
STL_name.grid(row=4, column = 0, sticky=W+E)
export_name.grid(row=4, column = 1, columnspan=2, sticky=W+E, padx=10)
Log_Label.grid(row=5, column = 0, columnspan=4, sticky=W+E,pady=10)

export_name.insert(0,"")
print(export_name.get())
stl_name = export_name.get()

mainloop()


