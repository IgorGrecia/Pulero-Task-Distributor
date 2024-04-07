f = open("PeopleAndPlaces - Backup.txt", "r")
f2 = open("PeopleAndPlaces.txt", "w")
for line in f:
	f2.write(line)
f.close()
f2.close()