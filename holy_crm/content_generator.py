import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape

class ContentGenerator:

    language = {'English': 'en',
                'German': 'de',
                'Spanish': 'es'
                }
    __log__ = logging.getLogger('holy-crm')

    def __init__(self, data):
        self.data = data
        self.correct_dataset()

    def correct_dataset(self):
        self.__log__.debug(F"Correcting record, deleting whitespaces...")
        self.data['person_first_name'] = self.data['person_first_name'].strip()
        self.data['person_last_name'] = self.data['person_last_name'].strip()
        self.data['company_name'] = self.data['company_name'].strip()

    def __generate(self, language, output_type):
        folder = 'data/' + self.language[language.strip()]
        template_file = self.language[language.strip()] + '_' + output_type
        self.__log__.debug(F"Generating {output_type}")
        env = Environment(
            loader = FileSystemLoader(folder),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template(template_file)
        return template.render(data=self.data, salutation=self.__gender_helper())

    def get_email_data(self):
        self.__log__.debug("Collecting email data")
        email_data = {}
        email_data['recipient_name'] = F"{self.data['person_first_name'].strip()} {self.data['person_last_name'].strip()}" 
        if self.data['person_email']:
            email_data['recipient_email'] = self.data['person_email']
        else:
            email_data['recipient_email'] = self.data['company_email']
        email_data['recipient_email'] = 'fw@felixwerner.name'
        email_data['subject'] = self.__generate(self.data['person_language'], 'subject')
        email_data['body'] = self.__generate(self.data['person_language'], 'html_body')
        email_data['plain_body'] = self.__generate(self.data['person_language'], 'plain_body')

        print("------------------------------")
        for entry in email_data:
            print(F'{entry}:\n {email_data.get(entry)} ')
        print("------------------------------\n")

        return email_data

    def __gender_helper(self):
        if(self.data['person_language'] == "German"):
            if self.data['person_gender'] == 'F':
                return 'Frau'
            else:
                return 'Herr'
        elif(self.data['person_language'] == "Spanish"):
            if self.data['person_gender'] == 'F':
                return 'Senora'
            else:
                return 'Senor'
        else:
            if self.data['person_gender'] == 'F':
                return 'Ms.'
            else:
                return 'Mr.'
        