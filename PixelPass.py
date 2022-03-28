import tkinter as tk
from tkinter import ttk
import Collection
import GenPass


class PixelPass():
    def __init__(self):

        #! Main window
<<<<<<< HEAD
=======

>>>>>>> 6e167558b75f74c67eab90e19cc69efbb250a133
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.resizable(width=False, height=False)
        self.root.title("Pixel.Pass")
        self.root.configure(bg="light grey")

        ################################################

        #! Password image label

        self.passImgPath = tk.StringVar()
        self.passImgLabel = tk.ttk.Label(
            self.root, textvariable=self.passImgPath, font=("Arial", 10, "bold"), foreground="black", background="light grey", wraplength=780)
        self.passImgPath.set("Select password image source")

        ##########################################################################

        #! Password image button

        self.passImgBtn = tk.Button(self.root, text="Password Image", font=("Arial", 12, "bold"), command=(
            lambda: [Collection.getContext(), self.changePassPath(), self.changeMax(), self.changePass(GenPass.desiredLength, self.onOrOff.get())]))

        #############################################################################################################

        #! Desired length label

        self.desiredLengthLabel = tk.ttk.Label(
            self.root, text="Enter password length:", font=("Arial", 16, "bold"), foreground="black", background="light grey")

        ################################################################################

        #! Maximum password length label

        self.maxLengthText = tk.StringVar()
        self.maxLengthLabel = tk.ttk.Label(
            self.root, textvariable=self.maxLengthText, font=("Arial", 10, "bold"), foreground="black", background="light grey")
        self.maxLengthText.set("(Maximum password length: 0)")

        ##############################################################################

        #! Desired password length entry

        self.desLengthEntry = tk.ttk.Entry(
            self.root, width=6, font=("Arial", 16, "bold"), justify="center")
        self.desLengthEntry.bind('<KeyRelease>', self.lengthBind)

        #######################################################################

        #! Outputted password label

        self.passLabel = tk.ttk.Label(self.root, font=(
            "Arial", 20, "bold"), justify="center", text="Password:", foreground="black", background="light grey")

        ##############################################################################################

        #! Outputted password entry

        self.passText = tk.Text(self.root, height=2, font=("Arial", 10, "bold"))
        self.passText.configure(
            inactiveselectbackground=self.passText.cget("selectbackground"))
        self.passText.bind("<Button-1>", self.copyPass)

        ###############################################################################################

        #! Special characters label

        self.specCharsLabel = tk.ttk.Label(
            self.root, text="Special characters:", font=("Arial", 16, "bold"), foreground="black", background="light grey")

        #! Special characters option

        self.onOrOff = tk.BooleanVar()
        self.specialCharacters = tk.Checkbutton(self.root, variable=self.onOrOff, command=self.specChars)

        ##########################################################################################

        #! Copied to clipboard label

        self.clipMessage = tk.ttk.Label(
            self.root, text="(Click to copy)", font=("Arial", 10, "bold"), foreground="black", background="light grey")

        #! Pack widgets

        self.passImgBtn.pack(pady=(40, 30), ipady=10, ipadx=10)
        self.desiredLengthLabel.pack()
        self.maxLengthLabel.pack()
        self.desLengthEntry.pack(pady=(10,0))
        self.specCharsLabel.pack(pady=(30, 0))
        self.specialCharacters.pack(pady=(3, 0))
        self.passLabel.pack(pady=(40, 0))
        self.clipMessage.pack()
        self.passText.pack()
        self.passImgLabel.pack(pady=(30,0))

        ################################

        #! Main loop

        self.root.mainloop()

        ########################

    # Updates the outputted password with the password gen function output
    def changePass(self, length, specialChars):
        if self.passText:
            self.passText.delete(1.0, tk.END)
            try:
                self.passText.insert(1.0, GenPass.genPass(
                    Collection.passMaxLength, length, self.onOrOff.get()), tk.END)
            except tk.TclError:
                return False
        else:
            self.passText.insert(1.0, GenPass.genPass(
                Collection.passMaxLength, length, self.onOrOff.get()), tk.END)

    # Updates the password image file path label
    def changePassPath(self):
        self.passImgPath.set(Collection.passImgPath)

    def changeMax(self):
        self.maxLengthText.set(
            "(Maximum password length: " + str(Collection.passMaxLength) + ")")

    def lengthBind(self, event):
        newLength = self.desLengthEntry.get()
        try:
            GenPass.desiredLength = int(newLength)
            return self.changePass(GenPass.desiredLength, self.onOrOff.get())
        except ValueError:
            return False

    def specChars(self):
        self.passText.delete(1.0, tk.END)
        try:
            self.passText.insert(1.0, GenPass.genPass(
                Collection.passMaxLength, self.desLengthEntry.get(), self.onOrOff.get()), tk.END)
        except tk.TclError:
            return False
    
    def copyPass(self, event):
        self.root.clipboard_clear()
        self.root.clipboard_append(GenPass.gendPass)
        self.root.update()

app = PixelPass()
