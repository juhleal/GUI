import tkinter as tk

# Create a GUI window
window = tk.Tk()
window.title("GUI Example")

# Add widgets
label = tk.Label(window, text="Hello, Recruiters!")
label.pack()

button = tk.Button(window, text="Click Me", command=lambda: print("Button clicked!"))
button.pack()

# Run the GUI event loop
window.mainloop()
