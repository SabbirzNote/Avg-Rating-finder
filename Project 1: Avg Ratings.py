opened_file = open('Applestore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
apps_data = apps_data[1: ]

rating_sum = []
for row in apps_data:
    rating = float(row[1])
    rating_sum.append(rating)
total = sum(rating_sum)
avg_rating = total/len(rating_sum)
avg_rating = round(avg_rating, 1)
    
print(avg_rating)
