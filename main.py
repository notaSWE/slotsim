from slotmachine import SlotMachine

# Sample simulations
slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})
slot2 = SlotMachine(4, {
  '7': 1,
  '77': 10,
  '777': 150,
  '7777': 1000
  })

print(slot1.simulation(100000, 20000, 2))
print(slot2.simulation(1000000, 20000, 2))
