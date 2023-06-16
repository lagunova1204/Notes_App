"""Модуль реализующий класс CommandRemove (удаление заметки)"""
from view.commands.command_abstract import Command


class CommandRemove(Command):
    """Класс реализует удаление заметки"""

    def __init__(self, console):
        self.console = console

    @property
    def description(self):
        """Возвращает описание команды"""
        return "Удалить заметку"

    def execute(self):
        """Запускает метод удаления заметки"""
        self.console.remove_note()