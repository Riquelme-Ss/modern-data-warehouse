FROM apache/spark:3.5.6

USER root

# Hadoop AWS / S3A
RUN curl -fL \
    -o /opt/spark/jars/hadoop-aws-3.3.4.jar \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar

RUN curl -fL \
    -o /opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar \
    https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

# PostgreSQL JDBC
RUN curl -fL \
    -o /opt/spark/jars/postgresql-42.7.7.jar \
    https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.7/postgresql-42.7.7.jar

RUN chown spark:spark \
    /opt/spark/jars/hadoop-aws-3.3.4.jar \
    /opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar \
    /opt/spark/jars/postgresql-42.7.7.jar