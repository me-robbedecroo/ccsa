kist = 20
pallet = 35

a = int(input())

kisten = a // kist
palletten = kisten // pallet
rest_kisten = kisten % pallet
rest_appels = a % kist

print(palletten)
print(rest_kisten)
print(rest_appels)