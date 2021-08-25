import pytest
import time

timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def main():
    pytest.main(['-v', '--html=report/report-{}.html'.format(timestr)])


if __name__ == '__main__':
    main()
