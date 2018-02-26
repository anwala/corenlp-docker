FROM openjdk

LABEL maintainer="Alexander Nwala <anwala@cs.odu.edu>"

RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip \
    && unzip stanford-corenlp-full-2017-06-09.zip \
    && cd stanford-corenlp-full-2017-06-09

WORKDIR stanford-corenlp-full-2017-06-09

RUN export CLASSPATH="`find . -name '*.jar'`"

CMD java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000