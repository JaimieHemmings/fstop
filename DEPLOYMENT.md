# FStops Photography Deployment &amp; Local Development

## Cloning

- Navigate to this projects repo page on Github
- Click the Code Button at the top right
- Select HTTPS and copy the link
- In the terminal of your IDE enter the command "git clone" followed by the link
- Press enter
- Set up a virtual python environment
- Back in the terminal run ```pip install -r requirements.txt```
- Then in the terminal run ```python manage.py runserver```

## Forking

- To fork the repo, from the repo click the "Fork" button at the top right
- This should add a fork of the repo to your own collection of repos on Github

## Deployment Steps

This website is hosted on Heroku, using AWS3 for image hosting, Stripe for Payment processing and Google for analytics

Prerequisites:

- [Github Account](https://github.com/)
- [Heroku Account](https://www.heroku.com)
- [Google Analytics Account (Optional)](https://developers.google.com/analytics)
- [Stripe Account (Optional)](https://stripe.com/gb)
- [Amazon Web Services account](https://aws.amazon.com/) - [Set Up Guide](#aws-s3-bucket-set-up-guide)

1. After forking or cloning the repo (Instructions below) to your own Github account (Create one if necassary)
2. Open the file "templates/base.html"
  - Find the string in the head element containing ```gtag('config', 'G-**********');```
  - Replace the alpha numeric string with your own from Google Anlytics
3. Log into Heroku and click the "New" Button. Select a name for your app and click "Create New app"
4. From within the app, go to "Resources" tab and use the search function to look for the add on named "Heroku Postgres" and enable the addon
5. Go to the Settings Tab and click the button "Reveal Config Vars"
6. Create the following config Vars and add your own relevant keys
  - "AWS_ACCESS_KEY_ID"
  - "AWS_SECRET_ACCESS_KEY"
  - "AWS_STORAGE_BUCKET_NAME"
  - "DEBUG"
  - "SECRET_KEY"
  - "STRIPE_PUBLIC_KEY"
  - "STRIPE_SECRET_KEY"
  - "STRIPE_WH_SECRET"
  - "USE_AWS"
7. Go to the Deploy tab and find the section "Deployment Method"
8. Choose GitHub and follow the steps to choose the relevant Repo
  - This should be the repo you created when you forked or cloned this repo
9. Next, Select Automatic Deploys from the relavant branch
  - Select Main if you have not made any changes
10. Click Deploy
11. Click Overview and wait for the "latest Activity" Stream to show "Deployed"
12. In the top right of the screen is a button "More", click this and select "Run Console"
13. Type "Bash" and wait for the terminal to load
14. Once loaded type "python manage.py migrate" and press enter
15. Then type "python manage.py createsuperuser" and follow the steps to create your first superuser account
16. At this point your site should be up and running but there is a few database entries we need to manually create, Heroku should have given you the URL of your website, navigate to it.
17. Then manually navigate to ```/admin``` and log in
18. The following databases entries will need a singular object to be populated manually:
  - About Pages
  - Home page abouts
  - Home page heros
  - Home page trusted bys
19. Then go to the Database management for 'Services Pages' and create and entry for 'Aerial', 'Property', 'Event' and 'Lifestyle', ensuring that the Title for each one matches that string exactly.
20. From here the content can be entirely managed in the Admin area. (/control-panel)

### AWS S3 Bucket set up guide

1. Create an account with AWS
2. Select personal for account type
3. Enter billing details when prompted
4. Complete the verification if necassary
5. Use the search functionality to find the S3 Admin panel
6. Create a new bucket
7. Name the bucket appropriately
8. Select your closest region for the hosting location
9. On the Object Ownership select ACL's enabled
10. Select "Bucket Owner Preferred" from the dropdown that appears
11. Uncheck "block all public access" and acknowledge the warning that appears
12. Click create bucket
13. Click into the bucket you just created and select "Properties" from the tabs available at the top
14. Scroll down to "Static Web Hosting" and click enable, add "index.html" and "error.html" to the fields for "index document" and "error document"
15. Open the permissions tab, copy the ARN (Amazon Resource Name) and navigate to the policy section, click edit and select "policy generator"
16. Under "Select Type Policy" select "S3 Bucket Policy"
17.  allow all principal by adding the * to the input and the from the Actions dropdown, select GetObject.
18. Paste the ARN we copied into the ARN (Amazon Resource Name) input field and click add statement, then click generate policy, copy the Policy from the new popup and paste it into the bucket policy editor and add /* at the end of the resource value to allow access to all resources in this policy and finally, click save.
19. In the CORS section copy in the following code:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

20. Navigate to the ACL (Access Control List)
21. Click Edit and tick List for *Everyone (public access)* and accept the warning.

#### The IAM Set up

1. Find IAM services using the search bar again
2. Create a group by selecting "User Groups"
3. Click "Create Group"
4. Choose a name
5. Click "Create Policy"
6. Open the JSON tab on the new page and select "import managed policy"
7. Search for S3 and select the predefined policy *AmazonS3FullAccess* and click import
8. Edit the policy by entering the code:
  - Replace *your-bucket-name with the name of your bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*",
            ]
        }
    ]
}
```

9. Click Next
10. Click Review
11. Give the policy a name and description
12. Attach the policy to the group you created by navigating back to user groups
13. Go to the permission tab
14. Click "Add permission"
15. Click "Users" then "Add Users" and give the user a name
16. Tick "Programmatic Access" from access type
17. Click Next
18. Add the user we just created to the group we created earlier
19. Download the .csv file containing the secret keys used to authenticate them from within our app.