""" Esta clase guarda cookies una sola vez, las reutiliza en cualquier test y vive en memoria. Mientras haya un logil global.
aplicado a un login auténtico con roles (alumno / docente / admin)"""

# NO ESTA ENCHUFADO AÚN

class SessionManager:
    _cookies = None

    @classmethod
    def save_cookies(cls, driver):
        cls._cookies = driver.get_cookies()

    @classmethod
    def load_cookies(cls, driver):
        if not cls._cookies:
            return

        for cookie in cls._cookies:
            driver.add_cookie(cookie)

