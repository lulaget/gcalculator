# Python program for simple calculator
import tkinter as tk
from tkinter import messagebox

#give a class for the calculator
class Calculator:
   #give the initialization of the application
   def __init__(self, root):
      self.root=root
      self.root.title("Calculator")
      self.root.geometry("600x700")
      self.root.resizable(0,0)
      #Give the string variable to hold the current input
      self.input_text = tk.StringVar
      # create a text entry widget to display the input
      input_frame=tk.Frame(self.root, width = 375, height = 50, bd = 0)
      input_frame.pack(side=tk.TOP)
      #Entry Field
      input_field=tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify = tk.RIGHT)
      input_field.grid(row=0, column=0)
      input_field.pack(ipady=10)# This is the internal padding to increase the height of the inputfield
      #create the buttons
      butttons_frame=tk.Frame(self.root, width= 375, height= 450, bg= 'grey')
      butttons_frame.pack()
      #define the buttons and the text layout
      buttons=[
         ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
         ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
         ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
         ('c',4,0), ('0',4,1), ('=',4,2), ('+',4,3)
      ]
      #create buttons in the frame
      for(text,row,col) in buttons:
         self.create_button(text, row, col, butttons_frame)

          
   def create_button(self, text, row, col, frame):
      button = tk.Button(frame, text=text, font=('arial', 18, 'bold'), textvariable = self.input_text, fg='black', width=9, height=3, bd = 0, bg = '#fff', cursor = "hand2", command = lambda:self.on_button_click(text))
      button.grid(row=row, column=col, padx=1, pady=1)
def on_button_click(self, text):
      if text == "=":
          try:
              # evaluate the expression in the ainput field
              result = str(eval(self.input_text.get()))
              self.input_text.set(result)
          except Exception as e:
              #show the error message if the input is invalid
              messagebox.showerror("Error", "Invaldi Input")
              self.input_text.set("")
      elif text == "C":
            #clear the input field
            self.input_text.set("")
      else:
          # append the clicked button's text to the current input
          current_text = self.input_text.get()
          self.input_text.set(current_text + text)
 # Initialize the GUI Application
if __name__ == "__main__":
      root=tk.Tk()
      calculator = Calculator(root)
      root.mainloop()
             
          
             


     


   
