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

# Run app.py when the container launches
CMD ["python", "src/webapp/app.py"]

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make sure the script is executable
RUN chmod +x entrypoint.sh

# Use the entrypoint script to start the container
ENTRYPOINT ["/entrypoint.sh"]
