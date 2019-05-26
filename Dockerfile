FROM debian:latest

RUN apt-get update && apt-get install -y nasm gdb gcc python3
