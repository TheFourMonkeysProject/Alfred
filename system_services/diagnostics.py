__author__ = 'matt.livingston'
import psutil



class AlfredDiagnostics:

    def get_cpu_count(self):
        return psutil.cpu_count()

    def get_virtual_memory(self):
        values = psutil.virtual_memory()
        return self.get_human_readable_size(values.total)

    def get_disk_usage(self):
        values = psutil.disk_usage('/')
        return self.get_human_readable_size(values.total)

    def get_human_readable_size(self, num):
        exp_str = [ (0, 'B'), (10, 'KB'),(20, 'MB'),(30, 'GB'),(40, 'TB'), (50, 'PB'),]
        i = 0
        while i+1 < len(exp_str) and num >= (2 ** exp_str[i+1][0]):
            i += 1
            rounded_val = round(float(num) / 2 ** exp_str[i][0], 2)

        return '%s %s' % (int(rounded_val), exp_str[i][1])