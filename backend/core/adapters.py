from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from core.models import Profile, Candidate


class CandidateSocialAccountAdapter(DefaultSocialAccountAdapter):

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        Profile.objects.get_or_create(
            user=user,
            defaults={'role': 'candidate'}
        )

        full_name = user.get_full_name() or user.email or user.username

        Candidate.objects.get_or_create(
            user=user,
            defaults={
                'full_name': full_name,
                'phone': '',
                'experience_years': 0,
            }
        )

        return user

    def get_login_redirect_url(self, request):
        return '/candidate/dashboard/'