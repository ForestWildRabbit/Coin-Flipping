## Coin-Flipping

### Info

There is a simulation of coin flips and bet value using Martingale (betting system).

> There is dependency of bet value and attempt number (up to 10 attempts).

![Bet value graph](/images/bet_value_graph.png)

### Parameters

- MAX_COIN_FLIPS_PER_SIMULATION = 100
    - How much coin flips will be simulated if current balance is positive.
- WINNING_MULTIPLIER = 1.9
    - Bet multiplier (e.g. if a bet is equal to $100, then in the case you win you'll get 100$ * 1.9 = $190)

### Simulation results

I run 100 simulations with initial_balance = 100_000, in each simulation balance was 100_000 / 100 = 1000.

If you do this many times, you'll see that you lose much more money than you win.

~$453 profit
![Delta positive](/images/delta_positive.png)

~$1327 loss
![Delta negative](/images/delta_negative.png)

In the long run, this is a losing strategy due to negative mathematical expectation and balance limit.

I suppose in real life this trick may be applied once, if you can afford 10x base bet increase.