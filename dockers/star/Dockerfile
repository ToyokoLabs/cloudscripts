FROM ubuntu:20.04
RUN apt-get update -y && apt-get install -y build-essential wget libz-dev
RUN wget https://github.com/alexdobin/STAR/archive/2.7.10a.tar.gz && \
    tar -xzf 2.7.10a.tar.gz && \
    cd STAR-2.7.10a/source && \
    make STAR
RUN rm 2.7.10a.tar.gz
