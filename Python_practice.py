print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)
numbers =[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_tuple
for i in range(len(counties_tuple)):
    print(counties_tuple[i])
for county in counties_tuple:
    print(county)
range(5)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
      print(voting_data[i])

for county_dict in voting_data:
    print(voting_data)

for county_dict in voting_data:
        print(county_dict['registered_voters'])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    for county, voters in counties_dict.items():
        print(
    f"{county} county has {voters} registered voters.")
