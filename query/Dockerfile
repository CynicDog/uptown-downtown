# Use official Apache Spark image with Hadoop
FROM apache/spark:3.5.1

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV DELTA_BASE_PATH=/delta
ENV PATH=$SPARK_HOME/bin:$PATH

# Create Delta directory volume
VOLUME ["/delta"]

# Copy entrypoint script
COPY scripts/run_thriftserver.sh /usr/local/bin/run_thriftserver.sh

USER root
RUN chmod +x /usr/local/bin/run_thriftserver.sh

# Expose Thrift server port
EXPOSE 10000

# Entrypoint to run Spark Thrift Server
ENTRYPOINT ["/usr/local/bin/run_thriftserver.sh"]