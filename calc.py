import tkinter as tk

calculation=""
def add_to_calc(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

#=======================================================
def evaluate_calc():
    global calculation
    try:
        calculation =str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
        
#=========================================================================        
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
#============================================================================

root=tk.Tk()
root.title("calculator")
root.geometry("300x320")
#========================================================================
text_result=tk.Text(root,height=2,width=16,bg="violet",bd=5,font=("Arial",24))
text_result.grid(columnspan=5)
#==========================================================================
btn_1=tk.Button(root,text="1",command=lambda:add_to_calc(1),bd=5,width=5,font=("Arial",16))
btn_1.grid(row=2,column=1)
btn_2=tk.Button(root,text="2",command=lambda:add_to_calc(2),bd=5,width=5,font=("Arial",16))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(root,text="3",command=lambda:add_to_calc(3),bd=5,width=5,font=("Arial",16))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(root,text="4",command=lambda:add_to_calc(4),bd=5,width=5,font=("Arial",16))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(root,text="5",command=lambda:add_to_calc(5),bd=5,width=5,font=("Arial",16))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(root,text="6",command=lambda:add_to_calc(6),bd=5,width=5,font=("Arial",16))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(root,text="7",command=lambda:add_to_calc(7),bd=5,width=5,font=("Arial",16))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(root,text="8",command=lambda:add_to_calc(8),bd=5,width=5,font=("Arial",16))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(root,text="9",command=lambda:add_to_calc(9),bd=5,width=5,font=("Arial",16))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(root,text="0",command=lambda:add_to_calc(0),bd=5,width=5,font=("Arial",16))
btn_0.grid(row=5,column=2)
btn_plus=tk.Button(root,text="+",command=lambda:add_to_calc("+"),bd=5,width=5,font=("Arial",16))
btn_plus.grid(row=2,column=4)
btn_min=tk.Button(root,text="-",command=lambda:add_to_calc("-"),bd=5,width=5,font=("Arial",16))
btn_min.grid(row=3,column=4)
btn_mult=tk.Button(root,text="*",command=lambda:add_to_calc("*"),bd=5,width=5,font=("Arial",16))
btn_mult.grid(row=4,column=4)
btn_div=tk.Button(root,text="/",command=lambda:add_to_calc("/"),bd=5,width=5,font=("Arial",16))
btn_div.grid(row=5,column=4)
btn_open=tk.Button(root,text="(",command=lambda:add_to_calc("("),bd=5,width=5,font=("Arial",16))
btn_open.grid(row=5,column=1)
btn_close=tk.Button(root,text=")",command=lambda:add_to_calc(")"),bd=5,width=5,font=("Arial",16))
btn_close.grid(row=5,column=3)
btn_clear=tk.Button(root,text="C",command=clear_field,width=11,bd=5,font=("Arial",16))
btn_clear.grid(row=6,column=1,columnspan=2)
btn_equals=tk.Button(root,text="=",command=evaluate_calc,width=11,bd=5,font=("Arial",16))
btn_equals.grid(row=6,column=3,columnspan=2)

root.mainloop()
