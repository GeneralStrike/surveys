from django.db import models

from surveys.models import TimeStampedModel


class DevSurvey(TimeStampedModel):
    NOTRAINING = 'notraining'
    SELF = 'self'
    WORKPLACE = 'workplace'
    SHORTCOURSE = 'shortcourse'
    DEGREE = 'degree'

    TRAINING_CHOICES = (
        (NOTRAINING, 'No training'),
        (SELF, 'Self taught only'),
        (WORKPLACE, 'Basic workplace training or conference workshops'),
        (SHORTCOURSE, 'Professional short courses (online or in person)'),
        (DEGREE, 'Diploma, degree or post-graduate'),
    )

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

    VPOOR = 'vpoor'
    POOR = 'poor'
    OK = 'ok'
    GOOD = 'good'
    EXCELLENT = 'excellent'
    NOANSWER = 'noanswer'

    RATING_CHOICES = (
        (VPOOR, 'Very poor'),
        (POOR, 'Poor'),
        (OK, 'OK'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
        (NOANSWER, 'Prefer not to answer'),
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

    ALWAYS = 'always'
    OFTEN = 'often'
    SOMETIMES = 'sometimes'
    RARELY = 'rarely'
    NEVER = 'never'
    IRRELEVANT = 'irrelevant'
    IDK = 'idk'
    NOANSWER = 'noanswer'

    IWIIC_CHOICES = (
        (ALWAYS, 'Always'),
        (OFTEN, 'Often'),
        (SOMETIMES, 'Sometimes'),
        (RARELY, 'Rarely'),
        (NEVER, 'Never'),
        (IDK, 'I don\'t know'),
        (IRRELEVANT, 'Not relevant'),
        (NOANSWER, 'Prefer not to answer'),
    )

    SIGNIFICANT = 'significant'
    MODERATE = 'moderate'
    SLIGHT = 'slight'
    NOIMPACT = 'noimpact'
    NOANSWER = 'noanswer'

    IMPACT_CHOICES = (
        (SIGNIFICANT, 'Significant'),
        (MODERATE, 'Moderate'),
        (SLIGHT, 'Slight'),
        (NOIMPACT, 'None'),
        (NOANSWER, 'Prefer not to answer'),
    )

    VUNCOMFY = 'vuncomfy'
    SUNCOMFY = 'suncomfy'
    AMB = 'ambivalent'
    SCOMFY = 'scomfy'
    VCOMFY = 'vcomfy'
    NOANSWER = 'noanswer'

    COMFORT_CHOICES = (
        (VUNCOMFY, 'Very uncomfortable'),
        (SUNCOMFY, 'Somewhat uncomfortable'),
        (AMB, 'Ambivalent'),
        (SCOMFY, 'Somewhat comfortable'),
        (VCOMFY, 'Very comfortable'),
        (NOANSWER, 'Prefer not to answer'),
    )

    # demographics
    backend = models.BooleanField(default=False)
    frontend = models.BooleanField(default=False)
    archeng = models.BooleanField(default=False)
    devops = models.BooleanField(default=False)
    infrastructure = models.BooleanField(default=False)
    project = models.BooleanField(default=False)
    qa = models.BooleanField(default=False)
    testing = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    ux = models.BooleanField(default=False)

    sec_training = models.CharField(
        max_length=255, default=None, choices=TRAINING_CHOICES
    )
    my_awareness = models.CharField(
        max_length=255, default=None, choices=RATING_CHOICES
    )
    gender = models.CharField(
        max_length=255, default=None, choices=GENDER_CHOICES
    )
    tech = models.CharField(max_length=255)

    # about your work
    employer_sec_support = models.CharField(
        max_length=255, default=None, choices=RATING_CHOICES
    )
    policy = models.CharField(
        max_length=255, default=None, choices=YNDK_CHOICES
    )
    sec_workflow = models.CharField(
        max_length=255, default=None, choices=YNDK_CHOICES
    )

    # if I could I would
    review_dependencies = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    update_dependencies = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    key_rotation = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    rm_ex_dev_access = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    rm_committed_keys = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    vuln_scan = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    pentest = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    logging = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )
    code_review = models.CharField(
        max_length=255, default=None, choices=IWIIC_CHOICES
    )

    # barriers
    other_barriers = models.TextField(blank=True)
    no_time = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    employer_interest = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    employer_understanding = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    user_interest = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    my_interest = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    my_expertise = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    team_expertise = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    working_relationship = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    legacy = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    resources = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    difficult_docs = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )
    confusing_advice = models.CharField(
        max_length=255, default=None, choices=IMPACT_CHOICES
    )

    # about your feelings
    comfort_approaching = models.CharField(
        max_length=255, default=None, choices=COMFORT_CHOICES
    )
    comfort_researching = models.CharField(
        max_length=255, default=None, choices=COMFORT_CHOICES
    )
    comfort_explanation = models.TextField(blank=True)

    # free text in general
    what_would_help = models.TextField()
    story = models.TextField(blank=True)
    anything_else = models.TextField(blank=True)
