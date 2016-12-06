import random

def open_file(n):
	f = open("cs170_final_inputs/"+str(n)+".in", "r")
	size = f.readline()
	g = []
	e = {}
	for i in range(int(size)):
		g.append([])
		cur = f.readline()
		x = [int(i) for i in cur.split()]
		g[i] = x
	for j in range(int(size)):
		e[j] = []
		for k in range(int(size)):
			if(g[j][k] == 1):
				e[j].append(k)
	return g, e

def horse(g, e):
	size = len(g)
	results = []
	for i in range(500):
		teams = []
		curr = random.randint(0, size-1)
		curr_team = []
		seen = []
		while (len(seen) != size):
			seen.append(curr)
			curr_team.append(curr)
			if(len(curr_team) == size):
				teams.append(curr_team)
				break
			neighbors = e[curr]
			not_seen = [x for x in neighbors if x not in seen]
			if(len(seen) == size):
				teams.append(curr_team)
			elif (len(not_seen) == 0):
				teams.append(curr_team)
				curr_team = []
				not_seen = [x for x in range(0, size) if x not in seen]
				curr = not_seen[random.randint(0, (len(not_seen)-1))]
			else:
				curr = not_seen[random.randint(0, (len(not_seen)-1))]

		if(len(curr_team) == size):
			results.append(teams)
			break
		else:		
			results.append(teams)

	best_score = -1

	for r in results:
		score = calculate_score(r, g)
		if(score > best_score):
			best_score = score
			best_lst = r
	print(best_lst)
	for b in range(len(best_lst)):
		best_lst[b] = ' '.join(map(str,best_lst[b]))

	return ("; ".join(best_lst), best_score)

def calculate_score(lst, g):
	total = 0
	for l in lst:
		total += (len(l) * sum_list(l, g))
	return total

def sum_list(lst, g):
	total = 0
	for l in lst:
		total += g[l][l]
	return total

def main():
	f = open('output300.out','w')
	for i in range(200, 300):
		g, e = open_file(i+1)
		best = horse(g,e)
		print("score: " + str(best[1]))
		f.write(best[0] + "\n")
		
main()

# g, e = open_file(1)
# print(horse(g, e))