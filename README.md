# Dockerfile for [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) (Natural language software) Server v3.8.0

This Dockerfile builds a docker image for the Stanford CoreNLP Server and runs the server on the localhost (port 9000). The server provides access to the NLP suite:
* [Part-Of-Speech (POS) tagger](https://nlp.stanford.edu/software/tagger.html)
* [Named Entity Recognizer (NER)](http://nlp.stanford.edu/software/CRF-NER.html)
* [Parser](https://nlp.stanford.edu/software/lex-parser.html)
* [Sentiment analysis](https://nlp.stanford.edu/sentiment/)
* etc.

# Prerequisite
* [Docker](https://docs.docker.com/install/)

# Start server on localhost port 9000
`$ docker run --rm -d -p 9000:9000 --name stanfordcorenlp anwala/stanfordcorenlp`

# Use server from browser
Goto http://localhost:9000/ from your browser

# Use server from command line (NER Tagger)
`$ wget -q -O - --post-data 'The quick brown fox jumped over the lazy dog.' 'localhost:9000/?properties={"annotators":"entitymentions","outputFormat":"json"}'`
# Stop server
`docker rm -f stanfordcorenlp`