from django.shortcuts import render

from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def home(request):
    bio = Bio.objects.first()
    education_list = Education.objects.all().order_by("order", "id")
    skills_list = Skill.objects.all().order_by("order", "id")
    experience_list = Experience.objects.all().order_by("order", "id")
    projects_list = Project.objects.all().order_by("order", "id")

    return render(request, "home.html", {
        "bio": bio,
        "education_list": education_list,
        "skills_list": skills_list,
        "experience_list": experience_list,
        "projects_list": projects_list,
    })
