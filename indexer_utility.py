# Regular expressions
re_not_alphanum = re.compile('\W+')
re_words = re.compile('\s+')

# Substitutes every non alphanumeric symbol with an empty string
def filter_alphanum(text):
	return re_not_alphanum.sub('', text)

# Splits text in words
def text2words(text):
	return re_words.split(text)

# Eliminates empty strings
def del_empty_strings(ls):
	return list(filter(lambda x: x != '', ls))
