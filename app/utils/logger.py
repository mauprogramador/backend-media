from app.models import TraceLog
import os
import sys


class Logger:
    METHOD = {
        "GET": "\033[94mGET\033[m",
        "POST": "\033[92mPOST\033[m",
        "PUT": "\033[93mPUT\033[m",
        "PATCH": "\033[96mPATCH\033[m",
        "DELETE": "\033[91mDELETE\033[m"
    }

    @classmethod
    def log(cls, type: str, message: str):
        log_type = f"\033[93m[{type}\033[93m]:"
        print(f"{log_type: <24}\033[m {message}")

    @classmethod
    def info(cls, message: str):
        cls.log("\033[92mINFO", message)

    @classmethod
    def error(cls, message: str):
        cls.log("\033[91mERROR", message)

    @classmethod
    def exception(cls, exception: Exception):
        exception_type, exception_value, exception_traceback = sys.exc_info()
        exception_name = getattr(exception_type, "__name__", "Exception")

        log_type = "\033[91mEXCEPTION"
        log_exception = f"<{exception_name}({exception.args}): {exception_value}>"
        cls.log(log_type, f"Unexpected Error {log_exception}")

        if exception_traceback is not None:
            fname = os.path.split(exception_traceback.tb_frame.f_code.co_filename)
            cls.log(log_type, f"Unexpected Error {exception_type} {fname} {exception_traceback.tb_lineno}")

    @classmethod
    def middleware(cls, data: TraceLog):
        point = "\033[95m\u2022\033[m"
        log_url = f"{cls.METHOD[data.method]: <6} {point} http://{data.host}:{data.port}{data.url}"
        status_color = 32 if data.status_code in (200, 201) else 31
        log_status = f"\033[{status_color}m{data.status_code} {data.status_phrase}"
        log_message = f"{log_url} {point} {log_status} \033[93m{data.process_time}ms\033[m"
        cls.log("\033[95mTRACE", log_message)

    @classmethod
    def service(cls, url: str, status_code: str, status_phrase: str, process_time: str):
        point = "\033[95m\u2022\033[m"
        log_url = f"{cls.METHOD['POST']: <6} {point} {url}"
        status_color = 32 if status_code in (200, 201) else 31
        log_status = f"\033[{status_color}m{status_code} {status_phrase}"
        log_message = f"{log_url} {point} {log_status} \033[93m{process_time}ms\033[m"
        cls.log("\033[95mSERVICE", log_message)
