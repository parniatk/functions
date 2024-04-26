#(Conversions between feet and meters)
def foot_to_Meter(feet):
    meter = 0.305 * feet
    return meter

def meter_to_Feet (meter):
    feet = meter / 0.305
    return feet

metr_amount = [20.0 , 26.0 , 30.0 , 36.0 , 40.0 , 46.0 , 50.0 , 56.0 , 60.0 , 66.0 ]

foot_amount= []
for amount in metr_amount:
    foot_amount.append(meter_to_Feet(amount))

# table
print("Metr \t Foot")
for amount in range(len(metr_amount)):
    print(f"{metr_amount[amount]}\t {foot_amount[amount]}")

foot_amount = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

# 
metr_temp = []
for amount in foot_amount:
    metr_temp.append(foot_to_Meter(amount))

#table
print("\nFoot \t Meter")
for amount in range(len(foot_amount)):
    print(f"{foot_amount[amount]}\t{metr_amount[amount]}")