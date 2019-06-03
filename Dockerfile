FROM python:3.7
ADD omdb_cli.py /omdb_cli.py
RUN pip install requests
RUN chmod 777 /omdb_cli.py
CMD [ "python", "/omdb_cli.py","batman" ]

