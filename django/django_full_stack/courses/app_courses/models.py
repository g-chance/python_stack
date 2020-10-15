from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postRequest):
        errors = {}
        if len(postRequest['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters."
        if len(postRequest['desc']) < 15 and len(postRequest['desc']) > 0:
            errors['desc'] = "Description must be at least 15 characters."
        return errors


# class Description(models.Model):
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # description = models.OneToOneField(Description, on_delete = models.CASCADE)
    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.OneToOneField(Course, on_delete = models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, related_name="comments")