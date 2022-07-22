FROM python
RUN pip3 install boto3
RUN pip3 install biopython
RUN mkdir /src
COPY index.py /src 
CMD ["python", "/src/index.py"]
