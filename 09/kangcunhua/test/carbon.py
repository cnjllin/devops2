#!?usr/bin/python
# coding:utf-8
"""Summary:通过socket创建metric
"""
import socket
import time
import errno


class CarbonClient(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._carbon = None
        self._connected = False

    def connect(self):
        if not self._connected:
            self._connect()

    def _connect(self):
        """
            连接host port
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while 1:
            try:
                sock.connect((self._host, self._port))
            except socket.error as e:
                if e.errno == errno.EINTR:
                    continue
                else:
                    raise e
            break
        self._carbon = sock
        self._connected = True

    def close(self):
        if self._connected:
            self._carbon.close()
            self._connected = False

    def send(self, metrics):
        chunk_start, chunk_end = 0, 20
        while 1:
            payload = []
            metric_chunk = metrics[chunk_start: chunk_end]
            if not metric_chunk:
                break
            now = int(time.time())
            print now
            for metric in metric_chunk:
                if len(metric) == 2:
                    payload.append("{} {} {}\n".format(metric[0], metric[1], now))
                elif len(metric) == 3:
                    payload.append("{} {} {}\n".format(metric[0], metric[1], metric[2]))
            self._carbon.sendall("".join(payload))
            chunk_start, chunk_end = chunk_end, chunk_end + 20

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exec_type, exec_value, exc_tb):
        self.close()
        return exec_value is None


class RebooCarbonClient(CarbonClient):
    REBOOT_CARBON_ADDR = ("192.168.99.15", 2003)

    def __init__(self):
        super(RebooCarbonClient, self).__init__(*self.REBOOT_CARBON_ADDR)


if __name__ == "__main__":

    with RebooCarbonClient() as client:
        client.send([("test1.aa", 40)])
        client.send([("test1.aa", 40)])
