from django.db import models

# Create your models here.

class Intro(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=30, null=True, blank=True)
    small_brief = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed Intro"



class frontendSkills(models.Model):
    frontend_skill = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.frontend_skill or "Unnamed Skill"
    

class backendSkills(models.Model):
    backend_skill = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.backend_skill or "Unnamed Skill"
    

class toolsTech(models.Model):
    tools = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.tools or "No Tools"
    

class TechTag(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed Tech"


class projects(models.Model):
    project_title = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    # tech_stuff = models.
    live_demo = models.URLField(max_length=50, null=True, blank=True)
    github = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.project_title or "No Projects"
    

class contact_info(models.Model):
    email = models.EmailField(max_length=30, null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    response_time = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.email or "No Contact Info"
    

class socialLinks(models.Model):
    linkedin = models.URLField(max_length=30, null=True, blank=True)
    github = models.URLField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.linkedin or "No Links Provided"