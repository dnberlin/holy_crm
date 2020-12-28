import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape

class ContentGenerator:

    __log__ = logging.getLogger('holy-crm')

    def __init__(self, data):
        self.data = data
        self.correct_dataset()

    def correct_dataset(self):
        self.__log__.debug(F"Correcting record, deleting whitespaces...")
        self.data['person_first_name'] = self.data['person_first_name'].strip()
        self.data['person_last_name'] = self.data['person_last_name'].strip()
        self.data['company_name'] = self.data['company_name'].strip()

    def __generate_subject(self):
        self.__log__.debug("Generating subject")
        env = Environment(
            loader = FileSystemLoader('data/'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('en_subject')
        return template.render(data=self.data)

    def __generate_body(self):
        self.__log__.debug("Generating subject")
        env = Environment(
            loader = FileSystemLoader('data/'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('en_body')
        return template.render(data=self.data, salutation=self.__gender_helper())

    def get_attachment(self):
        return
        #path = self.__make_attachment()
        #return path

    """def __make_attachment(self):
        output_path = 'out/'
        filename = 'gen_' + self.data['company'].replace(' ', '_') + '-' + self.data['name'].replace(' ', '_') + '.tex'
        output_target = output_path + filename

        # Prepare templating environment
        templating_tools = TemplatingTools()
        env = templating_tools.generate_jinja_env()
        # Process template
        template = env.get_template('flat_template.tex')
        output = template.render(data=self.data, \
                                 gender=self.__gender_helper(), \
                                 gender_correct=self.__gender_correction(), \
                                 lastname=self.__get_lastname())
        # Write out latex
        with open(output_target, 'w') as fp:
            fp.write(output)
            print (' [*] file %s exported' % output_target)
        # Compile to PDF
        latex_generator = LatexGenerator(output_target)
        output_file = latex_generator.compile_latex()
        #latex_generator.view_pdf()
        
        return output_file"""

    def get_email_data(self):
        self.__log__.debug("Collecting email data")
        email_data = {}
        email_data['recipient_name'] = F"{self.data['person_first_name'].strip()} {self.data['person_last_name'].strip()}" 
        if self.data['person_email']:
            email_data['recipient_email'] = self.data['person_email']
        else:
            email_data['recipient_email'] = self.data['company_email']
        #email_data['recipient_email'] = 'fw@felixwerner.name'
        email_data['subject'] = self.__generate_subject()
        email_data['body'] = self.__generate_body()

        # Generate attachment
        #attachment_path = content_generator.get_attachment()
        #data['attachment'] = attachment_path

        print("------------------------------")
        for entry in email_data:
            print(F'{entry}:\n {email_data.get(entry)} ')
        print("------------------------------\n")

        return email_data

    def __gender_helper(self):
        if self.data['person_language']:
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
                    return 'Mrs.'
                else:
                    return 'Mr.'
        # person_gender missing use country
        elif self.data['country']:
            if(self.data['country'] == "Germany"):
                if self.data['person_gender'] == 'F':
                    return 'Frau'
                else:
                    return 'Herr'
            elif(self.data['country'] == "Spain"):
                if self.data['person_gender'] == 'F':
                    return 'Senora'
                else:
                    return 'Senor'
            else:
                if self.data['person_gender'] == 'F':
                    return 'Mrs.'
                else:
                    return 'Mr.'

        