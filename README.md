# Processing Job DS

This project allows you to trigger processing jobs using an Amazon EC2 instance to build and push a Docker image to Amazon Elastic Container Registry (ECR).

## Introduction

The purpose of this project is to automate the triggering of processing jobs by building and pushing a Docker image to Amazon ECR using an Amazon EC2 instance. Processing jobs can then use this Docker image for data preprocessing, post-processing, or other tasks.

## Prerequisites

### EC2 Prerequisites

To set up the Amazon EC2 instance for building and pushing the Docker image, follow these prerequisites:

1. **Spin up an EC2 Instance:**
   - Launch an EC2 instance using the Amazon Linux AMI.
   - Ensure the instance has the necessary IAM permissions to interact with ECR and SageMaker. 

2. **Install 'make':**
   - Connect to your EC2 instance using SSH.
   - Run the following command to install 'make' functionality:

     ```bash
     sudo yum install make
     ```
Then we will leverage make functionality to create docker image and push the image to ecr. Then used lambda functionality to create processing job by referring to ECR image.

added

new1


squash
rebase
merge
update from main


pull vs fetch vs clone vs push

discard vs statsh

asdasd

asdsa

asas


asda
d


sadasd


sadsa


asd
asd

sa
as
