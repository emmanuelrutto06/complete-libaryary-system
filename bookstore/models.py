from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime,timedelta


# from .models import Student

#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.IntegerField()
       

class Book(models.Model):
    id = models.AutoField(primary_key="True")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='bookapp/pdfs/')
    cover = models.ImageField(upload_to='bookapp/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)        

# class Borrow(models.Model):
#     id = models.AutoField(primary_key=True)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     borrow_date = models.DateTimeField(null=True)
#     return_date = models.DateTimeField(null=True)
    
#     def __str__(self):
#         return self.student.first_name+" borrowed "+self.book.title
    

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)



class DeleteRequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.delete_request


class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.feedback

# def get_returndate():
#     return datetime.today() + timedelta(days=8)

class issue_book(models.Model):
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    student_id = models.ForeignKey('Student', on_delete= models.CASCADE)
    issue_date = models.DateTimeField()
    when_to_return=models.DateField(null=True, blank=True,help_text="Date the book is returned")

    def __str__(self):
        return self.student.fullname + " borrowed " + self.book.book_title

class BookInstance(models.Model):
    id=models.IntegerField(primary_key=True,help_text="Book unique id across the Library")
    book=models.ForeignKey('Book', on_delete=models.CASCADE,null=True)
    book_number=models.PositiveIntegerField(null=True,help_text="Book number for books of the save kind")
    Is_borrowed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} {self.book}"




