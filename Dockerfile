FROM public.ecr.aws/lambda/python:3.10

# Install system dependencies
RUN yum install -y libstdc++ cmake gcc-c++ && \
    yum clean all && \
    rm -rf /var/cache/yum

# Copy requirements.txt
COPY lambda_requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY src/lambda_function.py ${LAMBDA_TASK_ROOT}

# Copy the model
COPY models/stack_reg.pkl ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r lambda_requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.predict" ]