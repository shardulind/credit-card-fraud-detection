import csv
filename = "users.csv"


def read_all_users():
    fields = []
    rows = []

    #reading csv
    csvfile = open(filename , 'r')

    #csvfile object reader
    csvreader = csv.reader(csvfile)

    #fields name from 1st row
    fields = csvreader.__next__()

    #getting all data row by rows
    for row in csvreader:
        rows.append(row)


    print(rows)
    return rows



#login function
def user_login(username,password):
    csvfile = open(filename, 'r')   #reading csv file
    csvreader = csv.reader(csvfile)
    csvreader.__next__()

    #reading users file line by line
    for user in csvreader:
        print(user)

        #users[5] is stored username
        #users[5] is password
        #if entered username exists in users.csv
        if username == user[5]:
            if password == user[6]:
                return True
            else:
                return False

    return False



#function to register a new user
def add_new_user(name,ccnumber, mno, email, country, username, password):

#copies earlier stored data in users.csv file
    temp = open(filename, 'r')
    csvreader = csv.reader(temp)
    fields=csvreader.__next__()

    all_users=[]
    all_users.append(fields)
    for row in csvreader:
        all_users.append(row)

    print(all_users)
    temp.close()

#opens again csvfile in write mode...
#Note: writing anything clears every thing on it.. it doesnt append directly
#thus reading all data in all_users variable

#now opening users.csv file in write mode
    csvfile = open(filename, 'w')
    new_user = [name,ccnumber,mno,email,country,username,password]

    csvwriter = csv.writer(csvfile)
    all_users.append(new_user)          #appending new user data to earlier fetched list -> all_users

    csvwriter.writerows(all_users)

    csvfile.close()
