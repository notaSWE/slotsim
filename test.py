import random

columns = [[0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9],
  [0,1,2,3,4,5,6,7,8,9]]

# Key, value = roll, bet multiplier
wins = {
  '7': 2,
  '77': 7,
  '777': 30,
  '7777': 500
}

def spin():
  spinResult = ''
  for i in range(len(columns)):
    spinResult += str(random.choice(columns[i]))
  return spinResult

spinCount = 10
gamesToPlay = 10000
mostJackpots = 0
potAmt = 20000
totalPlayerRtp = 0
totalProfit = 0

# Game simulation
for i in range(gamesToPlay):
  jackpots = 0
  startingPot = potAmt
  totalPaid = 0
  winningSpins = 0

  for i in range(spinCount):
    bet = 2
    potAmt += bet
    currSpin = spin()
    hits = [item for item in wins.keys() if item in currSpin]
    if hits:
      multiplier = wins[max(hits)]
      payout = (bet * multiplier)
      potAmt -= payout
      totalPaid += payout
      winningSpins += 1
      if multiplier == wins[max(wins.keys())]:
        jackpots += 1
  gameProfit = float(f"{(potAmt - startingPot):.2f}")
  totalProfit += gameProfit
  playerRtp = totalPaid / (bet * spinCount)
  totalPlayerRtp += playerRtp
  # Per game stats
  # print(f"{winningSpins} wins/{spinCount} spins.  Paid out {totalPaid:.2f}.  Player result: {totalPaid - (bet * spinCount)} RTP: {playerRtp}")
  # print(f"Start pot was {(startingPot - bet):.2f}.  Remaining pot is {potAmt:.2f}.  Profit of {gameProfit}.")
  if jackpots > mostJackpots:
    mostJackpots = jackpots

# Per simulation stats
print(f"Average return to player: {(totalPlayerRtp / gamesToPlay):.2f}")
print(f"Jackpots hit: {mostJackpots}")
print(f"Profit after {gamesToPlay * spinCount} spins: ${totalProfit:,.2f}")
