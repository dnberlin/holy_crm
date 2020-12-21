class ContentGenerator:

    def __init__(self, data):
        self.data = data
        self.correct_dataset()

    def correct_dataset(self):
        return
        #self.data['company'] = self.data['company'].replace('&','und')
        #self.data['company'] = self.data['company'].replace('/',' ')
        #self.data['company'] = self.data['company'].replace('.',' ')

    def __generate_subject(self):
        return (f"Proposal for {self.data['person_first_name'].strip()} {self.data['person_last_name'].strip()} "\
                f"at {self.data['company_name'].strip()}. "
                )

    def __generate_body(self):
        return f"Hi {self.__gender_helper()} {self.data['person_first_name'].strip()} {self.data['person_last_name'].strip()}. " \
        f"You email is {self.data['person_email_address'].strip()}. " \
        f"You work for {self.data['company_name'].strip()}."

    def get_attachment(self):
        return
        #path = self.__make_attachment()
        #return path

    def get_phone(self):
        return
        #phone = f"{self.data['mobilephone']}, {self.data['phone_specific']}, {self.data['phone_general']}"
        #return phone

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
        email_data = {}
        email_data['recipient_name'] = F"{self.data['person_first_name'].strip()} {self.data['person_last_name'].strip()}" 
        #if element['email_specific'] != None:
        #    data['recipient_email'] = element['email_specific']
        #else:
        #    data['recipient_email'] = element['email_general']
        email_data['recipient_email'] = 'fw@felixwerner.name'
        email_data['subject'] = self.__generate_subject()
        email_data['body'] = self.__generate_body()
        #data['phone'] = content_generator.get_phone()

        # Generate attachment
        #attachment_path = content_generator.get_attachment()
        #data['attachment'] = attachment_path

        print("------------------------------")
        for entry in email_data:
            print(F'{entry}:\n {email_data.get(entry)} ')
        print("------------------------------\n")

        return email_data

    def __gender_correction(self):
        return
        #if self.data['gender'] == 'f':
        #    return ''
        #else:
        #    return 'r'

    def __get_lastname(self):
        return
        #return self.data['name'].split(' ')[-1]

    def __gender_helper(self):
        if(self.data['country'] == "Deutschland"):
            if self.data['person_gender'] == 'f':
                return 'Frau'
            else:
                return 'Herr'
        else:
            if self.data['person_gender'] == 'F':
                return 'Mrs.'
            else:
                return 'Mr.'

        