# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /src/

# Copy the current directory contents into the container at /src/
COPY . /src
COPY environment.yml /src/

# Install any needed packages specified in requirements.txt
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "RC_Coursework", "/bin/bash", "-c"]

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV RC_Coursework=value
