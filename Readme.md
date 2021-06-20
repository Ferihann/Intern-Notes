# IMAGE SHARING SYSTEM 

**Ferihan Çabuk 150116059**


**Anıl Altay 150118824**


In this project, we created a simple file sharing system. There are multiple users and one server in our system.
User create its public key and private key pair.
Every user generate its public and private key and one simetric key.
Every user who joins the system is registered to the server with a public key and user name.

Bonus part is not included in the project but as an extra, when a user logs in they get notifications they missed when they were offline.

**REGISTRATION & PUBLIC KEY CERTIFICATION**

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/register_view.png)

User enters a username and clicks to register button. At this point, a public and a private key pair are generated for user and stored in 'User_Keys' folder under the root directory named as the username entered. Then, generated public key is sent to the server, server signs the received public key,records user credentials to database along with this certificate and sends certificate back to the user, then user decrypts this certificate and checks if it matches with their public key.

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/users_table.png)

If user logs in with the same username again from same client. Public and private key information is read from the stored file and certificate check process is repeated. This repeats for every log-in process.

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/login_view.png)

After login 'Image Sharing System' page opens. In Image Sharing System, there are two buttons, one for encrypting and uploading the image to the server and the other one is for downloading the image. It is expected that Browse button is clicked to select an image file.

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/image_sharing_system.png)

**IMAGE POSTING**

From the browse button user can select image for encryption. Then when 'Encrypt&Upload' button is pressed , firstly client encrypt image with AES CBC mode, signed the encrypted image, then encrypt its Aes key with the public key of server. Then sends encrypted image, signed encrypted image, and encrypted AES key along with the full name of the file to the server.

Server saves the image file to the 'images' directory under its root directory. Then gives a path from there to database along with the sent information. We prefered to store AES Key and IV information as base64 encoded byte strings instead of BLOBs in database. These information is base64 encoded from client and stored.

In our approach we didn't allow user to enter image name but took the file name as image name and saved image according to the file name.
Users can download images with file name.

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/images_table.png)

**NOTIFICATIONS**

When a user uploads an image to the system, server sends notifications to all users.
Even though users are offline, they will receive the missed notifications when they login.
For this, our approach was to create a notification log table and log if a user is informed of an uploaded image. If not when user requests their notifications, missing notifications are returned to the user and this notifications are logged to table as user received the notification of the specific image.

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/notification.jpeg)
![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/notificationlog_table.png)

**IMAGE DOWNLOADING**

When user wants to download image, it enters the image name and clicks the download button. A request is sent to server with the username of requesting user and image name. Then server sends the encrypted image, certificated public key of owner, AES Key&IV encrypted with the public key of requesting user, signed encrypted image(digital signature) and the fullname of the image to the requested user.

User firstly extracts public key of the image owner, then decrypts the digital signature of image with this key. Then hashes encrypted image with SHA256 hash function and compares these two values for message integrity. Then, if these two values are equal, encrypted AES Key and IV is decrypted with user's private key for confidentiality. After AES Key and IV are decrypted and seperated, image file is decrypted, saved to 'Downloaded_Images' directory in root of client, and finally shown to the user.

![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/image_download.png)

**POTENTIAL SECURITY HOLES AND COUNTERMEASURES**

For now, user private and public key is stored to a text file for further usage. This is a major security hole. To test multiple user usage we preferred this way. But, if let only one user use the client in a device we can store key pairs in a external keychain system like WhatsApp.



**DATABASE SCHEMA**  
![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/database_schema.png)

**FLOW DIAGRAM**
![Alt Text](https://github.com/anilaltay/CSE4057_Programming_Assignment/blob/master/Screenshots/security.png)