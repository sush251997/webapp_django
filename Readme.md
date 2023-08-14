Welcome to the Catalyst Count Web Application! This application is designed to allow users to upload and manage large volume CSV data, perform data filtering, and visualize the upload progress. This README file provides an overview of the application, its features, setup instructions, and other essential details.

**Overview:**
The Catalyst Count Web Application is built using Django 3.x/4.x, Postgres, and Bootstrap 4/5. It offers a seamless user experience for uploading large CSV data files, processing the data, and querying it using a user-friendly interface. Users can visualize the upload progress, filter data, and retrieve record counts based on applied filters.

**Getting Started:**
To run this application, you'll need the following software installed on your system:
Python 3.x/Anaconda
Visual Code Studio
PostgreSQL
Git

**Install the required dependencies:**
pip install -r requirements.txt
**Create a media folder below. catalyst_count folder and then start running the project**

Set up environment variables using django-environ. Create a .env file in the project directory and provide necessary configurations like database settings, secret key, etc.

Access the application in your web browser at http://127.0.0.1:8000.

Features
The Catalyst Count Web Application provides the following features:

User authentication and secure login using django-all-auth.
Visual progress indicator during the upload of large CSV files.
Data storage in a Postgres database.
User-friendly UI using Bootstrap 4/5 for a modern and responsive design.
Data filtering using a Query Builder form.
Displaying record counts based on applied filters.
Maintaining project history on Bitbucket or GitHub using Git.
Usage
Login: Access the application using your credentials and the secure login system provided by django-all-auth.

Upload Data: Upload large volume CSV data files using the provided upload feature. Track the upload progress visually.

Query Builder: Filter the uploaded data using a user-friendly form. Apply various filters and retrieve record counts based on your selections.

Users: Manage user access and permissions using the authentication system.

Technologies Used
Django 3.x/4.x
PostgreSQL
Bootstrap 4/5
django-all-auth
Git
Contributing
Contributions are welcome! If you have suggestions, bug reports, or improvements, please feel free to submit issues or pull requests.

License
This project is licensed under the MIT License.

Thank you for using the Catalyst Count Web Application! We hope you find it useful and efficient for managing large volume CSV data. If you encounter any issues or have any questions, please don't hesitate to contact us.
