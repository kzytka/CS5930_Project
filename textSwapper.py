#import the csv file to be used assuming that the file has 4 columns
#with the word in English and then Arabic, then the changed words

import csv

#open the file that has the censored words and the changes
with open('iranCensorship.csv', newline='') as csvfile:

    #create a dictionary reader
    reader = csv.DictReader(csvfile) #this is a dictionary

    #print the file by each row
    #for row in reader:
    #    print(row['censoredWord'], row['translation'], 
    #          row['replacementWord'], row['translation2'])
        
    #open the file that is to be overwritten
    with open('test.txt', 'r') as test:

        #read the file
        contents = test.read()
        
    #iterate through censored word in dictionary
    for i in reader:

        #check if the word from the dictionary is in the file
        if i['censoredWord'] in contents:
                
            #replace the word
            contents.replace(i['censoredWord'], i['replacementWord'])
            print(f"overwrote {i['censoredWord']} with {i['replacementWord']}")
            #print(contents)
    
    #write to the file
    with open('test.txt', 'w') as test:
        test.write(contents)
        #print(contents)
