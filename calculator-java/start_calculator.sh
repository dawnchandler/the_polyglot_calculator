#!/bin/ash

rm -fr /calculator-java/target/*
javac -cp /calculator-java/dependencies/commons-lang3-3.11.jar:/calculator-java/dependencies/amqp-client-5.9.0.jar:/calculator-java/dependencies/json-20200518.jar:/calculator-java/dependencies/json-simple-1.1.1.jar:/calculator-java/dependencies/slf4j-api-2.0.0-alpha1.jar:/calculator-java/src/ /calculator-java/src/CalculatorRPCServer.java -d /calculator-java/target/
java -cp /calculator-java/dependencies/commons-lang3-3.11.jar:/calculator-java/dependencies/amqp-client-5.9.0.jar:/calculator-java/dependencies/json-20200518.jar:/calculator-java/dependencies/json-simple-1.1.1.jar:/calculator-java/dependencies/slf4j-api-2.0.0-alpha1.jar:/calculator-java/target/  CalculatorRPCServer