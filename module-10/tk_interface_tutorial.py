import tkinter as tk
import tkinter.messagebox as msg

#Tutorial walk through of Python Tkinter by Example walkthrough by David Love
#https://github.com/Dvlv/Tkinter-By-Example/blob/master/Tkinter-By-Example.pdf

#Create a class for the GUI
class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        #Create a menu bar
        self.menu = tk.Menu(self, bg="white", fg="black")
        
        #Add a file menu on the menu bar
        self.file_menu = tk.Menu(self.menu, tearoff=0, bg="white", fg="black")
        
        #Add an exit option to the file menu/make it close app when clicked
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.config(menu=self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        #Initialize a listbox to display the tasks
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        #Widget to hold tasks
        self.tasks_canvas = tk.Canvas(self)

        #Frame to hold tasks
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        #Crate a scrollbar to scroll through tasks
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        #define window size add title
        self.title("Schriner To-Do")
        self.geometry("300x400")

        #Text widget to enter tasks
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        #Use Pack() method to for canvas and scrollbar
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Create window to hold tasks frame
        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        #Use Pack() method to for text input place at the bottom of window
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        #Add default task
        todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here ---", bg="cyan", fg="black", pady=10)

        #Bind the right mouse click to the delete task function
        todo1.bind("<Button-3>", self.remove_task)

        #Add the default task to the listbox
        self.tasks.append(todo1)

        #Create loop for binding various events
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        #Bind the enter key to the add task function
        self.bind("<Return>", self.add_task)
        #Reconfigure the canvas when the window is resized
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll) #Mouse wheel scroll
        self.bind_all("<Button-4>", self.mouse_scroll) 
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        #Create color schemes for the GUI
        self.colour_schemes = [{"bg": "cyan", "fg": "black"}, {"bg": "orange", "fg": "black"}]

    def add_task(self, event=None):
        #Get the text from the text widget
        task_text = self.task_create.get(1.0,tk.END).strip()

        #If the task is not empty, add it to the listbox
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            #Create the alternating colours for the tasks
            self.set_task_colour(len(self.tasks), new_task)

            #Bind the right mouse click to the delete task function
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            #Add the task to the list
            self.tasks.append(new_task)

        #Clear the input after adding a task
        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        #Get the task that was clicked
        task = event.widget
        #Ask the user if they want to delete the task
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            #Delete the task from the list
            self.tasks.remove(event.widget)
            event.widget.destroy()
            #Recolor the remaing tasks to keep alternating colours
            self.recolour_tasks()
    
    #Recolors the tasks
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    #Creates the altenrating color pattern for the tasks
    def set_task_colour(self, position, task):
        #Altenrate the colours based on position
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        #Set the background and foreground colours
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    #Update scollbar when window is resized
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    #Adjust canvas width when resized
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    #Define mouse wheel scroll
    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")
   
#Main program execution
if __name__ == "__main__":
 todo = Todo()
 todo.mainloop()