# создаю декоратор для логирование
def logger_dec(func):
    def wrapper(*args, **kwargs):
        print("Log: start")
        result = func(*args, **kwargs)
        print("Log: end")
        return result
    return wrapper

# создаю декоратор для admin page
def admin_dec(func):
    def wrapper(*args, **kwargs):
        print("Admin page render start")
        result = func(*args, **kwargs)
        print("Admin page render end")
        return result
    return wrapper

class AuthRequiredMixin:
    def auth_render(self, auth_status: bool = False) -> bool:
        
        """
        метод проверяет авторизацию пользователя.
        принимает булево значение и если True, то возвращает True и печатает "Auth Ok".
        иначе печатает "Access denied" и возвращает False
        """

        if auth_status:
            print("Auth Ok")
            return True
        else:
            print("Access denied")
            return False

class BaseView(AuthRequiredMixin):
    def render(self, auth_status: bool = False):
        
        """
        метод рендерит страницу, если пользователь авторизован.
        если пользователь не авторизован, то страница не рендерится.
        """

        if self.auth_render(auth_status):
            print("Template render")
        else:
            pass

class LogginMixin(BaseView):
    @logger_dec
    def render(self, auth_status: bool = False):
        """метод логирует рендер страницы"""
        super().render(auth_status)

class AdminPageView(LogginMixin, BaseView):
    @admin_dec
    def render(self, auth_status: bool = False):
        """метод рендерит админ страницу, если пользователь авторизован"""
        super().render(auth_status)

admin_page = AdminPageView()
# print(admin_page.__class__.__mro__) # для проверки method resolution order
admin_page.render(auth_status=True)  # по умолчанию пользователь не зарегистрирован, вставьте auth_status=True, чтобы проверить авторизацию