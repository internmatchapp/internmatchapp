from django.shortcuts import render
from django.views.generic import ListView

from internships.models import Posting, Applicant, Business, Attribute
from django.contrib.auth.models import User

class PostingList(ListView):
    context_object_name = 'postings_list'
    template_namE

    def get_queryset(self):
        from django.utils import timezone
        self.postings = Posting.objects.filter(post_status__eq = 'pb').exclude(pub_date__gt = timezone.now())
