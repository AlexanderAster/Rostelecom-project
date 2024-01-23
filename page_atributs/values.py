'''Параметры отобраны с учётом документации-требований'''
class RegValues: 
    # Валидные значения:
    correct_name = 'Имя' # Можно заменить или оставить
    correct_surname = 'Фамилия' # Можно заменить или оставить
    correct_email = 'email' # Необходимо заменить на свой!
    correct_phone = 'phone' # Необходимо заменить на свой!
    correct_pass = 'Parparpum009' # Можно заменить или оставить
    correct_pass2 = 'Pumpumpar001'
    # Невалидные значения (негативные тесты):
    big_name = 'Орафцафрвкрквцййфчмиелшндрпбпртаееа' 
    big_surname = 'Ртаееащрквцййфчмиелшндрафцафрвкрпбп'
    big_phone = '95040831019504083101'
    big_email = 'ofofof@bk.ruofofofo@bk.ru'
    big_pass = 'Parwafawf1awfawfawfwa15125125'
    small_name = 'П'
    small_surname = 'Ш'
    small_phone = '40020'
    small_pass = 'Firgu4'
    eng_name = 'Ostap'
    eng_surname = 'Gingozu'
    wrong_email = 'piwpiw@bk.bu'
    rus_pass = 'КапустноеРагу810'
    only_number_pass = '921374500'
    only_text_pass = 'KapustnoeRagu'
    special_coding_name = '*Григорий?№"/'
    special_coding_surname = '@Воздухо~водов!@'
class AuthValues:
    # Валидные значения:
    correct_email = 'email' # Необходимо заменить на свой!
    correct_phone = 'phone' # Необходимо заменить на свой!
    correct_pass = 'Parparpum009'
    correct_ls = '650208410156' # Можно заменить или оставить
    correct_login = 'Login' # Можно заменить или оставить
    # Невалидные значения (негативные тесты):
    wrong_ls = '6528'
    wrong_login = 'MudDog8'
    wrong_phone = '345'
    wrong_email = 'piwpiw@bk.bu'
    wrong_pass = 'КапустноеРагу810'
    random_sms_code = '445869'
    MAIN_URL = 'https://start.rt.ru/?tab=main'