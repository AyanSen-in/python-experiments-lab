print ("welcome to my computer quize! ")

playing = input ("do you want to play ?  ")

if playing.lower() != "yes ":
    quit()

print("okay ! let's play :   " )
score = 0
answer = input (" what dose cpu stands for ? ")
if answer.lower()== "entral processing unit":
    print (' correct ')
    score += 1
else :
    print (" incorrect ! ")


answer = input ("what does gpu stands for ? ")
if answer.lower()== "graphical prosessing unit":
    print (' correct ')
    score += 1
else :
    print (" incorrect ! ")


answer = input ("what does ram stands for ? ")
if answer.lower()== "random acess memory":
    print (' correct ')
    score += 1
else :
    print (" incorrect ! ")


answer = input ("what does psu stands for ? ")
if answer.lower()== "power supply unit":
    print (' correct ')
    score += 1
else :
    print (" incorrect ! ")    

    
print("you got " + str(score) + " questions correct "  )     

