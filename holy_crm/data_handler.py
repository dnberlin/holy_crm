import logging
import pandas as pd
from datetime import datetime,  timedelta

class DataHandler:
    __data_path = "data"
    __log__ = logging.getLogger('holy_crm')

    def __init__(self, config):
        self.mode = config.get('mode')
        self.__log__.debug(F'Using {self.mode} mode')
        if self.mode == 'local':
            self.input_file = config.get('input_filename')
            self.__log__.debug(F'Input file: {self.input_file}')

    def get_dict_data(self):
        self.__log__.info('Importing data')
        if self.mode == 'local':
            self.df = self.__import_data_to_df(str(self.input_file))
            return self.__convert_df_to_dict(self.df)
        return data

    def update_entry(self, id):
        self.__log__.debug(F'Updating Customer {id}')
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #self.__log__.debug("\n\n" + str(now))
        self.df.at[id, 'last_contact'] = now
        #self.__log__.debug(self.df.loc[id])

    def save_data(self):
        file = self.__data_path + "/" + self.input_file  
        self.__log__.info('Saving data')
        self.df.to_excel(file, index=False)

    def __convert_df_to_dict(self, df):
        return df.to_dict('records')
    
    def __correct_df(self, df):
        # Fill Nan to ''
        return df.fillna('')

    def __import_data_to_df(self, xlsx_filename):
        file = self.__data_path + "/" + xlsx_filename
        self.__log__.debug(F"Importing {file} as datasource")
        return self.__correct_df(pd.read_excel(file))
