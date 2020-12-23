import logging
import pprint
from datetime import datetime, timedelta

class CustomerSelector:

    __log__ = logging.getLogger('holy-crm')

    def __init__(self, config, data):
        self.config = config
        self.data = data

    def select_customer(self, criteria):
        preselected_data = self.__preselect()
        final_selection = []

        if criteria == []:
            return preselected_data

        country_selection = self.__select_by_country(preselected_data, criteria)
        time_selection = self.__select_by_time(preselected_data, criteria)

        for record in country_selection:
            if record in country_selection and record in time_selection:
                final_selection.append(record)

        if len(final_selection) > 0:
            self.__log__.info(F"Found {len(final_selection)} customer from {criteria.get('country')}")
        else:
            self.__log__.warning(F"No customer found for selection country = {criteria.get('country')}. Please specify different criteria.")
        
        return final_selection

    def __preselect(self):
        selection = []
        for record in self.data:
            if record['person_first_name'] and \
            record['person_last_name'] and \
            record['person_email_address'] and \
            record['company_name']:
                selection.append(record)
            else:
                self.__log__.warning(F"Skipping customer {record['id']} due to missing email, first-, lastname or company name.")
        return selection

    def __select_by_country(self, data, criteria):
        selection = []
        # Country selection:
        for country in criteria.get('country'):
            self.__log__.info(F"Finding customer from {country}")
            for record in data:
                if record['country'].strip() == country:
                    selection.append(record)
        return selection


    def __select_by_time(self, data, criteria):
        selection = []
        for record in data:
            if not record['last_contact']:
                print("[*] Time empty")
                selection.append(record)
            elif (datetime.now() - timedelta(days=30)) > datetime.strptime(record['last_contact'], "%Y-%m-%d %H:%M:%S"):
                selection.append(record)
                print(F"[*] daytime-now {datetime.now()}\n Now - 30 days {datetime.now() - timedelta(days=30)}\n {datetime.strptime(record['last_contact'], '%Y-%m-%d %H:%M:%S')}")
        return selection


