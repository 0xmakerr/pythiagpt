FROM ubuntu:22.04
WORKDIR /app
RUN apt update && apt install -y python3 python3-pip
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "-u", "main.py"]