import random as rd
import os
import datetime


def get_place(to_clean):
	#print(f"get_place => {len(people_aux)} people")
	for i in range(len(people_aux)):
		#print(f"{i}")
		num = rd.randrange(0,len(people_aux))
		person = people_aux[num]
		if to_clean in dicio[person]:
			dicio_remove[person] = to_clean
			places_aux.remove(to_clean)
			people_aux.remove(person)
			return person
	return "Error"

#def ResetControl():
	# for person in people:
	# 	f.write(f"{person}")
	# 	for place in places:
	# 		f.write(f", {place}")
	# 	f.write("\n") 

	# f.close()

people = ["Cabeca", "Cafe", "Bordel", "Xupeta", "Moises", "Tesouro", "Desisto", "Tampinha", "P4", "Castro"]
places = ["Sala + Corredor Frente", "Lavabo + Corredor Quartos", "Banheiro Meio", "Banheiro Suite", "Fundo", "Garagem + Frente", "Garagem + Frente", "Salol + Sala Antiga", "Lavanderia + Banheiro Fundo + Cozinha", "Lavanderia + Banheiro Fundo + Cozinha"]
size_mandala = len(people)
dicio = {}

for person in people:
	dicio[person] = places.copy()

if len(places) != size_mandala:
	print("\nCorrige as listas hardcodadas corno\n")

today = datetime.datetime.today()
history = open(f"Tasks/Tasks Limpeza Pulero {today.strftime('%d-%m')}.txt", "w")

for week in range(0, size_mandala):
	dicio_remove = {}
	#reset = 0

	# f = open("PeopleAndPlaces.txt", "r")
	# #Populate dicio with left places to person do
	# for person in people:
	# 	temp = line.strip().split(", ")
	# 	size = len(temp)
	# 	dicio[temp[0]] = []
	# 	for i in range(1,size):
	# 		dicio[temp[0]].append(temp[i])

	# f.close()

	# Try to assign places multiple times, until it works
	while True:
		places_aux = places.copy()
		people_aux = people.copy()
		dicio_remove.clear()
		i = 0

		# Try to assign by luck
		while i != size_mandala:
			number_left = len(places_aux)
			#print(f"i:{i} PP: {len(people_aux)} {len(places_aux)} {len(people)} {len(places)}")
			num = rd.randrange(0, number_left) #Iterate through places 
			to_clean = places_aux[num] #Place to clean
			person = get_place(to_clean)
			if person == "Error":
				#print("\nFound Error\n")
				break

			i += 1

		# Success
		if i == size_mandala:
			break
	
	# Print output
	history.write(f"Semana {week} - {today.strftime('%d/%m')}\n\n")

	unique_places = list(set(places))
	for place in unique_places:
		history.write(f"{place}\n")
		for person in dicio_remove:
			if place == dicio_remove[person]:
				history.write(f"\t{person}\n")
				# history.write(f"{person} - {dicio_remove[person]}\n")
		history.write("\n")
	history.write("\n\n\n")

	today = today + datetime.timedelta(days=7)

	# Update dicio removing current done chore
	for person in dicio_remove:
		# print(f"{person} - {dicio_remove[person]}")
		dicio[person].remove(dicio_remove[person])

	# Update PeopleAndPlaces
	# f = open("PeopleAndPlaces.txt", "w")
	# for person in dicio:
	# 	f.write(person)
	# 	for place in dicio[person]:
	# 		f.write(f", {place}")
	# 	f.write("\n")
	# f.close()

history.close()