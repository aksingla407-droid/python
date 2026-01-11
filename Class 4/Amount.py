amount= int(input("Enter Amonut:"))
note_1= amount//100
note_2= (amount%100)//50
note_3= ((amount%100)%50)//10
print ("notes of 100 required is",note_1)
print ("notes of 50 required is",note_2)
print ("notes of 10 required is",note_3)

