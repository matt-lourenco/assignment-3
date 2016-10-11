# Created by: Matthew Lourenco
# Created on: 6 Oct 2016
# This is a program that calculates the price of a pizza based on size and toppings

import ui

HST = 0.13

def calculate_touch_up_inside(sender):
    #calculates the price of the custom pizza
    
    #input
    size = view['input_size_textfield'].text
    toppings = int(view['input_toppings_textfield'].text)
    
    if size == '1' or size == 'large' or size == 'Large':
        
        if toppings == 1 or toppings == 2 or toppings == 3 or toppings == 4:
            #process
            
            pizza = 6
            
            subtotal = pizza + (1 + (int(toppings) - 1)*0.75)
            subtotalHST = subtotal * HST
            total = subtotal + subtotalHST
            
            #output
            
            view['subtotal_label'].text = 'Subtotal: $' + str(subtotal)
            view['hst_label'].text = 'HST: $' + str(round(subtotalHST, 2))
            view['total_label'].text = 'Total: $' + str(round(total, 2))
        
        else:
            #output
            
            view['error_label'].text = 'Enter a valid number of toppings.'
    
    elif size == '2' or size == 'extra' or size == 'Extra':
        
        if toppings == 1 or toppings == 2 or toppings == 3 or toppings == 4:
            #process
            
            pizza = 10
            
            subtotal = pizza + (1 + (int(toppings) - 1)*0.75)
            subtotalHST = subtotal * HST
            total = subtotal + subtotalHST
            
            #output
            
            view['subtotal_label'].text = 'Subtotal: $' + str(subtotal)
            view['hst_label'].text = 'HST: $' + str(round(subtotalHST, 2))
            view['total_label'].text = 'Total: $' + str(round(total, 2))
        
        else:
            #output
            
            view['error_label'].text = 'Enter a valid number of toppings.'
    
    else:
        view['error_label'].text = 'Enter a valid pizza size.'

view = ui.load_view()
view.present('full_screen')
