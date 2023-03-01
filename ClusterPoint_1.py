import mysql.connector
from sklearn.cluster import KMeans
import numpy as np
import sqlite3

# Connect to the MySQL server
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bill1567",
        database="crawler"
    )
if(mydb):
    print("Connection Successful")
else:
    print("Connection Fail")

# Create a cursor object
mycursor = mydb.cursor()
#turn off safe mode

mycursor.execute("SET SQL_SAFE_UPDATES = 0")
mydb.commit()
mycursor.execute("Update ProviderDriveOption SET GbPerPrice=ROUND(Price/Capacity, 4)")
mydb.commit()
#----------------------------------------------------------------------
#ProviderHostOption
#PricePoint
query = "SELECT Price FROM ProviderHostOption"
mycursor.execute(query)
Prices = [Prices[0] for Prices in mycursor.fetchall()]

# Convert data to a NumPy array
Prices = np.sort(Prices, axis=0, kind='quicksort')[::-1]
#Prices = Prices.astype(int)
Prices = np.array(Prices).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=10, n_init=5)
clusters = kmeans.fit_predict(Prices)

# Zip the data and labels together
clustered_data = list(zip(Prices, kmeans.labels_))

# sort the Prices and corresponding labels
sorted_Prices, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Price" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (price, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 0.5
        label = new_label
        clustered_data[i] = (price, label)
    else:
        label = new_label
        clustered_data[i] = (price, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

# Iterate through the re-labeled data and update the "PricePoint" field
for price, label in clustered_data:
    query = "UPDATE ProviderHostOption SET PricePoint=%s WHERE ROUND(Price, 4) = %s"
    #need to convert into int
    values = (label, price[0])
    mycursor.execute(query, values)
    mydb.commit()
print('\n')
#----------------------------------------------------------------------
#CPUPonit
query = "SELECT Core FROM ProviderHostOption"
mycursor.execute(query)
CPUs = [CPUs[0] for CPUs in mycursor.fetchall()]

# Convert data to a NumPy array
CPUs = np.sort(CPUs, axis=0)
CPUs = CPUs.astype(int)
CPUs = np.array(CPUs).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(CPUs)

# Zip the data and labels together
clustered_data = list(zip(CPUs, kmeans.labels_))

# sort the CPUs and corresponding labels
sorted_CPUs, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "CPU" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (CPU, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (CPU, label)
    else:
        label = new_label
        clustered_data[i] = (CPU, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

# Iterate through the re-labeled data and update the "CPUPoint" field
for CPU, label in clustered_data:
    query = "UPDATE ProviderHostOption SET CPUPoint=%s WHERE Core = %s"
    #need to convert into int
    values = (label, int(CPU[0]))
    mycursor.execute(query, values)
    mydb.commit()
print('\n')
#----------------------------------------------------------------------
#RamPoint
query = "SELECT Ram FROM ProviderHostOption"
mycursor.execute(query)
Rams = [Rams[0] for Rams in mycursor.fetchall()]

# Convert data to a NumPy array
Rams = np.sort(Rams, axis=0)
Rams = Rams.astype(int)
Rams = np.array(Rams).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(Rams)

# Zip the data and labels together
clustered_data = list(zip(Rams, kmeans.labels_))

# sort the Rams and corresponding labels
sorted_Rams, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Ram" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (Ram, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (Ram, label)
    else:
        label = new_label
        clustered_data[i] = (Ram, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

# Iterate through the re-labeled data and update the "RamPoint" field
for Ram, label in clustered_data:
    query = "UPDATE ProviderHostOption SET RamPoint=%s WHERE Ram = %s"
    #need to convert into int
    values = (label, int(Ram[0]))
    mycursor.execute(query, values)
    mydb.commit()
print('\n')
#----------------------------------------------------------------------
#BandPoint
query = "SELECT BandWidth FROM ProviderHostOption"
mycursor.execute(query)
BandWidth = [BandWidth[0] for BandWidth in mycursor.fetchall()]

# Convert data to a NumPy array
BandWidth = np.sort(BandWidth, axis=0)
BandWidth = BandWidth.astype(int)
BandWidth = np.array(BandWidth).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(BandWidth)

# Zip the data and labels together
clustered_data = list(zip(BandWidth, kmeans.labels_))

# sort the BandWidth and corresponding labels
sorted_BandWidth, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Band" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (Band, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (Band, label)
    else:
        label = new_label
        clustered_data[i] = (Band, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

# Iterate through the re-labeled data and update the "BandPoint" field
for Band, label in clustered_data:
    query = "UPDATE ProviderHostOption SET BandPoint=%s WHERE BandWidth = %s"
    #need to convert into int
    values = (label, int(Band[0]))
    mycursor.execute(query, values)
    mydb.commit()
print('\n')

mycursor.execute("UPDATE ProviderHostOption SET AveragePoint = (PricePoint + CPUPoint + RamPoint + BandPoint)/4")
mydb.commit()

#---------------------------------
#drive
# Retrieve the data from the "Price" field
query = "SELECT GbPerPrice FROM ProviderDriveOption"
mycursor.execute(query)
prices = [price[0] for price in mycursor.fetchall()]

# Convert data to a NumPy array
prices = np.sort(prices, axis=0, kind='quicksort')[::-1]
prices = np.array(prices).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(prices)

# Zip the data and labels together
clustered_data = list(zip(prices, kmeans.labels_))

# sort the prices and corresponding labels
sorted_prices, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Price" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (price, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (price, label)
    else:
        label = new_label
        clustered_data[i] = (price, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

    # Iterate through the re-labeled data and update the "PricePoint" field
for price, label in clustered_data:
    query = "UPDATE ProviderDriveOption SET PricePoint=%s WHERE ROUND(GbPerPrice, 7) = %s"
    values = (label, price[0])
    mycursor.execute(query, values)
    # Commit the changes to the database
    mydb.commit()

#----------------------------------------------------------------------
#Update point for number of ppl
# Retrieve the data from the "Price" field
query = "SELECT MaxPeople FROM ProviderDriveOption"
mycursor.execute(query)
peoples = [peoples[0] for peoples in mycursor.fetchall()]

# Convert data to a NumPy array
peoples = np.sort(peoples, axis=0)
#peoples = peoples.astype(int)
peoples = np.array(peoples).reshape(-1, 1)

# Cluster data using KMeans
kmeans = KMeans(n_clusters=5, n_init=5)
clusters = kmeans.fit_predict(peoples)

# Zip the data and labels together
clustered_data = list(zip(peoples, kmeans.labels_))

# sort the peoples and corresponding labels
sorted_peoples, sorted_labels = zip(*sorted(clustered_data, key=lambda x: x[0], reverse=True))

#Re-labeling so that both data "Price" and "label" are in ascending order
old_label = -1
new_label = 0
for i, (people, label) in enumerate(clustered_data):
    if label != old_label:
        old_label = label
        new_label += 1
        label = new_label
        clustered_data[i] = (people, label)
    else:
        label = new_label
        clustered_data[i] = (people, label)

# print the re-labeled data
for element in clustered_data:
    print(element, end='\n')

# Iterate through the re-labeled data and update the "peoplePoint" field
for people, label in clustered_data:
    query = "UPDATE ProviderDriveOption SET PeoplePoint=%s WHERE MaxPeople = %s"
    #need to convert into int
    values = (label, int(people[0]))
    mycursor.execute(query, values)
    mydb.commit()

#---------------------------------------------------------------------------------
# take average for the getapp point where point = NULL
# Select all non-NULL values from GetAppPoint column
mycursor.execute("SELECT GetAppPoint FROM ProType WHERE GetAppPoint IS NOT NULL")

# Calculate the average of the selected values
result = mycursor.fetchall()
total = sum([row[0] for row in result])
num_values = len(result)
average = total / num_values

# Replace all NULL values with the calculated average
mycursor.execute("UPDATE ProType SET GetAppPoint = %s WHERE GetAppPoint IS NULL", (average,))
mydb.commit()

mycursor.execute("UPDATE ProviderDriveOption SET AveragePoint = (PricePoint + PeoplePoint)/2")
mydb.commit()

mycursor.close()
mydb.close()