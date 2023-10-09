Your project will depend on the Google credentials Steps to be followed when creating a project in Google Cloud.

Process of setting up an account for Google Project =>
Create a Google Cloud Platform (GCP) project.
If you don't have a Google Cloud account, create one and sign in.
Enable the necessary APIs eg.(Google Drive APIs) for your project.
Create a service account key for your project.
Download the service account key file and securely store it.
Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your service account key file.

You will receive the credentials like this one 
{
  "type": "service_account",
  "project_id": "xxxxx",
  "private_key_id": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
  "private_key": "-----BEGIN PRIVATE KEY-----\xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==\n-----END PRIVATE KEY-----\n",
  "client_email": "xxxxxxxxxxxxx@gmail.com",
  "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/xxxx",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/googledrive%xxxxxxxxxxxxxxxxxxx",
  "universe_domain": "xxxxxxxx.com"
}