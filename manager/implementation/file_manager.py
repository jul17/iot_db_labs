import view_data_interfaces.view_data as show_data
import urllib.request
import manager.process_data_interface as process_data_interface
import redis_data as redis
import time
import json
import csv

load_message = "LOADING... "
complete_message = "COMPLETED"
rows_message = "ROWS"  
redis_client = redis.Redis

class FileManager(process_data_interface.ProcessData):
    show_data_method = show_data.ViewDataInterface

    def process_data(self, show_data_method):
        file_name =self.split("/")[-1]
        file_status = file_name + '_' + 'status'
        file = "expenses_2.csv"


        if not redis_client.get_data(file_status) or redis_client.get_decode_data(file_status) != complete_message:
            print("No file in Azure Cache")
            print(load_message)

            redis_client.set_data('file_name', file_name)
            redis_client.show_data('file_name')
            redis_client.set_data('date', time.asctime())
            redis_client.show_data('date')

            data = urllib.request.urlopen(self)

            end_indx = 0
            start_indx = 0
            data_to_json = {}
            list_json = list()
            try:
                for item in data:
                    show_data_method.view_data(item.decode())
                    if (end_indx == 100 + start_indx):
                        redis_client.set_data(rows_message, "From file:{} Lines: {} - {} ".format(file_name, str(start_indx), str(end_indx)))
                        redis_client.show_data(rows_message)
                        start_indx = end_indx
                    end_indx += 1
                redis_client.set_data(file_status, complete_message)
                redis_client.show_data(file_status)
                return True
            except ValueError as e:
                print ("ValueError: " + str(e))
                can_add = False
        else:
            redis_client.set_data(file_status, "Trying to re-fill file")
            redis_client.show_data(file_status)

                
