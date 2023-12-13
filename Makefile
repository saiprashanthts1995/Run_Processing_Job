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
	docker build -t forecast-img .

testimage:
	docker run -it forecast-img

push-to-ecr:
	aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 674125467617.dkr.ecr.us-west-2.amazonaws.com
	docker tag forecast-img:latest 674125467617.dkr.ecr.us-west-2.amazonaws.com/sagemaker-img-repo:latest
	docker push 674125467617.dkr.ecr.us-west-2.amazonaws.com/sagemaker-img-repo:latest
