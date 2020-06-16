import math
import pickle

def frequency_unigram(words):
	findic = {}
	for i in range(len(words)):
		if words[i] not in findic:
			findic[words[i]]=0
		findic[words[i]]+=1
	return findic

def frequency_bigram_part2(words):
	findic = {}
	for i in range(len(words)-1):
		if (words[i],words[i+1]) not in findic:
			findic[(words[i],words[i+1])]=0
		findic[(words[i],words[i+1])]+=1
	return findic

def get_prob_dic(dicty,tags_unique):
	findic = {}
	total = 0
	for k,v in dicty.iteritems():
		total+=v
	for k,v in dicty.iteritems():
		findic[k] = math.log((v+1)/((total*1.0)+len(tags_unique)))
	for i in range(len(tags_unique)):
		if tags_unique[i] not in findic:
			findic[tags_unique[i]] = math.log((1)/((total*1.0)+len(tags_unique)))
	return findic

def Viterbit(obs, states, s_pro, t_pro, e_pro):
	# path = { s:[] for s in states} # init path: path[s] represents the path ends with s

	# Initializing step
	curr_pro = {}
	path = {}
	last_flag = 0
	for s in states:
		first_obs = obs[0]
		state_val = s
		emmi_prob = e_pro[first_obs][state_val]
		start_prob = s_pro[s]
		path[s] = []
		curr_pro[s] = start_prob+emmi_prob

	# Recurssion Step
	total_state_counts=0
	for i in xrange(1, len(obs)):
		last_pro = curr_pro
		curr_pro = {}
		for curr_state in states:
			max_pro = -999999999
			last_sta = -1
			for last_state in states:
				last_state_prob = last_pro[last_state] # last stage probability
				transition_prob = t_pro[last_state][curr_state] # transition probability
				emmision_prob = e_pro[obs[i]][curr_state] # emission probability
				tempmax = last_state_prob+transition_prob+emmision_prob # log probabilities are added
				if tempmax>max_pro:
					max_pro = tempmax
					last_sta = last_state
			# max_pro, last_sta = max(((last_pro[last_state]*t_pro[last_state][curr_state]*e_pro[obs[i]][curr_state], last_state) for last_state in states))
			curr_pro[curr_state] = max_pro
			total_state_counts+=1
			path[curr_state].append(last_sta) # storing the path for backtra