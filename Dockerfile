FROM python:3.9-slim

WORKDIR /docs

RUN pip install sphinxcontrib-confluencebuilder

CMD ["sphinx-build", "-b", "confluence", ".", "build/confluence", "-E", "-a"]