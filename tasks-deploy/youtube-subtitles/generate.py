TITLE = 'На Youtube обнаружено странное видео'
STATEMENT = '''
На самый популярный видеохостинг в мире — Youtube — пользователи каждую минуту загружают более четырёхсот часов видео, а просматривают более ста тысяч часов. При таком огромном количестве видеозаписей неудивительно, что время от времени на сайте находят что-то поистине необъяснимое.

На днях наш читатель из Великого Новгорода, пожелавший остаться анонимным, прислал в редакцию [ссылку на шестичасовое видео](https://www.youtube.com/watch?v=odWo7T1qA5U), на котором синтезированный голос читает очень длинный текст. Что это: аудиокнига для роботов или какое-то секретное послание? Члены редакции потратили на исследование записи несколько дней, но так и не смогли прослушать её целиком: монотонный голос и нудный текст усыпили всех наших журналистов.
'''


def generate(context):
    return TaskStatement(TITLE, STATEMENT)
