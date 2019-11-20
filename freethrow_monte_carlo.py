import numpy as np
import matplotlib.pyplot as plt
import random
import pdb

'''
 Monte Carlo simulation of the following problem:
  If you make x% of your free throws in basketball, and you take y shots in a row, what's
  the most likely maximum streak?
 I'd like to get a closed-form answer, but I can't figure out how to go about it, so this
 is a first pass.
'''

# returns a boolean of made / not made
# perc (float) : likelihood of making the shot
def run_random_event(perc):
	return perc > random.random()

# runs a set of random events
# n_events (int) : number of events
# perc (float) : percentage of each event happening
def run_set_for_streak(n_events, perc):
	longest_streak = 0
	current_streak = 0
	for i in range(n_events):
		happened = run_random_event(perc)
		if happened:
			current_streak += 1
			longest_streak = max(current_streak, longest_streak)
		else:
			current_streak = 0
	return longest_streak

def mean(data):
	return float(sum(data))/len(data)

if __name__ == '__main__':
	set_size = 2000
	events_per_set = 5000
	perc = .79
	data = []
	for i in range(set_size):
		data.append(run_set_for_streak(events_per_set, perc))

	print('min:\t{}'.format(min(data)))
	print('mean:\t{}'.format(mean(data)))
	print('max:\t{}'.format(max(data)))
	#plt.hist(data)
	#plt.show()
	#pdb.set_trace()





