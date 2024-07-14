import random as rd
import os
import datetime

# Try to assing a person to to_clean place
def get_place(to_clean):
	for i in range(len(people_aux)):
		#print(f"{i}")
		num = rd.randrange(0,len(people_aux))
		person = people_aux[num]
		if to_clean in dicio[person]:
			dicio_remove[person] = to_clean
			places_aux.remove(to_clean)
			people_aux.remove(person)
			return
	raise Exception()

people = ["Cabeca", "Cafe", "Bordel", "Xupeta", "Moises", "Tesouro", "Desisto", "Tampinha", "P4", "Castro"]
places = ["Sala + Corredor Frente", "Lavabo + Corredor Quartos", "Banheiro Meio", "Banheiro Suite", "Fundo", "Garagem + Frente", "Garagem + Frente", "Salol + Sala Antiga", "Lavanderia + Banheiro Fundo + Cozinha", "Lavanderia + Banheiro Fundo + Cozinha"]
size_mandala = len(people)
dicio = {}

for person in people:
	dicio[person] = places.copy()

if len(places) != size_mandala:
	print("\nCorrige as listas hardcodadas corno\n")

if not os.path.exists('Tasks'):
    os.makedirs('Tasks')

today = datetime.datetime.today()
history = open(f"Tasks/Tasks Limpeza Pulero {today.strftime('%d-%m')}.txt", "w")

for week in range(0, size_mandala):
	dicio_remove = {}

	# Try to assign places multiple times, until it works
	while True:
		places_aux = places.copy()
		people_aux = people.copy()
		dicio_remove.clear()

		# Try to assign by luck
		try:
			for i in range(0,size_mandala):
				number_left = len(places_aux)
				num = rd.randrange(0, number_left) #Iterate through places 
				to_clean = places_aux[num] #Place to clean
				get_place(to_clean)

		except:
			pass

		else:
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

	# Update dicio removing current done chores
	for person in dicio_remove:
		# print(f"{person} - {dicio_remove[person]}")
		dicio[person].remove(dicio_remove[person])

history.close()