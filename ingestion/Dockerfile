# --------------------------------------------------------------------------
# STAGE 1: BUILD STAGE (Sets up Python dependencies and the virtual environment)
# --------------------------------------------------------------------------
FROM python:3.11-slim-bookworm AS build-python

# Set working directory
WORKDIR /app

# 1. Install uv for fast dependency management
RUN pip install uv

# 2. Copy all necessary files for the build: manifest, source code, and scripts
COPY pyproject.toml .
COPY src ./src
COPY scripts ./scripts

# 3. Create the virtual environment
RUN uv venv

# 4. Activate the new .venv and install ALL project dependencies and the editable project.
#    The correct command is 'uv pip install'.
RUN . .venv/bin/activate && uv pip install -e .


# --------------------------------------------------------------------------
# STAGE 2: FINAL RUNTIME STAGE (Adds the required Java/JDK and copies the Python setup)
# --------------------------------------------------------------------------
FROM eclipse-temurin:17-jdk-jammy AS runtime

# Set environment variables for Java and the Delta application
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$JAVA_HOME/bin:$PATH
ENV DELTA_BASE_PATH=/app/data/delta

# Set working directory
WORKDIR /app

# --- CRITICAL CHANGE: Copy the entire Python 3.11 installation ---
# This ensures that all shared libraries and the core Python interpreter
# required by the virtual environment are present.
COPY --from=build-python /usr/local/ /usr/local/
# ----------------------------------------------------------------

# Copy the source code and entry files (pyproject.toml, src, scripts)
# We copy these again just in case the /usr/local/ copy missed any project files
COPY --from=build-python /app/pyproject.toml /app/
COPY --from=build-python /app/src /app/src
COPY --from=build-python /app/scripts /app/scripts
COPY --from=build-python /app/.venv/ /app/.venv/

# Prepare Delta directories on the final file system
RUN mkdir -p $DELTA_BASE_PATH/warehouse \
    && mkdir -p $DELTA_BASE_PATH/mta_trip_updates_bronze

# Expose Spark UI port
EXPOSE 4040

# Entrypoint: Run the ingestion service using the interpreter inside the copied .venv
ENTRYPOINT ["/app/.venv/bin/python", "-m", "mta_ingestion.main"]