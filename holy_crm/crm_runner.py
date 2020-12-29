import logging

from holy_crm.config import Config
from holy_crm.data_handler import DataHandler
from holy_crm.email_handler import EmailHandler
from holy_crm.content_generator import ContentGenerator
from holy_crm.customer_selector import CustomerSelector

class CrmRunner:

    __log__ = logging.getLogger('holy-crm')

    def __init__(self, config):
        self.config = config
        self.__initialize()

    def start_ui(self):
        return

    def start_shell(self):   
        # Process customer
        customer = self.customer_selector.get_customer()
        while customer:
            self.__log__.info(f"Processing Customer {customer['id']}")
            self.__log__.debug(f"Preparing E-Mail content based on data {customer}")
            # Initialize content_generator for customer
            content_generator = ContentGenerator(customer)
            customer_email_data = content_generator.get_email_data()
            # Prepare email
            self.__log__.info(f"Need info! Send this E-Mail? (y/n)")
            send = input("")
            if send == "y":
                # Send E-Mail
                self.email_handler.send_email(customer_email_data)
                # Update customer timestamp
                self.data_handler.update_entry(customer['id'])
            else:
                self.__log__.info(f"Skipping Customer {customer['id']}")
            self.__log__.info(f"Customer {customer['id']} complete\n")
            # Get next customer
            customer = self.customer_selector.get_customer()
        else:
            # Save updated data
            self.data_handler.save_data()

    def __initialize(self):
        self.__log__.debug('Initializing handler')
        self.data_handler = DataHandler(self.config)
        self.email_handler = EmailHandler(self.config)
        self.customer_selector = CustomerSelector(self.config, self.data_handler.get_dict_data())

