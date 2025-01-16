# HackNYU

This is Hack NYU.
We are aimed to created a website that transfers handwritten text to code. For instance, a user might take notes in their CS class on their ipad, LetMeCode enables the user to be able to export this handwritten text to their perferred IDE such as VSCode. 

Can be found @ https://eliotb26.github.io/HackNYU/


Used Google Cloud AutoML, and Google Cloud Vision API in the final project, while also tested MyScript API, but choose to not include. 


Package required: 
- pip3 install --upgrade google-cloud-vision
- pip3 install pandas



Character Recognition on local image files:
Need "GOOGLE_APPLICATION_CREDENTIALS" set to local json file.
Call the function with the path to the image. 
