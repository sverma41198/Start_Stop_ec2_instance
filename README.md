**Project: Using Lambda Function to Start & Stop the EC2 Instance Using Cloud watch Event**

**Agenda:**

- Create a function to start an ec2 instance at 10 AM IST if the instance has tag ec2\_start = "true".
- Create a function to stop an ec2 instance at 10 PM IST if the instance has tag ec2\_stop = "true".
- Outcome is ec2 instance should start or stop automatically based on cron job schedule.
- Keep the code stuff into the git repository.
- Document all the execution steps.

**Prerequisites:**

- **Aws account (Servicer:**Ec2, IAM, Lambda Function, CloudWatch Events)
- **Github Account**

**Project Architecture:**

![](Readme/Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.001.png)

**Execution Steps:**

1) **Create an IAM policy and execution role for your Lambda function**
1. [**Create an IAM policy using the JSON policy editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor)**.** {

"Version": "2012-10-17",

"Statement": [

{

"Effect": "Allow",

"Action": [

"logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"

],

"Resource": "arn:aws:logs:\*:\*:\*"

}, {

"Effect": "Allow", "Action": [

"ec2:Start\*", "ec2:Stop\*"

],

"Resource": "\*"

}

]

}

2. **Create an IAM role for Lambda.**
- **Added StartStopec2poily (custom) and AmazonEC2FullAccess**
2) **Create Lambda functions that stop and start your EC2 instances**
1. **Open the Lambda console, and then choose the Create function.**
1. **Choose an Author from scratch.**
1. **Under Basic information, add the following information:**

**For Function name, enter a name that identifies it as the function that's used to stop your EC2 instances. For example, "StopEC2Instances".**

**For Runtime, choose Python 3.9.**

**Under Permissions, expand Change default execution role. Under Execution role, choose Use an existing role.**

**Under Existing role, choose the IAM role that we created.**

![](Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.002.jpeg)

4. **Startinstance lambda function:**

![](Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.003.jpeg)

5. **Stopinstance lambda function:**

![](Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.004.jpeg)

6. **Test your Lambda functions**
1. **Open the Lambda console, and then choose Functions.**
1. **Choose one of the functions that you created.**
1. **Choose the Code tab.**
1. **In the Code source section, choose Test.**
1. **In the Configure test event dialog box, choose Create new test event.**
1. **Enter an Event name. Then, choose Create.**

**Note: Don't change the JSON code for the test event. The function doesn't use it.**

7. **Choose Test to run the function.**
3) **Create EventBridge rules that run your Lambda functions**
1. **Open the CLoudWatch**
1. **Select Create rule.**

**c . Enter a Name for your rule, "startinstances".**

**Description-Starting instance at 10:00 AM IST**

4. **Enter a Name for your rule, "stopinstances".**



|**Description**|**-Stopping instance at 10:00 PM IS**|
| - | - |
|||
5. **For Schedule pattern ‘start instance’,**

**Schedule Cron expression 30 4 \* \* ? \***

**For starting the instance at 4:30 GMT i.e. 10:00 AM in IST Then Lambda startinstance as target**

**6. For Schedule pattern ‘stopinstance’,**

**Schedule Cron expression 30 16 \* \* ? \*![](Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.005.png)**

**For stoping the instance at 16:30 GMT i.e. 10:00 PM in IST**

![](Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.006.jpeg)

![](Aspose.Words.64e7f0df-54b6-4fd3-acd4-5d18027cfd84.007.jpeg)

4) **Code Repo:**

[**Link: https://github.com/sverma41198/Start_Stop_ec2_instance**](https://github.com/sverma41198/Start_Stop_ec2_instance)

5) **Outcome:**
- **Ec2 instances with “ec2-start:true” tag started at 10:00 Am IST**
- **Ec2 instances with “ec2-stop:true” tag stopped at 10:00 PM IST**
