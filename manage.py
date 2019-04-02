import sys

from src.iapp import app

orders = [
    'runserver'
]


def run_server():
    """
    运行的主要函数。
    """
    para = sys.argv
    print(para)
    if not para:
        raise ValueError('Program need order.')
    if para[1] not in orders:
        raise ValueError('Wrong order.')
    if para[1] == 'runserver':
        _host, _port = ('127.0.0.1', 8000)
        try:
            _host, _port = para[2].split(':')
        except Exception:
            raise Exception('Wrong host or port.')
        app.run(
            host=_host,
            port=_port,
        )


if __name__ == '__main__':
    run_server()
