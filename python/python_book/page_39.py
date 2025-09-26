# 3.8
from networkx.algorithms.operators.unary import reverse

trip = ['China', 'Japan', 'America', 'France', 'England']
print(trip)
print(sorted(trip))
print(trip)
print(sorted(trip, reverse=True))
print(trip)
print(trip.reverse())
print(trip.reverse())
print(trip.sort())
print(trip.sort(reverse=True))
