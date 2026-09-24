gekocht_aantal = int(input())
prijs = float(input())
barcodes_nodig = int(input())
mijl_per_coupon = int(input())

aantal_coupons = gekocht_aantal // barcodes_nodig
aantal_mijl = aantal_coupons * mijl_per_coupon

print(f'Phillips spendeerde ${gekocht_aantal * prijs} voor {aantal_mijl} frequent flyer mijlen.')