import sys

from src.iapp import app

orders = [
    'runserver'
]


def main():
    """
    运行的主要函数。
    """
    para = sys.argv
    if not para:
        raise ValueError('Program need order.')
    if para[0] not in orders:
        raise ValueError('Wrong order.')
    if para[0] == 'runserver':
        _host, _port = ('127.0.0.1', 8000)
        try:
            _host, _port = para[1].split(':')
        except Exception:
            raise Exception('Wrong host or port.')
        app.run(
            host=_host,
            port=_port,
        )


if __name__ == '__main__':
    main()
