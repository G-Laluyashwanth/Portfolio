from django.contrib import admin
from .models import (
    Intro, frontendSkills, backendSkills,
    toolsTech, TechTag, projects, contact_info, socialLinks
)
from unfold.admin import ModelAdmin as UnfoldModelAdmin


@admin.register(Intro)
class IntroAdmin(UnfoldModelAdmin):
    pass

@admin.register(frontendSkills)
class FrontendSkillsAdmin(UnfoldModelAdmin):
    pass

@admin.register(backendSkills)
class BackendSkillsAdmin(UnfoldModelAdmin):
    pass

@admin.register(toolsTech)
class ToolsTechAdmin(UnfoldModelAdmin):
    pass

@admin.register(TechTag)
class TechTagAdmin(UnfoldModelAdmin):
    pass

@admin.register(projects)
class ProjectsAdmin(UnfoldModelAdmin):
    pass

@admin.register(contact_info)
class ContactInfoAdmin(UnfoldModelAdmin):
    pass

@admin.register(socialLinks)
class SocialLinksAdmin(UnfoldModelAdmin):
    pass
