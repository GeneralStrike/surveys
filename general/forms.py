from django import forms

from .models import UserSurvey


class UserSurveyForm(forms.ModelForm):

    class Meta:
        model = UserSurvey
        fields = (
            'gender',
            'age_range',
            'net_usage',
            'sec_training',
            'pwd_mgr',
            'pwd_reuse',
            'pwd_long',
            'twofa',
            'backups',
            'vpn',
            'ad_block',
            'updates',
            'important_things',
            'online',
            'family',
            'guru_family',
            'sec_org',
            'gov',
            'other',
            'noanswer',
            'other_sources',
            'target',
            'target_reasons',
            'financial',
            'email_account',
            'home_address',
            'medical_info',
            'photos',
            'location_history',
            'childrens_info',
            'browser_search_history',
            'social_sec_tfn',
            'social_media',
            'loss_of_data',
            'loss_of_funds',
            'dignity',
            'physical_safety',
            'restriction',
            'emotional_safety',
            'integrity',
            'what_threat_looks_like',
            'good_security_steps',
            'feel_secure',
            'not_concerned',
            'not_a_target',
            'confused',
            'inconvenient',
            'locking_out',
            'forget',
            'scam_concern',
            'time_issues',
            'trust_issues',
            'confident',
            'anything_else',
        )
        widgets = {
            'gender': forms.RadioSelect,
            'age_range': forms.RadioSelect,
            'net_usage': forms.RadioSelect,
            'sec_training': forms.RadioSelect,
            'pwd_mgr': forms.RadioSelect,
            'pwd_reuse': forms.RadioSelect,
            'pwd_long': forms.RadioSelect,
            'twofa': forms.RadioSelect,
            'backups': forms.RadioSelect,
            'vpn': forms.RadioSelect,
            'ad_block': forms.RadioSelect,
            'updates': forms.RadioSelect,
            'good_security_steps': forms.RadioSelect,
            'feel_secure': forms.RadioSelect,
            'not_concerned': forms.RadioSelect,
            'not_a_target': forms.RadioSelect,
            'inconvenient': forms.RadioSelect,
            'locking_out': forms.RadioSelect,
            'forget': forms.RadioSelect,
            'target': forms.RadioSelect,
            'financial': forms.RadioSelect,
            'email_account': forms.RadioSelect,
            'home_address': forms.RadioSelect,
            'medical_info': forms.RadioSelect,
            'photos': forms.RadioSelect,
            'location_history': forms.RadioSelect,
            'childrens_info': forms.RadioSelect,
            'browser_search_history': forms.RadioSelect,
            'social_sec_tfn': forms.RadioSelect,
            'social_media': forms.RadioSelect,
            'loss_of_data': forms.RadioSelect,
            'loss_of_funds': forms.RadioSelect,
            'dignity': forms.RadioSelect,
            'physical_safety': forms.RadioSelect,
            'restriction': forms.RadioSelect,
            'emotional_safety': forms.RadioSelect,
            'integrity': forms.RadioSelect,
            'confident': forms.RadioSelect,
            'confused': forms.RadioSelect,
            'incapable': forms.RadioSelect,
            'scam_concern': forms.RadioSelect,
            'trust_issues': forms.RadioSelect,
            'time_issues': forms.RadioSelect,
        }
