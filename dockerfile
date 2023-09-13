FROM python:3.8-alpine

COPY . ./prac_lucap
WORKDIR /prac_lucap

RUN pip install -r requirements.txt
EXPOSE 5005
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]