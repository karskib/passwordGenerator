import tkinter as tk
from tkinter.ttk import Combobox
import random
import pandas as pd


class PW:

    def __init__(self, master):
        master.title('Random password Generator')
        master.configure(bg='grey')

        self.letter = 8

        self.additional_frame = tk.Frame(master,width =30)
        self.additional_frame.grid(row=2,column = 0,sticky='nw')

        self.myText = tk.Label(master, text='PASSWORD GENERATOR', height=2,font= ('Mistral 13 bold'),width = 30,relief = tk.RAISED)
        self.myText.grid(row=0, column=0, sticky='nw')

        self.password_field = tk.Label(master, text='your password will appear here', bg='white',width = 30,relief=tk.RAISED)
        self.password_field.grid(row=1, column=0, sticky='nw')

        self.button_generate = tk.Button(self.additional_frame,height=2, text='Generate the password', font= ('Mistral 12 bold'), relief=tk.RAISED,
        command=self.generate_password,width=30)
        self.button_generate.grid(row=0, column=0,sticky='nw')

        self.frame_for_buttons = tk.Frame(master, bg='pink',width=30)
        self.frame_for_buttons.grid(row=3, column=0, sticky='nw')

        self.add_letters = tk.Button(self.frame_for_buttons, width=15, height=2, text='Add letters',relief=tk.RAISED,
                                     command=self.add_letter)
        self.add_letters.grid(row=2, column=0, sticky='w')

        self.reduce_letter = tk.Button(self.frame_for_buttons, width=15, height=2, text='Subtract letter',relief=tk.RAISED,
                                       command=self.subtract_letter)
        self.reduce_letter.grid(row=2, column=1, sticky='w')

        self.slider = tk.LabelFrame(master, text='Difficulty', relief=tk.SUNKEN,width=30)
        self.slider.grid(row=4, column=0, sticky='nw')

        self.show_letter_count = tk.Label(self.additional_frame, text=self.letter, relief = tk.RIDGE,width = 30)
        self.show_letter_count.grid(row=1, column=0)

        self.scale = tk.Scale(self.slider, orient=tk.HORIZONTAL, from_=0, to_=3,width = 15)
        self.scale.grid(row=0, column=0, sticky='nw')
        self.scale.set(0)

        self.copy = tk.Button(self.slider,text='Copy the password \nto clipboard',command = self.copy_to_clipboard,relief =tk.RAISED)
        self.copy.grid(row=0,column = 1,sticky='e',padx= 20)

    def generate_password(self):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
        password = ""
        if self.scale.get() == 0:
            top = tk.Toplevel()
            top.geometry('350x100-100-100')
            top.title = 'ERROR'
            tk.Label(top, text='Difficulty cannot be lower than 1', font=('Mistral 18 bold')).pack()
        for i in range(self.letter):
            if self.scale.get() == 1:
                password = password + random.choice(lower)
                self.password_field.configure(text=password)
            elif self.scale.get() == 2:
                password = password + random.choice(upper)
                self.password_field.configure(text=password)
            elif self.scale.get() == 3:
                password = password + random.choice(digits)
                self.password_field.configure(text=password)

    def add_letter(self):
        self.letter += 1
        self.show_letter_count.configure(text=f'No. letters \t {self.letter}')

    def subtract_letter(self):
        self.letter -= 1
        self.show_letter_count.configure(text=f'No. letters \t {self.letter}')

    def copy_to_clipboard(self):
        df = pd.DataFrame([self.password_field['text']])
        df.to_clipboard(index=False, header=False)

if __name__ == '__main__':
    root = tk.Tk()
    PW(root)
    tk.mainloop()
