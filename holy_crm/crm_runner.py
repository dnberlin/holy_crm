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

    def start_ui(self):
        return

    def start_shell(self):
        # Initializing handler
        self.__log__.debug('Initializing handler')
        data_handler = DataHandler(self.config)
        email_handler = EmailHandler(self.config)
        customer_selector = CustomerSelector(self.config, data_handler.get_dict_data())

        # Preselect customer
        selected_customer = customer_selector.select_customer()
        
        # Process customer
        for customer in selected_customer:
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
                email_handler.send_email(customer_email_data)
                # Update customer timestamp
                data_handler.update_entry(customer['id'])
            else:
                self.__log__.info(f"Skipping Customer {customer['id']}")
            self.__log__.info(f"Customer {customer['id']} complete\n")
        data_handler.save_data()
