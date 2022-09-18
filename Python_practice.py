counties_dict = ['Arapahoe', 'Denver', 'Jefferson']
if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties.')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties.')



counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dict:
    print(county)


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dict.keys():
    print(county)


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for voters in counties_dict.values():
    print(voters)


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dict.items():
    print(county, voters)


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dict.items():
    print(county, voters)


voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
                {'county':'Denver', 'registered_voters': 463353},
                {'county':'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])       

for county_dict in voting_data:
    print(county_dict['county'])


# f-strings can be used to print out the keys or values of a dictionary
my_votes = int(input("How many votes did you get in the electioin?"))
total_votes = int(input("what is the total votes in the election?"))
print(f"T received {my_votes / total_votes * 100}% of the total votes.")


#Using f-strings with dictionaries
counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candiddate get in the election?"))
total_votes = int(input("What is the total number of votes in the election"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#didn't work
voting_data = [{'county':'Arapahoe', 'registered_voters': 422829},
                {'county':'Denver', 'registered_voters': 463353},
                {'county':'Jefferson', 'registered_voters': 432438}]
for county, registered_voters in voting_data.items():
    print(f"{county} county has {registered_voters:,} registered voters.")