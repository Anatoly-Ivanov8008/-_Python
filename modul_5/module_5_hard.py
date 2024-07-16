""""
Модуль 5 задача 5
Дополнительное практическое задание по модулю: "Классы и объекты."
Задание "Свой YouTube"
"""
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in range(0, len(self.users), 3):
            if self.users[i] == nickname and hash(self.users[i + 1]) == hash(password):
                self.current_user = self.users[i]

    def register(self, nickname, password, age):
        if len(self.users) < 2:
            self.users.append(nickname)
            self.users.append(password)
            self.users.append(age)
            self.current_user = nickname
        else:
            for i in range(0, len(self.users), 3):
                if self.users[i] == nickname:
                    print(f'Пользователь {nickname} уже существует')
                    break
                else:
                    self.users.append(nickname)
                    self.users.append(password)
                    self.users.append(age)
                    self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        buffer = [args]
        for i in buffer:
            for j in i:
                if j.title not in self.videos:
                    self.videos.append(j.title)
                    self.videos.append(j.duration)
                    self.videos.append(j.time_now)
                    self.videos.append(j.adult_mode)

    def get_videos(self, word):
        found_videos = []
        for i in range(0, len(self.videos), 4):
            a = self.videos[i]
            if word.lower() in a.lower():
                found_videos.append(a)
        return found_videos

    def watch_video(self, title):
        age = 0
        import time
        if self.current_user != None:
            for i in range(0, len(self.users), 3):
                if self.users[i] == self.current_user:
                    age = self.users[i + 2]
                    break
            for i in range(0, len(self.videos), 4):
                if title == self.videos[i]:
                    if age < 18 and self.videos[i + 3] == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                    else:
                        for j in range(1, self.videos[i + 1] + 1):
                            print(j, ' ', end='')
                            time.sleep(1)
                        print('Конец видео')
        else:
            print('Войдите в аккаунт чтобы смотреть видео.')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
