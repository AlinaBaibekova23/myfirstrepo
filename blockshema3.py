people = {"Alīna": 27, "Maria": 19, "Evnika": 23}
for person in people:
    print(".....")
    print(person)  #tikeu klāt vārdam
    print(people[person])  #tieku klāt vecumam

    if people[person] >= 18:
        print(f"{person} ir pilngadīgs(-a)")
    else:
        print(f"{person} nav pilngadīgs(-a)")
