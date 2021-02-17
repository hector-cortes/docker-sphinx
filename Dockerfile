FROM python:3.9-slim

ADD conf.py /docs/conf.py

WORKDIR /docs

RUN pip install sphinxcontrib-confluencebuilder

CMD ["sphinx-build", "-b", "confluence", ".", "build/confluence", "-E", "-a"]