mylist = ["Lucas Bravo", "Sandra Gurgzdaityte", "John Carling", "Felix Smith",
          "Kevin Randle", "Pauline Hughes", "Thomas Jim", "Martin Trav", "Eveglina Gurgzdaityte"]


for i in range(len(mylist)):
    fullname = mylist[i].split()
    firstname_initial = fullname[0][0]
    lastname_initial = fullname[1][0]
    both_initial = firstname_initial + lastname_initial
    print(both_initial)