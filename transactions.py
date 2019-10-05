import csv
filename="transactions.csv"

def add_transaction_detail(ccnumber, amount, country):
    temp = open(filename,'r')
    csvreader = csv.reader(temp)
    fields = csvreader.__next__()

    all_transactions=[]
    all_transactions.append(fields)
    for row in csvreader:
        all_transactions.append(row)

    print(all_transactions)
    temp.close()

    new_transaction = [ccnumber, amount, country]
    all_transactions.append(new_transaction)

    csvfile = open(filename, 'w')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(all_transactions)

    csvfile.close()


def is_unusual_payment(ccnumber, amount, country):
        temp = open(filename,'r')
        csvreader = csv.reader(temp)
        fields = csvreader.__next__()



        sum = 0
        row_count =0;
        for row in csvreader:
            if row[0] == ccnumber:
                user_country = row[2]
                row_count +=1
                sum = sum + int(row[1])

        average_payment = sum/row_count

        print(average_payment)
        temp.close()

        if float(amount) > average_payment*1.45:
            return True
        elif country != user_country:
            return True
        else:
            return False

print(is_unusual_payment('6969','6000','INDIA'))
