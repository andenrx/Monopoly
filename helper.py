# This file just contains some helper functions that the notebook uses
import numpy as np
from matplotlib import pyplot

# List of Space names
SPACES = [
  'Go',
  'Mediterranean Avenue',
  'Community Chest',
  'Baltic Avenue',
  'Income Tax',
  'Reading Railroad',
  'Oriental Avenue',
  'Chance',
  'Vermont Avenue',
  'Connecticut Avenue',
  'Just Visiting',
  'St. Charles Place',
  'Electric Company',
  'States Avenue',
  'Virginia Avenue',
  'Pennsylvania Railroad',
  'St. James Place',
  'Community Chest',
  'Tennessee Avenue',
  'New York Avenue',
  'Free Parking',
  'Kentucky Avenue',
  'Chance',
  'Indiana Avenue',
  'Illinois Avenue',
  'B&O Railroad',
  'Atlantic Avenue',
  'Ventnor Avenue',
  'Water Works',
  'Marvin Gardens',
  'Go to Jail',
  'Pacific Avenue',
  'North Carolina Avenue',
  'Community Chest',
  'Pennsylvania Avenue',
  'Short Line',
  'Chance',
  'Park Place',
  'Luxury Tax',
  'Boardwalk',
  'Jail',
  'Jail',
]
SPACES = list(map(lambda s: f"{s[0]:2}. {s[1]}", enumerate(SPACES)))
assert len(SPACES) == 42

# Helper function for the "Advance to the nearest Railroad" card
def next_railroad(i: range(0,40)) -> {5, 15, 25, 35}:
  """Get the next railroad after space 'i'
  3  ->  5
  10 -> 15
  11 -> 15

  i       : The current space
  returns : The next railroad (ie 5, 15, 25, 35) after space i
            If i is a railroad, the next railroad after i
  """
  if i < 0 or 40 <= i:
    raise ValueError(f"Expected 0 <= i < 40, instead got {i}.")
  return (i + 1 + ((4-i) % 10)) % 40

# A few special spaces we need to watch out for
CHANCE = {7, 22, 36}
COMMUNITY_CHEST = {2, 17, 32}
GO_TO_JAIL = {30}

def format(matrix: np.ndarray(shape=(42, 1))) -> str:
  """Format a probability vector"""
  output = []
  for i, name, (p,) in zip(range(42), SPACES, matrix):
    if len(matrix.shape) != 2 or matrix.shape[1] != 1:
      raise ValueError(f"Expected matrix to be n x 1, instead found {matrix.shape}")
    output.append(f"{name:<26}:{abs(p) * 100:6.2f}%")
  return "\n".join(output)

# Helper function for plot
def plot_average_travel_time(A):
	pyplot.imshow(A, 'inferno', vmin=20, vmax=70)
	pyplot.colorbar()
	pyplot.ylabel('from')
	pyplot.xlabel('to')
	pyplot.title(f'Average Travelling Time')

# Helper function for plot
def plot_long_term_probability(v_inf):
	pyplot.plot(v_inf*100, 'k-')
	pyplot.ylabel('Probability (%)')
	pyplot.xlabel('Space')
	pyplot.title('Long Term Probability')
	pyplot.ylim(0)
