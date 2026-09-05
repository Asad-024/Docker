FROM alpine/java:22.0.2-jdk

WORKDIR /app

COPY . .

RUN javac src/Main.java

CMD ["java","-cp","src","Main"]
