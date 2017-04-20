import os
import pprint

DATA_DIRECTORY = "data"
COMMENT_SEPARATOR = '=*=COMMENT_SEPARATOR=*='
LIKE_SEPARATOR = '=*=LIKE_SEPARATOR=*='

# global recipe map. contains all recipes downloaded in the form {link -> (recipe_title, comment_list)}
# where comment_list is a list of the form [(comment, #likes), (comment2, #likes2), ...]
recipe_map = {}
# map from cuisine -> map from {recipe_link -> (recipe_title, comment_list)}
cuisine_map = {}

#result data
# list of tuples (recipe_link, recipe_title, score, # of comments, [cuisine1, cuisine2, ...])
results = []

def read_data():
    for directory, subdirectories, file_names in os.walk(DATA_DIRECTORY):
        for recipe_name in file_names:
            cuisine = directory.split('/')[1]
            recipe_link = get_link(directory, recipe_name)
            if recipe_link in recipe_map:
                result = recipe_map[recipe_link]
            else:
                result = read_recipe(directory, recipe_name)
                recipe_map[recipe_link] = read_recipe(directory, recipe_name)
            cuisine_map[cuisine] = result

def get_link(directory, recipe_name):
    with open(os.path.join(directory, recipe_name)) as file:
        return file.readline().strip()

def read_recipe(directory, recipe_name):
    with open(os.path.join(directory, recipe_name)) as file:
        lines = list(file)
        content = ''.join(lines[1:]).replace('\n', '')
        comment_list = []
        fragments = content.split(COMMENT_SEPARATOR)
        for fragment in fragments:
            comment_and_like = fragment.split(LIKE_SEPARATOR)
            if comment_and_like != ['']:
                comment_and_like[1] = int(comment_and_like[1])
                comment_list.append(tuple(comment_and_like))

        return (recipe_name, comment_list)

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
                # // note: #likes can be 0. laplace smoothing?
                # total_score += #likes * model.Predict(comment)
                # num_likes += #likes
            # score = total_score / num_likes
            # add to results list
    pass

# figure out the 10 most liked / least hated recipes, most liked / hated cuisine.
# be careful w/ sample size in cuisine. E.g. there are only 3 Egyptian recipes.
def process_results():
    pass

read_data()
print "Recipe Map ------\n", pprint.pprint(recipe_map)
print "Cuisine Map ------\n", pprint.pprint(cuisine_map)