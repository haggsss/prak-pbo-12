# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:01:21 2024

@author: kusfi
"""
import datetime
import pytz

def my_decorator(inner):
    def inner_decorator():
        print("===================================")
        print("Syahrul Arifin")
        print("064002300032")
        print("===================================")
        # Mendapatkan waktu UTC
        utc_now = datetime.datetime.now(pytz.utc)
        # Mengubah waktu UTC menjadi UTC+7 (Jakarta Time)
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_now = utc_now.astimezone(jakarta_tz)

        # Menampilkan waktu sebelum menjalankan fungsi
        print("Timezone:", jakarta_tz.zone)
        print("Tanggal:", jakarta_now.strftime('%Y-%m-%d'))
        print("Waktu:", jakarta_now.strftime('%H:%M:%S.%f'))
        print()

        # Memanggil fungsi yang dihias
        inner()

        # Mendapatkan waktu UTC lagi setelah pemanggilan fungsi
        utc_now = datetime.datetime.now(pytz.utc)
        jakarta_now = utc_now.astimezone(jakarta_tz)

        # Menampilkan waktu setelah menjalankan fungsi
        print()
        print("Tanggal:", jakarta_now.strftime('%Y-%m-%d'))
        print("Waktu:", jakarta_now.strftime('%H:%M:%S.%f'))

    return inner_decorator

@my_decorator
def decorated():
    print("Berubah Menjadi")

if __name__ == "__main__":
    decorated()
