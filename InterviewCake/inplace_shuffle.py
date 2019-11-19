# Fisher-Yates shuffle (sometimes called the Knuth shuffle).
import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place
    last_index = len(the_list) - 1
    for first_index in range(0, last_index - 1):
        random_index = get_random(first_index + 1, last_index)
        the_list[first_index], the_list[random_index] = the_list[random_index],the_list[first_index] 

def out_of_place_shuffle(the_list):
	out = []
	while len(the_list) != 0:
		if len(the_list) - 2 <= 0:
			random_index = 0
		else:
			random_index = get_random(0, len(the_list) - 2)
		out.append(the_list[random_index])
		del the_list[random_index]
	return out

sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list
print out_of_place_shuffle(sample_list)
print sample_list