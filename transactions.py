#transactions module
#functions : 1) add_transaction_detail
#             2) is_unusual_payment


import csv
filename="transactions.csv"

#functions adds transaction record in transactions.csv file

def add_transaction_detail(ccnumber, amount, country):
    #opening transactions.csv file in temp variable
    temp = open(filename,'r')

    #csvreader is object which reads csv file
    csvreader = csv.reader(temp)


    #defining an list to store all earlier transactions
    all_transactions=[]

    #reading csv file row by row
    for row in csvreader:
        all_transactions.append(row)        #appending csv file in all_transactions variable (list)

    print(all_transactions)
    temp.close()                            #closing temp


    #making list (row) of new_transaction which is about to be added into csv file
    new_transaction = [ccnumber, amount, country]
    all_transactions.append(new_transaction)    #appending new transaction


    #opening csv file in write mode
    csvfile = open(filename, 'w')
    #object for csvwriter
    csvwriter = csv.writer(csvfile)

    #writing all_transactions along with new transaction into the csv file
    csvwriter.writerows(all_transactions)

    #closing csv file
    csvfile.close()



# function to check if transaction is unusal or not
# this function finds average of a credit card number
#   and check if ongoing payment amount is 45% more than usual credit card spending
#   also checks if country is same or different
#
# if unusal or fraud : returns true
# if not unusal or not fraud : returns false

def is_unusual_payment(ccnumber, amount, country):

        #opening transactions.csv in temp
        temp = open(filename,'r')
        csvreader = csv.reader(temp)
        fields = csvreader.__next__()


        #to store sum amount and row_count to count no. of transactions of given ccnumber
        sum = 0
        row_count =0;

        #reading csv file row by row
        #row[0] : ccnumber
        #row[1] : amount
        #row[2] : country

        for row in csvreader:
            if row[0] == ccnumber:      #finding entered ccnumber
                user_country = row[2]
                row_count +=1
                sum = sum + int(row[1])


        #if row_count is zero.. means new user has zero transactions in transactions.csv
        #it returns false... because less data available to find trend about the credit card number
        if row_count == 0:
            return False
        elif row_count < 10:
            return False

        #calculating average
        average_payment = sum/row_count

        print(average_payment)
        temp.close()

        #checking if transaction amount is 45% greater than usual spending
        if float(amount) > average_payment*1.45:
            return True
        #checking if country is different
        elif country != user_country:
            return True
        else:
            return False
