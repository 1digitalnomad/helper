from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['first_name']) < 2:
            errors.append('First name must be longer than 2 characters. Try again')
        if len(form['last_name']) <2:
            errors.append('Last name must be filled out. Try again.')
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Please enter a valid email address.')
        if len(form['password']) <8:
            errors.append('Password should be at least 8 characters. Try again.')
        if form['password'] != form['confirm_pw']:
            errors.append('Passwords must match. Please try again.')
        print(errors)
        print(form)

        if self.filter(email=form['email']):
            errors.append('email address is already in use.')

        return errors

    def create_user(self, form_data):
        pw_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
        user = self.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'], 
            email = form_data['email'], 
            pw_hash=pw_hash,
        )
        
        return user

    def login(self, form):
        user_list = self.filter(email=form['email'])
        if len(user_list) > 0:
            user = user_list[0]
            if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                return (True, user.id, user.first_name)
            else:
                return(False, "Email or Password is not right.")

        else:
            return(False, "Email or Password is not right. Try again.")
        





# Create your models here.
class User(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "<User object: {} {}>" .format(self.first_name, self.last_name)
