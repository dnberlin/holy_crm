from PyQt5 import QtWidgets

from holy_crm.ui.v013 import Ui_MainWindow  # importing our generated file

import logging

#from logging import Handler

import sys

class log_to_text_edit(logging.Handler):
    def emit(self, record):
        s = self.format(record) + '\n'
        self.console_out.insertPlainText(s);
        self.console_out.moveCursor(11)
    def __init__ (self, to):
        logging.Handler.__init__(self)
        self.console_out = to



class mywindow(QtWidgets.QMainWindow):
    # init callbacks, logger and buttons
    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
    
        self.ui.setupUi(self)
        
        self.ui.start.clicked.connect(self.start_main)
        self.ui.send_but.clicked.connect(self.ok_customer)
        self.ui.no_send_but.clicked.connect(self.not_ok_customer)
        
        self.ui.console_out.moveCursor(11,0);
        self.ui.console_out.insertPlainText("\n")
        self.ui.console_out.centerOnScroll()
        self.log_hndle = log_to_text_edit(self.ui.console_out)
        
        self.root_logger = logging.getLogger('holy_crm')
        self.root_logger.addHandler(self.log_hndle)
        self.main_loop = ""
        self.current_customer_mail_data = 0
    def start_main(self):
        self.main_loop()
        self.setup_next_customer()
        #holy.launch_holy_crm(conf)
    def ok_customer(self):
        if self.current_customer_mail_data != 0:
            
            self.current_customer_mail_data['body'] = self.ui.cont_edit.getText()
            self.current_customer_mail_data['subject'] = self.ui.sub_edit.getText()
            self.sent_o_not(self.current_customer,self.current_customer_mail_data,True)
            self.setup_next_customer()
    def not_ok_customer(self):
        if self.current_customer_mail_data != 0:
            self.sent_o_not(self.current_customer,self.current_customer_mail_data,False)
            self.setup_next_customer()
    def setup_next_customer(self):
        mail_and_cust = self.next_cust()
        
        if mail_and_cust != False:
            self.current_customer_mail_data = mail_and_cust[1]
            self.current_customer = mail_and_cust[2]
            self.ui.cont_edit.clear()
            self.ui.cont_edit.insertPlainText(self.current_customer_mail_data['body'])
            self.ui.sub_edit.clear()
            self.ui.sub_edit.insertPlainText(self.current_customer_mail_data['subject'])
            self.ui.recipient.setText(self.current_customer_mail_data['send_mail_to'])
            self.ui.last_contact.setText(self.current_customer['contact_string'])
        else:
            self.ui.sub_edit.clear()
            self.ui.cont_edit.clear()
            self.ui.recipient.setText("")
            self.ui.last_contact.setText("")
            self.current_customer_mail_data = 0
class main_window():
    def init_main(sent_or_not,next_customer):
        app = QtWidgets.QApplication([])

        app_window = mywindow()
        
        app_window.show()
        app_window.next_cust = next_customer
        app_window.sent_o_not = sent_or_not
        
        app.exec()
        
