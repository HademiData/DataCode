

# FUNCTION 1

def meanCalc(myList):
    container = 0 #the summing variable
    for data in myList:
        #looping through the given list and summing up the values  
        container= data+container
    mean = container/(len(myList)) # calculating the mean of the list values
    return mean
# print (meanCalc([1,2,3,4]))



# FUNCTION 2
def readColumn(dataFile, colNum):
    dummyList=[] # to store the data for further analysis
    result=[] # to store the data in the column specified
    # opening the file 
    with open(dataFile, 'r') as file:
        # storing each row in the file as a list
        for line in file:      
            line = line.replace("\n", "").split(',') # cleaning the file 
            # this code is to convert all string numbers to floats
            for i in range(0, len(line)):
                try:
                    line[i] = float(line[i])
                except ValueError:
                    line[i] = line[i]
                
            dummyList.append(line) # replacing the dummylist with the modified strings to float
            
        columName = dummyList[0][colNum] # stores the name of the column
        dummyList= dummyList[1:]  # grabs the lists in the dummylist excluding the list containing the column names
        
        # getting the data for the specified colum number and stores it in the result list
        for data in dummyList:
            
            result.append(data[colNum])
            
    return result, columName


#print(readColumn('task1.csv', 4))


# FUNCTION 3

def readCsvToMemory(dataFile):
    StorageDict = {}
    
    with open(dataFile, 'r') as file:
        for line in file:      
            line = line.replace("\n", "").split(',') 
        
        lengthOfRow = len(line)
        for i in range(0,lengthOfRow):
            temp = readColumn(dataFile, i)
            StorageDict[temp[1]] = temp[0]
            
    return StorageDict
  
#print(readCsvToMemory('task1.csv'))



# FUNCTION 4
def PearsonCorr(list1,list2):
    # renaming the list for convenience
    # list1 = x and list2 = y 
    x =list1
    y =list2       
    if len(x)==len(y):
        
        
        mean_x = meanCalc(x) # mean for list 1
        mean_y = meanCalc(y) # mean for list 2
        
        x_deviations = []
        y_deviations = []
        for i in range(0, len(x)):
            # len(X) is used because all the generated
            #lists are of the same length
            
            # creating the list of deviations (x-xbar) for both list values
            x_deviations.append(x[i]-mean_x)
            y_deviations.append(y[1]-mean_y)
         
        
        multiple_of_deviations = []
        for i in range(0,len(x)):
            multiple_of_deviations.append(x_deviations[i]*y_deviations[i])
            
        
        Sum_multiple_of_deviations = 0
        for data in multiple_of_deviations:
            # updating the value of Sum_multiple_of_deviations by adding each value in the 
            # multiple_of_deviations list
            
            Sum_multiple_of_deviations = Sum_multiple_of_deviations+data
        
            # this sum_multiple_of_deviations is the numerator for the pearsons correlation coefficiant
            # calculation
        #print(Sum_multiple_of_deviations)
        
        # now finding  the squared of deviation values for each elements
        x_deviations_squared = [ k**k for k in x_deviations]
        y_deviations_squared = [ p**p for p in y_deviations]
            
        # now finding the  sum of the deviations squared for each list1 or x and list2  or y  
        sum_x_deviations_squared = 0
        sum_y_deviations_squared = 0
        for k in range(0,len(x)):
            # now adding all the elemants in x_deviations_squared and y_deviations_squared together
            sum_x_deviations_squared = sum_x_deviations_squared+x_deviations_squared[k]
            sum_y_deviations_squared = sum_y_deviations_squared+y_deviations_squared[k]
            
        pearsons_corr_coefficient = (Sum_multiple_of_deviations)/((sum_x_deviations_squared*sum_y_deviations_squared)**(1/2))
        
        
        return float(pearsons_corr_coefficient )   
    
    else:
        return 'ERROR the input Lists are not of the same length'

A = [85, 29, 35, 55]
B = [ 85, 29, 35, 55]


#print(PearsonCorr(A,B))







# FUNCTION 5
def setOfPearsonCorrelation(datafile):
    temp = readCsvToMemory(datafile)
    sol = []

    for k in temp:
        for i in temp:
            if k!=i:
                a=(k , i , PearsonCorr(temp[k],temp[i]))
                sol.append(a)
    print(sol)
    return False


setOfPearsonCorrelation('task1.csv')

# FUNCTION 6

def CustomTable(listOfCorrCoeff, bordChar, *columns):

    temp = [] # this temporary list holds the columns specified in list formatt for ease in analysis
    for column in columns:
        # converting the columns specified in to the table format
        temp.append(column)
        tempString =f"{bordChar} "+f' { bordChar } '.join(temp) + f" {bordChar}" # formatting the rows in the table
                
    print(" "*16 +borChar*len(tempString))     
    print("                "+tempString)      
    
    pearsonCorrStorage =listOfCorrCoeff 
    for data in temp:
        for x,y,z in listOfCorrCoeff:
            if x!=y and x==data:
                coeff= z

            elif x==y and x==data:
                coeff = '-'
            




 