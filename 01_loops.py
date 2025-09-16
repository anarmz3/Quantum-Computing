# loops and vectors
# hot equal or more then 176F; warm is in between; cold is less  or equal to 75F

temperature = 110
v_temperature = [66,70,74,79,85,90,101,180,190,200,210]
        #indexes  0, 1, 2, 3, 4, 5, 6
for i in range(0,len(v_temperature)):
    print("Index:", i, "Element:", v_temperature[i])
    if (v_temperature[i] >=175):
        print("This day is hot!")
    elif (v_temperature[i] <=75):
        print("This day is cold")
    elif (v_temperature[i] > 75 and v_temperature[i] < 176):
        print("This day is warm!")