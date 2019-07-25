# Personal Website

This is the Git repository for hyunwookshin.com

## Deployment

### AWS CodeDeploy

[AWS CodePipeline](https://aws.amazon.com/getting-started/tutorials/continuous-deployment-pipeline/) is used to deploy the website directly from this GitHub repository.

### Frontend

The frontend is written in [Vue.js](https://vuejs.org/) and [Bootstrap-Vue](https://bootstrap-vue.js.org).
To run the web server in a demo environment run:

```
make install #one time
make build   #one time
make run
```

The webpage is then accessible via `http://localhost/8080`

The frontend is served directly from Amazon **S3 bucket** fronted by [AWS Cloudfront](https://aws.amazon.com/cloudfront) CDN.

### Backend (REST)

The REST endpoints, implemented in Python, will be deployed using FaaS (function as a service) model
as [lambda functions](https://aws.amazon.com/lambda/)

To deploy the backend functions run

```
make config
make backend
```

### Backend (Stream)

Amazon Kinesis and kubernetes is used to read and parse incoming tweets.

### Database

AWS DynamoDB is used to store all post data defined as:

```
{
   "title" : <string>,
   "section" : <string>,
   "content" : <string>,
   "uploaded" : <date>,
   "img_url" : <string>,
   "external_url" : <string>,
   "posted_by" : <string>
}
```

**title** and **section** are partition and sort keys. The optional
fields are **img_url** and **external_url**.
Python boto3 will be used to access the Dynamo DB.

### Authentication

The authentication and authorization is managed by AWS Cognito.
