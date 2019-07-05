from django.db import models


from surveys.models import TimeStampedModel


class UserSurvey(TimeStampedModel):
    WOMAN = 'woman'
    MAN = 'man'
    NBGQ = 'nbgq'
    NOANSWER = 'noanswer'

    GENDER_CHOICES = (
        (WOMAN, 'Woman'),
        (MAN, 'Man'),
        (NBGQ, 'Non-binary or gender queer'),
        (NOANSWER, 'Prefer not to answer'),
    )

    TEENS = 'teens'
    TWENTIES = 'twenties'
    THIRTIES = 'thirties'
    FORTIES = 'forties'
    FIFTIES = 'fifties'
    SIXTIES = 'sixties'
    SEVENTIES = 'seventies'
    EIGHTIES = 'eighties'
    NINETYPLUS = 'nintyplus'
    NOANSWER = 'noanswer'

    AGE_CHOICES = (
        (TEENS, '10 - 19'),
        (TWENTIES, '20 - 29'),
        (THIRTIES, '30 - 39'),
        (FORTIES, '40 - 49'),
        (FIFTIES, '50 - 59'),
        (SIXTIES, '60 - 69'),
        (SEVENTIES, '70 - 79'),
        (EIGHTIES, '80 - 89'),
        (NINETYPLUS, '90+'),
        (NOANSWER, 'Prefer not to answer'),
    )

    ALLTHETIME = 'allthetime'
    LOTS = 'lots'
    DAILY = 'daily'
    BIWEEKLY = 'biweekly'
    WEEKLY = 'weekly'
    LESS = 'less'

    NET_USAGE_CHOICES = (
        (ALLTHETIME, 'Nearly all the time'),
        (LOTS, 'Several times a day'),
        (DAILY, 'Daily'),
        (BIWEEKLY, 'Several times a week'),
        (WEEKLY, 'Once a week'),
        (LESS, 'Less often'),
    )

    NOTRAINING = 'notraining'
    WORKPLACE = 'workplace'
    ITWORKPLACE = 'itworkplace'
    INFORMAL = 'informal'
    SHORTCOURSE = 'shortcourse'
    DEGREE = 'degree'

    TRAINING_CHOICES = (
        (NOTRAINING, 'No training'),
        (WORKPLACE, 'Basic workplace or community training (eg induction, library session)'),
        (INFORMAL, 'Informal professional training (eg conference workshop)'),
        (ITWORKPLACE, 'I work in IT but have no security training'),
        (SHORTCOURSE, 'Formal short course (eg online course)'),
        (DEGREE, 'Degree level or higher'),
    )

    EVERYWHERE = 'everywhere'
    IMPORTANT = 'important'
    ATWORK = 'atwork'
    ATWORKANDIMP = 'at_work_and_important'
    NO = 'no'
    NOANSWER = 'noanswer'

    BEHAVIOUR_CHOICES = (
        (EVERYWHERE, 'Yes, everywhere'),
        (EVERYWHERE, 'Yes, but only for important things'),
        (ATWORK, 'Yes, at work'),
        (ATWORKANDIMP, 'Yes, at work and for important things'),
        (NO, 'No'),
        (NOANSWER, 'Prefer not to say'),
    )

    YES = 'yes'
    NO = 'no'
    DONTKNOW = 'dontknow'
    NOANSWER = 'noanswer'

    YNDK_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),
        (DONTKNOW, 'I Don\'t know'),
        (NOANSWER, 'Prefer not to answer'),
    )

    MOST = 'most'
    SOMEWHAT = 'somewhat'
    AMBIVALENT = 'ambivalent'
    SOMEWHATDONT = 'somewhatdont'
    LEAST = 'least'
    NOANSWER = 'noanswer'

    PRIORITY_CHOICES = (
        (MOST, 'Very concerned'),
        (SOMEWHAT, 'Somewhat concerned'),
        (AMBIVALENT, 'Ambivalent'),
        (SOMEWHATDONT, 'Somewhat unconcerned'),
        (LEAST, 'Not concerned'),
        (NOANSWER, 'Prefer not to say'),
    )

    YSTRONG = 'ystrong'
    YSOMEWHAT = 'ysomewhat'
    NEITHER = 'neither'
    NSOMEWHAT = 'nsomewhat'
    NSTRONG = 'nstrong'
    NOANSWER = 'noanswer'

    FEELINGS_CHOICES = (
        (YSTRONG, 'Strongly agree'),
        (YSOMEWHAT, 'Somewhat agree'),
        (NEITHER, 'Neither agree or disagree'),
        (NSOMEWHAT, 'Somewhat disagree'),
        (NSTRONG, 'Strongly disagree'),
        (NOANSWER, 'Prefer not to say'),
    )

    # demographics
    gender = models.CharField(
        max_length=255, default=None, choices=GENDER_CHOICES
    )
    age_range = models.CharField(
        max_length=255, default=None, choices=AGE_CHOICES
    )
    net_usage = models.CharField(
        max_length=255, default=None, choices=NET_USAGE_CHOICES
    )
    sec_training = models.CharField(
        max_length=255, default=None, choices=TRAINING_CHOICES
    )

    # behaviours
    pwd_mgr = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    pwd_reuse = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    pwd_long = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    twofa = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    backups = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    vpn = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    ad_block = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    updates = models.CharField(
        max_length=255, default=None, choices=BEHAVIOUR_CHOICES
    )
    important_things = models.TextField(blank=True)

    # threat modelling
    target = models.CharField(
        max_length=255, default=None, choices=YNDK_CHOICES
    )
    target_reasons = models.TextField(blank=True)

    # data priotities
    financial = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    email_account = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    home_address = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    medical_info = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    photos = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    location_history = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    childrens_info = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    browser_search_history = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    social_sec_tfn = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    social_media = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )

    what_threat_looks_like = models.TextField(blank=True)

    # outcome priotities
    loss_of_data = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    loss_of_funds = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    dignity = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    physical_safety = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    restriction = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    emotional_safety = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )
    integrity = models.CharField(
        max_length=255, default=None, choices=PRIORITY_CHOICES
    )

    # feelings
    # why not better
    good_security_steps = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    feel_secure = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    not_concerned = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    not_a_target = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    inconvenient = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    locking_out = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    forget = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )

    # info sources booleans
    online = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    guru_family = models.BooleanField(default=False)
    sec_org = models.BooleanField(default=False)
    gov = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    noanswer = models.BooleanField(default=False)

    other_sources = models.TextField(max_length=255, blank=True)

    confident = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    confused = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    scam_concern = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    trust_issues = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    time_issues = models.CharField(
        max_length=255, default=None, choices=FEELINGS_CHOICES
    )
    anything_else = models.TextField(blank=True)
