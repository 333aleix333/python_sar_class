# Regular expressions
re_not_alphanum = re.compile('\W+')
re_words = re.compile('\s+')

def filter_alphanum(text):
	'''Substitutes every non alphanumeric symbol with an empty string

        :param String text: Text to filter

        :returns: The filtered text
        :rtype: String
        '''
	return re_not_alphanum.sub('', text)

def text2words(text):
	'''Splits text in words
	
        :param String text: Text to split

        :returns: The splitted text
        :rtype: List
        '''
	return re_words.split(text)

def del_empty_strings(ls):
	'''Eliminates empty strings
	
        :param List ls: List to eliminate the empty string from
        :returns: List without the empty string
        :rtype: List
        '''
	return list(filter(lambda x: x != '', ls))
