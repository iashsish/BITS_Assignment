# BITS_Assignment

1 Build the Docker image:

#Navigate to the directory containing your Dockerfile and run the following command:
docker build -t linear-regression-pytorch .

#Run the Docker container:
docker run -it --rm linear-regression-pytorch


#To push a Docker image to AWS Elastic Container Service (ECS), you need to follow these steps:

#Step 1: Create an ECR Repository
(e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com/linear-regression-pytorch).

I create a script "aws.sh" for push docker into AWS ECS


