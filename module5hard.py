class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)  # Хэш пароля
        self.age = age

    def check_login(self, nickname, password):
        return self.nickname == nickname and self.password == hash(password)

    def __str__(self):
        return f"{self.nickname}: {self.age}"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return f"{self.title}: {self.duration}sec, adult mode={self.adult_mode}"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.check_login(nickname, password):
                self.current_user = user
                break
        else:
            print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add_video(self, video):
        if any(vid.title == video.title for vid in self.videos):
            print("Видео с таким названием уже существует")
        else:
            self.videos.append(video)

    def get_videos(self, search_word):
        result = [vid.title for vid in self.videos if search_word.lower() in vid.title.lower()]
        return result

    def watch_video(self, title):
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    from time import sleep
                    while video.time_now < video.duration:
                        print(video.time_now)
                        sleep(1)
                        video.time_now += 1
                    print("Конец видео")
                    video.time_now = 0
                break
        else:
            print("Видео не найдено")


if __name__ == "__main__":
    ur_tube = UrTube()

    # Пример регистрации
    ur_tube.register("admin", "password", 30)
    ur_tube.register("user1", "password1", 20)
    ur_tube.register("user2", "password2", 18)

    # Пример входа
    ur_tube.log_in("admin", "password")
    ur_tube.log_in("user1", "password1")
    ur_tube.log_in("user2", "password2")

    # Пример добавления видео
    ur_tube.add_video(Video("Видео 1", 60, True))
    ur_tube.add_video(Video("Видео 2", 30))
    ur_tube.add_video(Video("Видео 3", 45, False))

    # Пример поиска видео
    titles = ur_tube.get_videos("видео")
    print(titles)

    # Пример просмотра видео
    ur_tube.watch_video("Видео 2")
    ur_tube.watch_video("Видео 3")
    ur_tube.watch_video("Несуществующее видео")

    # Пример выхода
    ur_tube.log_out()
    ur_tube.log_out()
    ur_tube.log_out()

    # Тестовый вход после выхода
    ur_tube.log_in("admin", "password")
    ur_tube.log_in("user1", "password1")
    ur_tube.log_in("user2", "password2")

    # Проверка наличия ограничений
    ur_tube.watch_video("Видео 1")
    ur_tube.watch_video("Видео 3")
    ur_tube.watch_video("Видео 1")

    # Очистка текущего времени просмотра
    ur_tube.watch_video("Видео 1")
    ur_tube.watch_video("Видео 3")
    ur_tube.watch_video("Видео 1")

    # Проверка отсутствия входа
    ur_tube.watch_video("Видео 1")
    ur_tube.watch_video("Видео 3")
    ur_tube.watch_video("Видео 1")

    # Еще один тестовый вход
    ur_tube.log_in("admin", "password")
    ur_tube.log_in("user1", "password1")
    ur_tube.log_in("user2", "password2")

    # Еще одна проверка наличия ограничений
    ur_tube.watch_video("Видео 1")
    ur_tube.watch_video("Видео 3")
    ur_tube.watch_video("Видео 1")

    # Очистка текущего времени просмотра
    ur_tube.watch_video("Видео 1")
    ur_tube.watch_video("Видео 3")
    ur_tube.watch_video("Видео 1")