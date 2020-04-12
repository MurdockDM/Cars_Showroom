showroom = set()
favoriteCars=("aventador", "model s", "model 3", "p1")
showroom.update(favoriteCars)
print(len(showroom))
duplicateModel = ("model s",)
showroom.update(duplicateModel)
print(showroom)

twoMoreCars = ("R8", "model y")
showroom.update(twoMoreCars)
showroom.discard("p1")

junkyard = {'miata', 'focus', 'aventador', 'model s'}

print(junkyard.intersection(showroom))

showroomAndJunkyard = showroom.union(junkyard)
print(showroomAndJunkyard)

showroomAndJunkyard.discard("focus")
showroomAndJunkyard.discard("miata")
print(showroomAndJunkyard)