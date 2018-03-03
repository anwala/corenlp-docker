import json	
import os, sys
from subprocess import check_output

#iso8601Date: YYYY-MM-DDTHH:MM:SS
def nlpGetEntities(text, host='localhost', iso8601Date='', labelLst=['PERSON','LOCATION','ORGANIZATION','DATE','MONEY','PERCENT','TIME']):
	
	'''
		This function annontates text with named entity labels

		@param text: text to label
		@param host: server host
		@param iso8601Date: reference date for SUTime (https://nlp.stanford.edu/software/sutime.html)
		@param labelLst: candidate list of entity labels for annotation
		
		returns: list of 2d list of entity/label tuples, e.g, [ ['John Doe', 'PERSON], ['1980', 'DATE] ]
    '''

	labelLst = set(labelLst)
	iso8601Date = iso8601Date.strip()
	if( len(iso8601Date) != 0 ):
		iso8601Date = ',"date":"' + iso8601Date + '"'

	request = host + ':9000/?properties={"annotators":"entitymentions","outputFormat":"json"' + iso8601Date + '}'
	entities = []
	dedupSet = set()

	try:
		output = check_output(['wget', '-q', '-O', '-', '--post-data', text, request])
		parsed = json.loads(output.decode('utf-8'))

		if( 'sentences' not in parsed ):
			return []

		for sent in parsed['sentences']:
			
			if( 'entitymentions' not in sent ):
				continue

			for entity in sent['entitymentions']:

				#text is entity, ner is entity class
				dedupKey = entity['text'] + entity['ner']
				
				if( dedupKey in dedupSet or entity['ner'] not in labelLst ):
					continue

				if( len(entity['text']) != 0 ):
					entities.append( [entity['text'], entity['ner']] )
					dedupSet.add(dedupKey)
	except:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorMessage = fname + ', ' + str(exc_tb.tb_lineno)  + ', ' + str(sys.exc_info())
		print('\tERROR:', errorMessage)

	return entities

text = 'CNN was founded in 1980 and was the first news company to deliver 24-hour news in America. Most of the early afternoon and late morning news was shown on CNN Newsroom that also shared Legal Views on certain matters.'
print( nlpGetEntities(text) )

