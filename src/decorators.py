def log(filename=None):
    """
      Декоратор для логирования выполнения функций.

      Параметры:
      filename (str, optional): Путь к файлу для записи логов.
          Если не указан, логи выводятся в консоль.

      Возвращает:
      function: Декоратор, который оборачивает целевую функцию

      Описание:
      Декоратор добавляет логирование к любой функции. При успешном выполнении
      функции записывает сообщение об успехе, при возникновении исключения -
      информацию об ошибке.

      Логирование может производиться как в консоль (по умолчанию), так и в файл.
      В случае записи в файл используется режим добавления (append).

      Пример использования:

      @log('app.log')
      def my_function(arg1, arg2):
          return arg1 + arg2

      @log()  # Логирование в консоль
      def another_function():
          return "Hello, world!"
      """
    def log_decorator(function):
        """
               Внутренний декоратор, оборачивающий целевую функцию.

               Параметры:
               function (callable): Функция, которую нужно декорировать

               Возвращает:
               function: Обёрнутую функцию с логированием
               """
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = function(*args, **kwargs)
                message = f"{function.__name__} ok"
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)
                return result
            except Exception as e:
                message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {{}}"
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message)

            return result

        return wrapper

    return log_decorator