from sklearn import tree

#Rough     1
#0    0

def main():
    print("Ball Classification case Study")

    #Load the Data
    BallFeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1], [92,0],[35,1],[35,1],[35,1], [96,0], [43,1],[110, 0], [35,1],[95, 0]]

    Labels = ["Tennis" , "Tennis" , "Cricket" , "Tennis" , "Cricket" , "Tennis" , "Cricket" "Tennis" , "Tennis" , "Tennis" , "Cricket" , "Tennis" , "Cricket" , "Tennis" , "Cricket" , "" ]

    obj = tree.DecisionTreeClassifier()  #Decide The Algorithm

    obj = obj.fit(BallFeatures , Labels) #Train the Alogtirhm

    print(obj.predict([[36 , 1] , [91 , 0]])) #Test The Algorithm


if __name__=="__main__":
    main()