from pydantic import BaseModel


class TraceLog(BaseModel):
    host: str
    port: int
    method: str
    url: str
    status_code: int
    status_phrase: str
    process_time: str

    @staticmethod
    def make(
        host: str,
        port: int,
        method: str,
        url: str,
        status_code: int,
        status_phrase: str,
        process_time: str
    ):
        return TraceLog(
            host=host,
            port=port,
            method=method,
            url=url,
            status_code=status_code,
            status_phrase=status_phrase,
            process_time=process_time
        )
