# Replace with your AWS account ID, region, and repository name
AWS_ACCOUNT_ID=123456789012
AWS_REGION=your-region
REPOSITORY_NAME=linear-regression-pytorch

# Authenticate Docker to your Amazon ECR registry
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Build the Docker image
docker build -t $REPOSITORY_NAME .

# Tag the Docker image
docker tag $REPOSITORY_NAME:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPOSITORY_NAME:latest

# Push the Docker image to ECR
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPOSITORY_NAME:latest
