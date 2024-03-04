# has to have customtkinter master file inside of directore, regular install won't work?


# Import customtkinter module
import customtkinter as ctk
 
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("dark")        
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")    
 
# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("NMR")    
# Dimensions of the window will be 200x200
        self.geometry("500x350")    
 
 
if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop()    