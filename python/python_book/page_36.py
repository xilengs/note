# 3.4 & 3.5 & 3.6 & 3.7
guests = ['Bob', 'Alice', 'Jack']
for guest in guests:
    print(f"Hello {guest}, I'd like to invite you to have dinner together!")

absent = guests.pop(1)
print(f"{absent} has no time to come, so I invite another friend!")

guests.append('Coco')
for guest in guests:
    print(f"Hello {guest}, I'd like to invite you to have dinner together!")

print("I have found a bigger dining table, so I can invite more my friends to have dinner with me.")

guests.insert(0, 'Judy')
guests.insert(2, 'Danni')
guests.append('Frank')

for guest in guests:
    print(f"Hello {guest}, I'd like to invite you to have dinner together!")

print("The table that I bought just now can't be delivered to me in time, so I can just invite two of my friends to have dinner with me!")

while len(guests) > 2:
    print(f"I'm sorry, {guests.pop()}, because my new table can't be delivered in time, I can't invite you to have dinner!")

for guest in guests:
    print(f"Hello {guest}, don't worry, you are still in the list, you can come and have dinner with me tonight!")

while guests:
    del guests[0]
print(guests)
