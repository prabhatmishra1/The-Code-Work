from django.core.validators import RegexValidator


''' =============================================================================
    Description: Regix validators for Phone.    
    Author:Prabhat Mishra
    ==============================================================================
'''
phone_regix = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message=("Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed."))
