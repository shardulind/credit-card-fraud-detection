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




def user_login(username,password):
    csvfile = open(filename, 'r')
    csvreader = csv.reader(csvfile)
    csvreader.__next__()

    for user in csvreader:
        if username == user[5]:
            if password == user[6]:
                return True
            else:
                return False
        else:
            return False




def add_new_user(name,ccnumber, mno, email, country, username, password):

#copies earlier stored data
    temp = open(filename, 'r')
    csvreader = csv.reader(temp)
    fields=csvreader.__next__()

    all_users=[]
    all_users.append(fields)
    for row in csvreader:
        all_users.append(row)

    print(all_users)
    temp.close()

#opens again csvfile in write mode... Note: writing anything clears every thing on it.. it doesnt append directly
    csvfile = open(filename, 'w')
    new_user = [name,ccnumber,mno,email,country,username,password]

    csvwriter = csv.writer(csvfile)
    all_users.append(new_user)          #appending new user data to earlier fetched list -> all_users

    csvwriter.writerows(all_users)

    csvfile.close()
