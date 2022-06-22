# This python code helps me to delete extra unneeded characters from folder names and file names

class foldername():

    def __str__(self):
        return 'This python code helps the user to delete extra unneeded characters from folder names'

    def __init__(self, foldername, prefix_chars, suffix_chars):
        self.foldername_total_char = len(foldername)
        self.foldername_filtered = self.foldername_total_char - prefix_chars - suffix_chars
        self.new_foldername = foldername[prefix_chars:self.foldername_total_char - suffix_chars]

    def foldername_changer(self):
        changed_foldername = self.new_foldername.replace('.', ' ').replace('-', ' ').replace('_', ' ')
        print(changed_foldername)

        return


class filename():

    def __str__(self):
        return 'This python code helps the user to delete extra unneeded characters from file names'

    def __init__(self, filename, prefix_chars, suffix_chars, extention):

        self.filename_total_char = len(filename)
        self.filename_filtered = self.filename_total_char - prefix_chars - suffix_chars
        self.new_filename = filename[prefix_chars:self.filename_total_char - suffix_chars]

    def filename_changer(self):

        changed_filename = self.new_filename.replace('.', ' ').replace('-', ' ').replace('_', ' ')

    # TODO at a later time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    response = input('If you want to change foldername(s) please type "yes". '
                     'If you want to change filename(s) please type "no". ')

    if response == 'yes':
        foldername(str(input()), int(input()), int(input())).foldername_changer()
    if response == 'no':
        filename()