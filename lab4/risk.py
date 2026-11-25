import random, statistics as st
TOKEN = '310f6e15b051ef25'
random.seed(int(TOKEN[:8], 16))
TRIALS, P_ANNUAL = 100_000, 0.15
LOW, MODE, HIGH = 5_000, 20_000, 90_000

losses = [random.triangular(LOW, HIGH, MODE) if random.random() < P_ANNUAL else 0.0
          for _ in range(TRIALS)]
losses.sort()
loss_years = [x for x in losses if x > 0]

print('token:', TOKEN, ' seed:', int(TOKEN[:8], 16))
print(f'trials {TRIALS}, loss years {len(loss_years)} '
      f'({100 * len(loss_years) / TRIALS:.1f} percent)')
print(f'mean annual loss       ${st.mean(losses):,.0f}')
print(f'median annual loss     ${st.median(losses):,.0f}')
print(f'p90 of all years       ${losses[int(0.90 * TRIALS)]:,.0f}')
print(f'p90 of loss years only ${loss_years[int(0.90 * len(loss_years))]:,.0f}')
print('loss exceedance')
for x in (0, 10_000, 25_000, 50_000, 75_000):
    p = sum(1 for v in losses if v > x) / TRIALS
    print(f'  P(annual loss > ${x:>7,}) = {p:6.3f}')
