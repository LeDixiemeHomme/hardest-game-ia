import logging

from project.constants import constants


class Logger:
    def __init__(self, name: str, log_file_name: str = 'default_log_file'):
        self._name = name
        self._log_file_name = constants.BASE_PATH + 'logs/' + log_file_name + '.log'
        self._format = logging.Formatter("%(asctime)s | %(levelname)s (at) %(name)s : %(message)s")
        # self._file_log = self._init_file_log()
        self._stdout_log = self._init_stdout_log()

    # def _init_file_log(self):
    #     my_logs_file = logging.getLogger(self._name)
    #     my_logs_file.setLevel(logging.DEBUG)
    #
    #     file = logging.FileHandler(self._log_file_name)
    #     file.setFormatter(self._format)
    #     my_logs_file.addHandler(file)
    #     return my_logs_file

    def _init_stdout_log(self):
        my_logs_stdout = logging.getLogger(self._name)
        my_logs_stdout.setLevel(logging.DEBUG)

        stream = logging.StreamHandler()
        stream.setFormatter(self._format)
        my_logs_stdout.addHandler(stream)
        return my_logs_stdout

    # @property
    # def file_log(self):
    #     return self._file_log

    @property
    def stdout_log(self):
        return self._stdout_log
