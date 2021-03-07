FROM python:3.8

ENV PATH="$PATH:/root/.local/bin"

# streamlit-specific commands
RUN mkdir -p /home/karandeep/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /home/karandeep/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /home/karandeep/.streamlit/config.toml'

# remember to expose the port your app'll be exposed on.
EXPOSE 8080

RUN python3 -m pip install --upgrade pip 

COPY requirements.txt app/requirements.txt
RUN pip3 install --user -r app/requirements.txt && python3 -m spacy download en 

# copy into a directory of its own (so it isn't in the toplevel dir)
COPY . /app
WORKDIR /app

# run it!
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
