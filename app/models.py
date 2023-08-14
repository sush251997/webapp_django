from django.db import models

class Company(models.Model):
    cmp_name = models.CharField(max_length=255)
    cmp_link = models.CharField(max_length=255)
    cmp_year_founded = models.CharField(max_length=255)
    cmp_type = models.CharField(max_length=255)
    cmp_Size_range = models.CharField(max_length=255)
    cmp_location = models.CharField(max_length=255)
    cmp_country = models.CharField(max_length=255)
    cmp_linkedin = models.TextField()
    cmp_emp_estimate = models.CharField(max_length=255)
    total_cmp_emp = models.CharField(max_length=255)

class userlogin(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True, auto_created=True)
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)

