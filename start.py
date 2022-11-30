import boto3

def start_model(project_arn, model_arn, version_name, min_inference_units):

    client=boto3.client('rekognition')

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')
    
def main():
    project_arn='arn:aws:rekognition:us-east-1:843645451050:project/face_recognition_model/1669822511444'
    model_arn='arn:aws:rekognition:us-east-1:843645451050:project/face_recognition_model/version/face_recognition_model.2022-11-30T21.22.27/1669823552738'
    min_inference_units=1 
    version_name='face_recognition_model.2022-11-30T21.22.27'
    start_model(project_arn, model_arn, version_name, min_inference_units)

if __name__ == "__main__":
    main()