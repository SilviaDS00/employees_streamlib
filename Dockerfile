FROM python:3.8
RUN pip install streamlit matplotlib pandas
COPY src/* /app/
COPY data/* /app/data/employees.csv
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]