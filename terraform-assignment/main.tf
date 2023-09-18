# Define the AWS provider and region
provider "aws" {
  region = "us-east-1"
}

# Create a VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.10.0.0/16"
}

# Create a public subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.10.0.0/24"
  availability_zone       = "us-east-1a"  # Specify the actual availability zone
  map_public_ip_on_launch = true
}

# Create a private subnet
resource "aws_subnet" "private_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.10.1.0/24"
  availability_zone       = "us-east-1a"  # Specify the same availability zone as the public subnet
}

# Create an EC2 instance in the public subnet
resource "aws_instance" "ec2_instance" {
  ami           = "i-9582549269"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  key_name      = "my-existing-key-pair"  # Replace with your key pair name

  root_block_device {
    volume_size = 8
    volume_type = "gp2"
  }


  tags = {
    Name    = "AssignmentInstance"
    purpose = "Assignment"
  }
}

# Create a security group
resource "aws_security_group" "ec2_security_group" {
  name        = "ec2-security-group"
  description = "Security group for EC2 instance"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "EC2SecurityGroup"
  }
}

# Attach the security group to the EC2 instance
resource "aws_network_interface_sg_attachment" "example" {
  security_group_id    = aws_security_group.ec2_security_group.id
  network_interface_id = aws_instance.ec2_instance.network_interface_ids[0]
}
