ARG PYTHON_VERSION=3.13-slim

ARG PROJECT_DIR=/opt/furniture_store
ARG PROJECT_USER=django_user
ARG USER_ID=5000
ARG PROJECT_GROUP=django_group
ARG GROUP_ID=5000

FROM python:${PYTHON_VERSION} AS builder

ARG PROJECT_DIR

RUN mkdir ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip and install dependencies
RUN pip install --upgrade pip 

COPY requirements.txt ${PROJECT_DIR}/
RUN pip install --no-cache-dir -r requirements.txt
 
# Stage 2: Production stage
FROM python:${PYTHON_VERSION}

ARG PROJECT_DIR
ARG PROJECT_USER
ARG USER_ID
ARG PROJECT_GROUP
ARG GROUP_ID
 
RUN groupadd --gid ${GROUP_ID} ${PROJECT_GROUP} && \
    useradd -r ${PROJECT_USER} --uid ${USER_ID} --gid ${GROUP_ID} && \
    mkdir ${PROJECT_DIR} && \
    chown -R ${PROJECT_USER}:${PROJECT_GROUP} ${PROJECT_DIR}
 
# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
 
# Set the working directory
WORKDIR ${PROJECT_DIR}
 
# Copy application code
COPY --chown=${PROJECT_USER}:${PROJECT_GROUP} . ${PROJECT_DIR}
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Switch to non-root user
USER ${PROJECT_USER}
 
# Expose the application port
EXPOSE 8000 
 
# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "core.wsgi:application"]