

def fair_sharer(values, num_iterations, share=0.1):
    #Koopie eingabe array
    values_new = values.copy()
    
    for i in range(num_iterations):
        #höchsterr wert um values_new array
        h_Wert = values_new.index(max(values_new))
        amount = share * values_new[h_Wert] #amount = Wert der verteilt werden soll
        
        # aktualisiert den linken Nachbarn 
        links = (h_Wert - 1) % len(values_new)
        values_new[links] += amount / 2
        
        # aktualisiert den rechten Nachbarn 
        rechts = (h_Wert + 1) % len(values_new)
        values_new[rechts] += amount / 2
        
        # reduziert den höchsten Wert um den umverteilten Betrag
        values_new[h_Wert] -= amount
    
    
    return values_new