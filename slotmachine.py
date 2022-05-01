import random

class SlotMachine:
  def __init__(self, reelNum, winDict):
    self.reels = [[i for i in range(10)]] * reelNum
    self.wins = winDict

  # Spin; currently based on a random selection from each reel.
  def spin(self):
    spinResult = ''
    for reel in self.reels:
      spinResult += str(random.choice(reel))
    return spinResult

  # Simulates profitability and return to player in a given number of spins/average bet.
  def simulation(self, spinCount, potAmt, betAmt):
    self.spinCount, self.potAmt, self.betAmt = spinCount, potAmt, betAmt
    jackpots = 0
    startingPot = potAmt
    totalPaid = 0
    winningSpins = 0

    for i in range(self.spinCount):
      potAmt += betAmt
      currSpin = self.spin()
      hits = [item for item in self.wins.keys() if item in currSpin]
      if hits:
        multiplier = self.wins[max(hits)]
        payout = (betAmt * multiplier)
        potAmt -= payout
        totalPaid += payout
        winningSpins += 1
        if multiplier == self.wins[max(self.wins.keys())]:
          jackpots += 1

    # Calculations and return statements in various profitability scenarios
    returnToPlayer = float(f"{totalPaid / (betAmt * spinCount)}")
    profit = potAmt - startingPot

    if totalPaid == 0:
      profit = f"${float(profit):,.2f}"
      return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}. RTP: 0.0"
    if profit > 0:
      profit = f"${float(profit):,.2f}"
      return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}.  RTP: {returnToPlayer:.2f}"
    elif profit < 0:
      profit = f"${float(profit):,.2f}"
      profit = str(profit).replace("-", "-$")
      return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}. RTP: {returnToPlayer:.2f}"
    else:
      return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}. RTP: {returnToPlayer:.2f}"
