FROM python:3

ADD app.py requirements.txt ./

#Install python env
ENV VIRTUAL_ENV=.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install flask

#prepare flask
ENV FLASK_APP app
ENV FLASK_DEBUG 1 

#flask entry points
ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=9000"]