import customtkinter
import operator
import re


app =  customtkinter.CTk()
#make the res like a phone so its more like the calc that comes with windows
app.geometry("320x500")
app.grid_columnconfigure((0,1,2,3), weight=1)
app.grid_rowconfigure(0, weight=2)
app.grid_rowconfigure((1, 2, 3, 4), weight=1)
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
#function that will be called when a number button is pressed\
just_calculated = False
number_list1 = []
numbers=[]
operations=[]





textbox= customtkinter.CTkTextbox(app, width= 500, height=100,font=("Arial", 60), wrap='none')
textbox.grid(row=0, column=0,  columnspan=4, padx=10, pady=0, sticky='nsew')

button1 = customtkinter.CTkButton(app, text="1", command=lambda: number_button(1), width=40, height=40)
button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button2 = customtkinter.CTkButton(app, text="2", command=lambda: number_button(2), width=40, height=40)
button2.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
button3 = customtkinter.CTkButton(app, text="3", command=lambda: number_button(3), width=40, height=40)
button3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
button4 = customtkinter.CTkButton(app, text="4", command=lambda: number_button(4), width=40, height=40)
button4.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
button5 = customtkinter.CTkButton(app, text="5", command=lambda: number_button(5), width=40, height=40)
button5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
button6 = customtkinter.CTkButton(app, text="6", command=lambda: number_button(6), width=40, height=40)
button6.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')
button7 = customtkinter.CTkButton(app, text="7", command=lambda: number_button(7), width=40, height=40)
button7.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button8 = customtkinter.CTkButton(app, text="8", command=lambda: number_button(8), width=40, height=40)
button8.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
button9 = customtkinter.CTkButton(app, text="9", command=lambda: number_button(9), width=40, height=40)
button9.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
button0 = customtkinter.CTkButton(app, text="0", command=lambda: number_button(0), width=40, height=40)
button0.grid(row=4, column=1, padx=5, pady=5, sticky='nsew')

#special buttons
buttonplus = customtkinter.CTkButton(app, text="+", command=lambda: operation('plus'), width=40, height=40)
buttonplus.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
buttonminus = customtkinter.CTkButton(app, text="-", command=lambda: operation('minus'), width=40, height=40)
buttonminus.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')
buttontimes = customtkinter.CTkButton(app, text="X", command=lambda: operation('multiply'), width=40, height=40)
buttontimes.grid(row=3, column=3, padx=5, pady=5, sticky='nsew')
buttondivide = customtkinter.CTkButton(app, text="÷", command=lambda: operation("divide"), width=40, height=40)
buttondivide.grid(row=4, column=3, padx=5, pady=5, sticky='nsew')
buttonclear = customtkinter.CTkButton(app, text="CE", command=lambda: clear("clear"), width=40, height=40)
buttonclear.grid(row=4, column=2, padx=5, pady=5, sticky='nsew')
buttondecimal = customtkinter.CTkButton(app, text=".", command=lambda: decimal('.'), width=40, height=40)
buttondecimal.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')
buttonenter = customtkinter.CTkButton(app, text="↵", command=lambda: equal(), width=40, height=40)
buttonenter.grid(row=5, column=3, padx=5, pady=5, sticky='nsew')

#    asdf=textbox.get("0.0", "end")
#use this later for getting the numbers 


def number_button(s):
    textbox.configure(state="normal")
    global just_calculated
    if just_calculated:
        textbox.delete("0.0", "end")
        just_calculated = False
    
    s=int(s)
    number_list1.append(s)
    strs=str(s)
    ohio=""
    ohio += strs
    for number in ohio:
        textbox.insert("end", number) 
    textbox.configure(state="disabled")
def decimal(s):
    textbox.configure(state="normal")
    number_list1.append(s)
    strs=str(s)
    ohio=""
    ohio += strs
    for number in ohio:
        textbox.insert("end", number) 
    textbox.configure(state="disabled")

def clear(op):
    textbox.configure(state="normal")
    if op == 'clear':
        numbers.clear()
        operations.clear()
        textbox.delete("0.0", "end")
        textbox.configure(state="disabled")

def operation(op):
    op.strip()
    textbox.configure(state="normal")
    if operations:
        nums = textbox.get("0.0", "end")
        nums=nums.strip()
        nums=float(nums)
        numbers.append(nums)
        oper=operations[-1]
        result = oper(numbers[-2], numbers[-1])
        if result.is_integer():
            result=int(result)
        numbers.append(result)
        textbox.configure(state="normal")
        textbox.delete("0.0", "end")
        textbox.insert("0.0", result)
        textbox.configure(state="disabled")
        global just_calculated
        just_calculated = True
        operations.clear()
        if op == "plus":
            operations.append(operator.add)
        elif op == "minus":
            operations.append(operator.sub)
        elif op == "multiply":
            operations.append(operator.mul)
        elif op == "divide":
            operations.append(operator.truediv)
        

    if op == 'plus':

        nums = textbox.get("0.0", "end")
        textbox.delete("0.0", "end")
        nums.strip()
        nums=float(nums)
        
        numbers.append(nums)
        
        textbox.configure(state="disabled")
        operations.append(operator.add)
    if op == 'minus':

        nums = textbox.get("0.0", "end")
        nums.strip()
        textbox.delete("0.0", "end")
        nums=float(nums)
        numbers.append(nums)
        
        
        textbox.configure(state="disabled")
        operations.append(operator.sub)
    if op == 'divide':

        nums = textbox.get("0.0", "end")

        nums.strip()
        textbox.delete("0.0", "end")
        nums=float(nums)
        numbers.append(nums)
        
        textbox.configure(state="disabled")
        operations.append(operator.truediv)
    if op == 'multiply':

        nums = textbox.get("0.0", "end")
        nums.strip()
        textbox.delete("0.0", "end")
        nums=float(nums)
        numbers.append(nums)
        
        textbox.configure(state="disabled")
        operations.append(operator.mul)
    
def equal():
    nums = textbox.get("0.0", "end")
    nums=nums.strip()
    nums=float(nums)
    numbers.append(nums)
    oper=operations[-1]
    result = oper(numbers[-2], numbers[-1])
    if result.is_integer():
        result=int(result)
    numbers.append(result)
    textbox.configure(state="normal")
    textbox.delete("0.0", "end")
    textbox.insert("0.0", result)
    textbox.configure(state="disabled")
    global just_calculated
    just_calculated = True
    operations.clear()



app.mainloop()