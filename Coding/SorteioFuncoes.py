import random as rd
import os
import datetime


def get_place(places_aux, people_aux, to_clean, dicio):
	for item in people_aux:
		num = rd.randint(0,len(people_aux))
		person = people_aux[num-1]
		if to_clean in dicio[person]:
			dicio_remove[person] = to_clean
			places_aux.remove(to_clean)
			people_aux.remove(person)
			return person
	return "Error"

today = datetime.datetime.today()
history = open(f"Tasks/Tasks Limpeza Pulero {today.strftime('%d-%m')}.txt", "w")
filename = "ResetPeopleAndPlaces.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

for week in range(0,14):

	people = ["Cabeca", "Cafe", "Bordel", "Filhinho", "Jucelio", "Marcola", "Tietz", "Moises", "Penado", "Tesouro", "Desisto", "P2", "P1", "Teresa"]
	places = ["Sala + Corredor Frente", "Sala Antiga + Lavabo + Corredor Quartos", "Sala Antiga + Lavabo + Corredor Quartos", "Banheiro Meio", "Banheiro Suite", "Fundo", "Fundo", "Fundo", "Garagem + Frente", "Garagem + Frente", "Salol + Cozinha", "Salol + Cozinha", "Lavanderia + Banheiro Fundo", "Lavanderia + Banheiro Fundo"]

	dicio = {}
	dicio_remove = {}
	reset = 0

	f = open("PeopleAndPlaces.txt", "r")
	for line in f:
		temp = line.strip().split(", ")
		size = len(temp)
		if size == 1:
			print("==================================================================")
			print("\nChegamos ao fim da 14ª semana, logo foi feito o reset dos cômodos.\n")
			print("==================================================================\n")
			filename = "ResetPeopleAndPlaces.py"
			with open(filename, "rb") as source_file:
			    code = compile(source_file.read(), filename, "exec")
			exec(code)
			dicio.clear()
			reset = 1
			break
		dicio[temp[0]] = []
		for i in range(1,size):
			dicio[temp[0]].append(temp[i])
	f.close()

	if reset == 1:
		f = open("PeopleAndPlaces.txt", "r")
		for line in f:
			temp = line.strip().split(", ")
			size = len(temp)
			dicio[temp[0]] = []
			for i in range(1,size):
				dicio[temp[0]].append(temp[i])
		f.close()

	while True:
		places_aux = places.copy()
		people_aux = people.copy()
		dicio_remove.clear()
		size_people = len(people_aux)
		i = 0

		while i != size_people:
			size_places = len(places_aux)
			num = rd.randint(0,size_places)
			to_clean = places_aux[num-1]
			person = get_place(places_aux, people_aux, to_clean, dicio)
			if person == "Error":
				# print("\nFound Error\n")
				break
			i += 1

		if i == size_people:
			break
	
	history.write(f"Semana {week+1} - {today.strftime('%d-%m')}\n\n")

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


	for person in dicio_remove:
		# print(f"{person} - {dicio_remove[person]}")
		dicio[person].remove(dicio_remove[person])

	f = open("PeopleAndPlaces.txt", "w")
	for person in dicio:
		f.write(person)
		for place in dicio[person]:
			f.write(f", {place}")
		f.write("\n")
	f.close()

history.close()