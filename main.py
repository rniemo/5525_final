

# global recipe map. contains all recipes downloaded in the form {link -> (recipe_title, comment_list)}
# where comment_list is a list of the form [(comment, #likes), (comment2, #likes2), ...]
recipe_map = {}
# map from cuisine -> map from {recipe_link -> (recipe_title, commenet_list)}
cuisine_map = {}

#result data
# list of tuples (recipe_link, recipe_title, score, #comments, [cuisine1, cuisine2, ...])
results = []

def read_data():
	# go through data/ folder
	# for each folder (each named a cuisine):
		# for each file in folder:
			# recipe_link = get_link(file)
			# if recipe_map has_key recipe_link:
				# result = (recipe_link, recipe_map[recipe_link])
			#else:
				# result = read_recipe(file) // return (recipe_link, (recipe_title, comment_list))
				# add result to recipe_map
			# add result to cuisine_map
	pass

def get_link(file):
	# read first link of file and return the link
	pass

def read_recipe(file):
	# open file, read link
	# comment_list = []
	# while(not eof):
		# read until comment_separator
		# read until like_separator
		# add to comment_list
	#return (recipe_link, comment_list)
	pass

def train_model():
	# train naive bayes using NaiveByaes.py
	pass


# generate predicted scores for sentiment for each comment on each recipe
def generate_results():
	# for each cuisine in cuisine map:
		# for each recipe_link
			#### add in averaging score without num_likes?
			# num_likes = 0
			# total_score = 0
			# for each (comment, #likes) pair in comment_list:
				# total_score += #likes * model.Predict(comment)
				# num_likes += #likes
			# score = total_score / num_likes
			# add to results list
	pass

# figure out the 10 most liked / least hated recipes, most liked / hated cuisine.
# be careful w/ sample size in cuisine. E.g. there are only 3 Egyptian recipes.
def process_results():
	pass