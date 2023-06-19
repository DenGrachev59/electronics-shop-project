# # Множественное наследование. Домашнее задание
#
# ## Описание задачи
#
# - Создайте класс `Keyboard` для товара “клавиатура”.
#
# > Товар отличается от `Item` тем, что у него есть атрибут `language` и метод для изменения языка (раскладки клавиатуры).
#
# - Реализуйте дополнительный функционал по хранению и изменению раскладки клавиатуры в отдельном классе-миксине, который “подмешивается” в цепочку наследования класса `Keyboard`.
#
# > Язык по умолчанию (при инициализации) - английский (`EN`). Всего поддерживается два языка: `EN` и `RU`.
# > Изменить язык можно только методом `change_lang()`.
#
# Тестирование:
# - Напишите тесты для класса `Keyboard`
#
# ## Ожидаемое поведение
# - Код в файле `main.py` должен выдавать ожидаемые значения
from src.item import Item


class MixinLanguage:
    LANGUAGE = 'EN'

    def __init__(self):
        self.__language = self.LANGUAGE
        # MixinLanguage.LANGUAGE = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang != 'EN' and lang != 'RU':
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        self.__language = lang


class KeyBoard(Item, MixinLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
