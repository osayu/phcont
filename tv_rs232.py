import argparse

from serial import Serial


class TV(Serial):
    command_map = {
        "POWER-GET": [0x19],
        "POWER-OFF": [0x18, 0x01],
        "POWER-ON": [0x18, 0x02],
        "INPUT-GET": [0xad],
        "INPUT-VGA": [0xac, 0x05, 0x00, 0x01, 0x00],
        "INPUT-HDMI": [0xac, 0x06, 0x02, 0x01, 0x00],
        "INPUT-MHDMI": [0xac, 0x06, 0x03, 0x01, 0x00],
        "INPUT-DP": [0xac, 0x09, 0x04, 0x01, 0x00],
        "INPUT-MDP": [0xac, 0x09, 0x05, 0x01, 0x00],
        "PIC-NORM": [0x3a, 0x00],
        "PIC-CUST": [0x3a, 0x01],
        "PIC-REAL": [0x3a, 0x02],
        "PIC-FULL": [0x3a, 0x03],
        "PIC-21-9": [0x3a, 0x04],
        "PIC-DYN": [0x3a, 0x05],
        "PIP-GET": [0x3d],
        "PIP-OFF": [0x3c, 0x00, 0x00, 0x00, 0x00],
        "PIP-BL": [0x3c, 0x01, 0x00, 0x00, 0x00],
        "PIP-TL": [0x3c, 0x01, 0x01, 0x00, 0x00],
        "PIP-TR": [0x3c, 0x01, 0x02, 0x00, 0x00],
        "PIP-BR": [0x3c, 0x01, 0x03, 0x00, 0x00],
        "PIP-OT": [0x3c, 0x01, 0x04, 0x00, 0x00],
        "PIP-S-GET": [0x85],
        "PIP-S-VGA": [0x84, 0xfd, 0x00, 0x02, 0x02],
        "PIP-S-HDMI": [0x84, 0xfd, 0x02, 0x02, 0x02],
        "PIP-S-MHDMI": [0x84, 0xfd, 0x03, 0x02, 0x02],
        "PIP-S-DP": [0x84, 0xfd, 0x04, 0x02, 0x02],
        "PIP-S-MDP": [0x84, 0xfd, 0x05, 0x02, 0x02],
        "PIP-M-2": [0xfb, 0x01, 0x02],
        "VOL0": [0x44, 0x00],
        "VOL10": [0x44, 0x0A],
        "VOL20": [0x44, 0x14],
        "VOL30": [0x44, 0x1e],
        "VOL40": [0x44, 0x28],
        "VOL50": [0x44, 0x32],
        "VOL60": [0x44, 0x3c],
        "VOL70": [0x44, 0x46],
        "VOL80": [0x44, 0x50],
        "VOL90": [0x44, 0x5a],
        "VOL100": [0x44, 0x64],
    }

    def __init__(self, timeout=0.1):  # timeout=0.05
        super(TV, self).__init__(r"/dev/ttyUSB0", timeout=timeout)

    def _send(self, data):
        buf = bytearray(data)
        buf.insert(0, 0xa6)  # header
        buf.insert(1, 0x01)  # id
        buf.insert(2, 0x00)  # category
        buf.insert(3, 0x00)  # page
        buf.insert(4, 0x00)  # function
        buf.insert(5, len(buf) - 3)  # length
        buf.insert(6, 0x01)  # control
        buf.append(reduce(lambda a, b: a ^ b, buf))  # checksum
        self.write(buf)
        rep = self.read(40)
        result = rep[6:-1]
        return result

    def command(self, cmd):
        return self._send(self.command_map[cmd])


def main():
    parser = argparse.ArgumentParser(description='Control philips BDM40.')
    parser.add_argument('command', help='command')

    args = parser.parse_args()
    if args.command not in TV.command_map:
        print "unknown command"
        return

    tv = TV()
    tv.command(args.command)


if __name__ == '__main__':
    main()
