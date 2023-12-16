# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the environment.yml file
COPY environment.yml .

# Copy the data directory into the container
COPY data/ data/

# Copy the src directory contents into the container
COPY src/ src/

# Copy the docs directory contents into the container
COPY docs/ docs/

# Install any needed packages specified in requirements.txt
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "sudoku_env", "/bin/bash", "-c"]

# Build Sphinx Documentation
RUN sphinx-build -b html docs/source/ docs/build/

# The code to run when container is started
ENTRYPOINT ["conda", "run", "-n", "sudoku_env", "python", "src/solve_sudoku.py"]

# Make port 80 available to the world outside this container
EXPOSE 80
