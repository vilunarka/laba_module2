from typing import Any


class SocialNetwork:
    """
    Базовый класс для представления социальной сети.

    Атрибуты:
        name (str): Название социальной сети.
        users (dict[str, Any]): Словарь пользователей, где ключом является имя пользователя, а значением -
            его данные.
        posts (list[dict[str, Any]]): Список постов в социальной сети, каждый пост представляет собой словарь.
    """

    def __init__(self, name: str) -> None:
        """
        Конструктор базового класса.

        Args:
            name (str): Название социальной сети.
        """
        self.name: str = name
        self.users: dict[str, Any] = {}
        self.posts: list[dict[str, Any]] = []

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта социальной сети.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Social Network: {self.name} with {len(self.users)} users and {len(self.posts)} posts"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.__class__.__name__}(name='{self.name}')"

    def add_user(self, username: str, user_data: dict[str, Any]) -> None:
        """
        Добавляет пользователя в социальную сеть.

        Args:
            username (str): Имя пользователя.
            user_data (dict[str, Any]): Данные пользователя.
        """
        self.users[username] = user_data

    def add_post(self, post_data: dict[str, Any]) -> None:
        """
        Добавляет пост в социальную сеть.

          Args:
            post_data (dict[str, Any]): Данные поста.
          """
        self.posts.append(post_data)


class VK(SocialNetwork):
    """
    Класс для представления социальной сети VK, наследуется от SocialNetwork.

    Атрибуты:
        name (str): Название социальной сети (установлено как "VK").
        groups (dict[str, Any]): Словарь групп в VK, где ключом является название группы, а значением - ее
            данные.
    """

    def __init__(self) -> None:
        """
        Конструктор дочернего класса VK. Наследует конструктор родителя и добавляет новые атрибуты.
        """
        super().__init__(name="VK")
        self.groups: dict[str, Any] = {}

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для вывода информации о VK.
        """
        return f"VK Network with {len(self.users)} users, {len(self.groups)} groups, and {len(self.posts)} posts"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для представления объекта VK.
        """
        return f"{self.__class__.__name__}()"

    def add_group(self, group_name: str, group_data: dict[str, Any]) -> None:
        """
        Добавляет группу в VK.

        Args:
            group_name (str): Название группы.
            group_data (dict[str, Any]): Данные группы.
        """
        self.groups[group_name] = group_data

    def share_post(self, post_data: dict[str, Any]) -> None:
        """
        Перегруженный метод для добавления поста в VK.
        В VK посты добавляются не в общий список, а в ленту группы или пользователя
        Args:
            post_data (dict[str, Any]): Данные поста.
        """
        self.posts.append(post_data)

    def find_user(self, username: str) -> Any:
        """
        Наследует метод add_user из базового класса и перегружает.
        Добавляет пользователя в социальную сеть.

          Args:
            username (str): Имя пользователя.

          Returns:
            dict[str, Any] | None: Данные пользователя, если он найден, или None, если не найден.

        """
        return self.users.get(username)


class Facebook(SocialNetwork):
    """
     Класс для представления социальной сети Facebook, наследуется от SocialNetwork.

    Атрибуты:
        name (str): Название социальной сети (установлено как "Facebook").
        pages (dict[str, Any]): Словарь страниц в Facebook, где ключом является название страницы, а значением - ее
            данные.
        _privacy_settings (dict[str, Any]): Непубличный атрибут для хранения настроек приватности пользователей.
            Инкапсуляция необходима, так как не все пользователи должны иметь возможность просматривать
            данные о приватности.
    """

    def __init__(self) -> None:
        """
        Конструктор дочернего класса Facebook. Наследует конструктор родителя и добавляет новые атрибуты.
        """
        super().__init__(name="Facebook")
        self.pages: dict[str, Any] = {}
        self._privacy_settings: dict[str, Any] = {}

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для вывода информации о Facebook.
        """
        return f"Facebook Network with {len(self.users)} users, {len(self.pages)} pages, and {len(self.posts)} posts"

    def __repr__(self) -> str:
        """
         Перегрузка метода __repr__ для представления объекта Facebook.
         """
        return f"{self.__class__.__name__}()"

    def add_page(self, page_name: str, page_data: dict[str, Any]) -> None:
        """
        Добавляет страницу в Facebook.

          Args:
            page_name (str): Название страницы.
            page_data (dict[str, Any]): Данные страницы.
          """
        self.pages[page_name] = page_data

    def set_privacy_settings(self, username: str, settings: dict[str, Any]) -> None:
        """
        Устанавливает настройки приватности для пользователя.

         Args:
          username (str): Имя пользователя.
          settings (dict[str, Any]): Настройки приватности пользователя.
         """
        self._privacy_settings[username] = settings

    def get_privacy_settings(self, username: str) -> dict[str, Any]:
        """
         Получает настройки приватности для пользователя.
          Инкапсуляция необходима для защиты доступа к данным о приватности.
          Args:
             username (str): Имя пользователя.

          Returns:
             dict[str, Any]: Настройки приватности пользователя.
          """
        return self._privacy_settings.get(username, {})

    def add_post(self, post_data: dict[str, Any]) -> None:
        """
        Перегруженный метод для добавления поста в Facebook.
        В Facebook посты добавляются с учетом приватности и настроек пользователей
          Args:
            post_data (dict[str, Any]): Данные поста.
        """
        self.posts.append(post_data)


if __name__ == '__main__':
    # Пример использования

    vk_network = VK()
    vk_network.add_user("ivanov", {"name": "Ivan", "age": 30})
    vk_network.add_group("programming_club", {"description": "Discussion about programming"})
    vk_network.add_post({"author": "ivanov", "text": "Hello, VK!"})
    print(vk_network)
    print(repr(vk_network))
    print(vk_network.find_user("ivanov"))
    print(vk_network.find_user("petrov"))

    fb_network = Facebook()
    fb_network.add_user("petrova", {"name": "Anna", "city": "Moscow"})
    fb_network.add_page("tech_blog", {"description": "Interesting articles about tech"})
    fb_network.add_post({"author": "petrova", "text": "Hello, Facebook!"})
    fb_network.set_privacy_settings("petrova", {"posts": "friends_only"})
    print(fb_network)
    print(repr(fb_network))
    print(fb_network.get_privacy_settings("petrova"))
    print(fb_network.get_privacy_settings("sidorov"))

    base_network = SocialNetwork("BaseNetwork")
    print(base_network)
    print(repr(base_network))
