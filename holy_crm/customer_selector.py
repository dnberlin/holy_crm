import logging
import pprint
from datetime import datetime, timedelta

class CustomerSelector:

    __log__ = logging.getLogger('holy_crm')

    def __init__(self, config, data):
        self.config = config
        self.data = data
        self.selection = self.__select_customer()

    def get_customer(self):
        if len(self.selection) > 0:
            return self.selection.pop()
        else:
            return False

    def __select_customer(self):
        # Preselect customer
        preselected_data = self.__preselect()
        final_selection = []

        self.__log__.debug(F"Critieria loaded from config-file: {self.config.get('criteria')}") 
        if self.config.get('criteria') is not None:
            self.__log__.info('Selecting customer using criteria')
            criteria = self.config.get('criteria', dict())
        else:
            self.__log__.info('No cirteria defined. Using all customer.')
            return preselected_data

        # Select by language and company type
        language_type_selection = self.__select_by_language_type(preselected_data, criteria)
        final_selection = self.__select_by_time(language_type_selection, criteria)

        # Document results after selection
        if len(final_selection) > 0:
        	self.__log__.info(F"Found {len(final_selection)} companies with type {criteria.get('company_type')} speaking {criteria.get('language')} ")
        else:
            self.__log__.warning(F"No company found for selection type = {criteria.get('company_type')} and language = {criteria.get('language')}. Please specify different criteria.")
        
        return final_selection

    def __preselect(self):
        selection = []
        for record in self.data:
            if (record['person_first_name'] and \
            record['person_last_name'] and \
            (record['person_email'] or record['company_email']) and \
            record['company_name'] and \
            record['person_language']):
                selection.append(record)
            else:
                self.__log__.warning(F"Skipping customer {record['id']} due to missing language, email, first-, lastname or company name.")
        return selection

    def __select_by_country(self, data, criteria):
        selection = []
        # Country selection
        for country in criteria.get('country'):
            self.__log__.info(F"Finding customer from {country}")
            for record in data:
                if record['country'].strip() == country:
                    selection.append(record)
        return selection

    def __select_by_language_type(self, data, criteria):
        selection = []
        company_type = criteria.get('company_type')
        self.__log__.info(F"Finding customer by company_type: {company_type}")
        # Language/ topic selection 
        for language in criteria.get('language'):
            self.__log__.info(F"Finding customer speaking {language}")
            for record in data:
                #self.__log__.info(F" Record spreaks {record['person_language']} has topic {record['company_type']}.")
                if record['person_language'].strip() == language and record['company_type'].strip() == company_type:
                    selection.append(record)
        return selection

    def __select_by_time(self, data, criteria):
        selection = []
        self.__log__.info(F"Customer shall be contacted every {self.config.get('contact_intervall')} days")
        for record in data:
            # Customer that has never contacted before shall be contacted
            if not record['last_contact']:
                self.__log__.info(F"Customer {record['id']} was never contacted before.")
                record['contact_string'] = F"Customer {record['id']} was never contacted before."
                selection.append(record)
            # Customer that has been contacted more than a defined time age shall be contacted
            elif (datetime.now() - timedelta(days=self.config.get('contact_intervall'))) > datetime.strptime(record['last_contact'], "%Y-%m-%d %H:%M:%S"):
                self.__log__.info(F"Customer {record['id']} was contacted on {record['last_contact']}. " \
                F"That\'s {datetime.now() - datetime.strptime(record['last_contact'], '%Y-%m-%d %H:%M:%S')} ago. It\'s time to send a new message.")
                record['contact_string'] = F"Customer {record['id']} was contacted on {record['last_contact']}. " \
                F"That\'s {datetime.now() - datetime.strptime(record['last_contact'], '%Y-%m-%d %H:%M:%S')} ago."
                selection.append(record)
            # Customer shall not be contacted, was contacted lately
            else:
                self.__log__.info(F"Customer {record['id']} was last contacted on {record['last_contact']}. Let\'s wait and don\'t spam.")
        return selection


