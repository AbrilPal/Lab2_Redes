# AJPoulter-Soton. (2019). Obtenido de: https://gist.github.com/AJPoulter-Soton/9d0d2505af64f0719bdee59b9a4533ba

class Deteccion():
    def fletcher32(self, data, length):
        w_len = length
        c0 = 0
        c1 = 0
        x = 0

        while w_len >= 360:
            for i in range (360):
                c0 = c0 + ord(data[x])
                c1 = c1 + c0
                x = x + 1
            c0 = c0 % 65535
            c1 = c1 % 65535
            w_len = w_len - 360
        
        for i in range (w_len):
            c0 = c0 + ord(data[x])
            c1 = c1 + c0
            x = x + 1
        c0 = c0 % 65535
        c1 = c1 % 65535
        return (c1 << 16 | c0)