places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
# def cToF(arr):
#     FPlaces = []
#     for p in places:
#         farh = p[1] *(9/5) +32
#         city = p[0]
#         new_tup = (city, farh)
#         FPlaces.append(new_tup)
#     return(new_tup)
# list(map(cToF,places))

temps = list(map(lambda x: (9/5)* x + 32, (lis[1] for lis in places)))
cities = list(map(lambda x: x, (lis[0] for lis in places)))


# cities = list(map(lambda x: x, (lis[0] for lis in places)))
# new_list = [cities,temps]
# print(new_list)
# final_list = []
# for n in new_list:
    

new_temps = []
for city in cities:
    for temp in temps:
        tup = (city,temp)
        new_temps.append(tup)
print(new_temps)