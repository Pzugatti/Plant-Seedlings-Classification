from datetime import datetime
import numpy as np
import zipfile
from shutil import unpack_archive
import os

class tools:

    @staticmethod
    def start_end_timer(start_time=None):
        if not start_time:
            start_time = datetime.now()
            return start_time
        elif start_time:
            thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
            tmin, tsec = divmod(temp_sec, 60)
            print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))

    @staticmethod
    def data_size(data,format = 'B'):
        if not isinstance(data,np.ndarray):
            raise TypeError('It is not an array !')

        if format == 'B':
            format_bytes = 1
        elif format == 'MB':
            format_bytes = 2**20 # 1 Megabyte is 1,048,576 bytes
        elif format == 'GB':
            format_bytes = 2**30 # 1 Gigabyte is 1,073,741,824 bytes
        else:
            raise Exception('choose B, MB & GB only !')


        total = data.nbytes/format_bytes
        return '{:.2f} {}'.format(total,format)


    @staticmethod
    def check_zip_file(dir_zip):
        with zipfile.ZipFile(dir_zip) as z:
          for filename in z.namelist():
                  print(filename)

    @staticmethod
    def unpack_zip_file(dir_zip,des_dir):
        for zdir in dir_zip:
          unpack_archive(zdir,des_dir)
