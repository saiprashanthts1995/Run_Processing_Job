# sudo yum install make
installdocker:
	sudo yum update -y
	sudo yum install docker -y
	sudo usermod -a -G docker ec2-user
	id ec2-user
	newgrp docker

start-docker:
	sudo systemctl enable docker.service
	sudo systemctl start docker.service

buildimg:
	docker build -t test-sai-img .

testimage:
	docker run -it test-sai-img

push-to-ecr:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 801355498549.dkr.ecr.us-east-1.amazonaws.com
	docker tag test-sai-img:latest 801355498549.dkr.ecr.us-east-1.amazonaws.com/test_sai_ecr:latest
	docker push 801355498549.dkr.ecr.us-east-1.amazonaws.com/test_sai_ecr:latest
