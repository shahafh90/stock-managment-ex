FROM python:3
ADD src code
RUN pip install flask
RUN pip install pymongo
CMD [ "python", "/code/app.py" ]
