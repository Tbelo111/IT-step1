#ordered
my_list =["khinkali", "mwvadi", "qababi", 50]
print(my_list)

#changeable
my_list.append("soko") #ბოლოში ჩამატება


#list can contain duplicates
my_list.append("mwvadi")
my_list[3] = "lobiani" #შეცვლა
print(my_list)

my_list.insert(2, "sulguni") # ჩამატება
print(my_list) 

my_list.remove("qababi") # სიიდან წაშლა
print(my_list)
#del my_list   # სიის წაშლა

#my_list.clear() # სიის გასუფთავება

my_list.sort(reverse=True)
print(my_list)