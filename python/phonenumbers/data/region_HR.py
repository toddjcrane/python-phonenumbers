"""Auto-generated file, do not edit by hand. HR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_HR = PhoneMetadata(id='HR', country_code=385, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-7]\\d{5,8}|[89]\\d{6,11}', possible_number_pattern='\\d{6,12}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1\\d{7}|(?:2[0-3]|3[1-5]|4[02-47-9]|5[1-3])\\d{6}', possible_number_pattern='\\d{6,8}', example_number='12345678'),
    mobile=PhoneNumberDesc(national_number_pattern='9[1257-9]\\d{6,10}', possible_number_pattern='\\d{8,12}', example_number='912345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='80[01]\\d{4,7}', possible_number_pattern='\\d{7,10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='6(?:[09]\\d{7}|[145]\\d{4,7})', possible_number_pattern='\\d{6,9}', example_number='611234'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='7[45]\\d{4,7}', possible_number_pattern='\\d{6,9}', example_number='741234567'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='62\\d{6,7}', possible_number_pattern='\\d{8,9}', example_number='62123456'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(1)(\\d{4})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(6[09])(\\d{4})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['6[09]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(62)(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['62'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='([2-5]\\d)(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[2-5]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9\\d)(\\d{3})(\\d{3,4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9\\d)(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9\\d)(\\d{3,4})(\\d{3})(\\d{3})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['9'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2,3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['6[145]|7'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['6[145]|7'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(80[01])(\\d{2})(\\d{2,3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(80[01])(\\d{3,4})(\\d{3})', format=u'\\1 \\2 \\3', leading_digits_pattern=['8'], national_prefix_formatting_rule=u'0\\1')],
    mobile_number_portable_region=True)
