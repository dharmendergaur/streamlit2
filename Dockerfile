FROM almalinux:9.3-20240410

# Set the working alrectory
WORKDIR /app 

# Copy package. json and package-lock. json
COPY requirements.txt .

RUN  dnf update -y &&  dnf upgrade -y
RUN yum -y update && \
    yum -y install python3 && \
    python3 -m ensurepip
RUN pip3 install -r requirements.txt

# Copy project files and folders to the current working directory
COPY . .


#Run the vue application
RUN chmod +x start.sh

CMD ["./start.sh"]