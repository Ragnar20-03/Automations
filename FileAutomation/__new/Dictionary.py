
dict = {"Roshan" : 20 , "Anurag" : 22 , 
        "Home" : {
            "kalyani" : 24 , 
            "saurabh" : 29
        }}
print (dict)

print ("---"*80)

print(dict["Roshan"])

print ("-*10 Myyyy")
dict["Roshan"] = [100]
dict["Roshan"].append(232323)
dict["Roshan"].append("After append")

print("Roshan : " , dict["Roshan"])
print ("Length of Roshan : " , len(dict["Roshan"]))
