# for text to speech conversion
import pyttsx3
# for extracting text from a pdf file
import PyPDF2
# for translating extracted text to user desired language
import googletrans

pdf_file = "gaming_test.pdf"
# provide pdf file name in pdf_file and open it with read in binary mode . You can either use sys module and can import pdf name as argument
pdf = open(pdf_file, 'rb')

# accessing pdf contents by creating an object contents
contents = PyPDF2.PdfFileReader(pdf)

# processing the total page count for the pdf and storing it in page_count
page_count = contents.numPages

# showing user with page number along with uploaded file name
print('------------------------------------------------------')
print('Successfully uploaded {} with {} pages'.format(pdf_file, page_count))
print('------------------------------------------------------')
# create a dictionary to store languages with its short names
lang_dict = {'arabic': 'ar', 'bengali': 'bn', 'chinese': 'zh-cn', 'dutch': 'nl',
             'english': 'en', 'french': 'fr', 'german': 'de', 'hindi': 'hi', 'indonesian': 'id',
             'japanese': 'ja', 'korean': 'ko', 'latin': 'la', 'malayalam': 'ml', 'nepali': 'ne',
             'persian': 'fa', 'portuguese': 'pt', 'russian': 'ru', 'spanish': 'es', 'tamil': 'ta',
             'urdu': 'te', 'turkish': 'tr', 'vietnamese': 'vi'}

# showing users available values to select
print('\nList of languages available')
print('-------------------------------------------------------')

for key, val in lang_dict.items():
    print(key, end=' , ')
print('\n-------------------------------------------------------')
# checking user selected language in the provided dictionary
while True:
    # getting user desired language
    get_user_lang = input("Select Language for translation: ")

    if get_user_lang.lower() in lang_dict:
        # if found the input will be passed to translator
        selected = lang_dict[get_user_lang.lower()]
        break
    else:
        # if not found will prompt user to input correct value
        print('\nPlease enter in correct format as mentioned in list!!\n')

# prompting user whether to process full pdf or some certain range or a certain page
while True:
    get_user_input = input("\nDo you want to process the whole pages ? (y/n) : ")

    # if user input is yes process whole text by providing range as total page count

    if get_user_input.lower() == "y" or get_user_input.lower() == "yes":

        for pages in range(page_count):
            read_page = contents.getPage(pages)
            words = read_page.extractText()
            # create object to access translator functionalities
            translator = googletrans.Translator()
            # converting the text using translator
            converted_text = translator.translate(words, dest=selected)
            print('page - {}'.format(pages+1))
            print('-------------------------------------------------')
            # showing converted text by referencing with page number
            print(converted_text)
            print('\n')
            break

# if user inputs no ask user about page selection criteria
    elif get_user_input.lower() == "n" or get_user_input.lower() == "no":
        # taking user criteria for selection
        while True:
            page_selection = input('\nDo you want custom selection or single selection ? : (c/s) : ')

            if page_selection.lower() == "s" or page_selection.lower() == "single":
                try:
                    selected_page_number = int(input('Enter page number you want to translate : '))
                except ValueError as v:
                    print('\nyou have entered in wrong format. Please enter in correct format\n')

                # if page value provided by user greater than page limit , will get a false message
                if selected_page_number > page_count:
                    print('Enter value within page limit')
                else:
                    read_page = contents.getPage(selected_page_number-1)
                    words = read_page.extractText()
                    # create object to access translator functionalities
                    translator = googletrans.Translator()
                    # converting the text using translator
                    converted_text = translator.translate(words, dest=selected)
                    print('page - {}'.format(selected_page_number))
                    print('-------------------------------------------------')
                    # showing converted text by referencing with page number
                    print(converted_text)
                    print('\n')
                    break

            elif page_selection.lower() == "c" or page_selection.lower() == "custom":
                while True:
                    try:
                        lowlimit = int(input('Enter Range from : '))
                        uplimit =  int(input('Enter Range to: '))
                    except ValueError as v:
                        print('\nyou have entered in wrong format. Please enter in correct format\n')

                    if uplimit > page_count or lowlimit > page_count:
                        print('\nEnter value within page limit\n')
                        print('\n')
                    else:
                        for val in range(lowlimit-1, uplimit):
                            read_page = contents.getPage(val)
                            words = read_page.extractText()
                            # create object to access translator functionalities
                            translator = googletrans.Translator()
                            # converting the text using translator
                            converted_text = translator.translate(words, dest=selected)
                            print('\npage - {}'.format(val+1))
                            print('-------------------------------------------------')
                            # showing converted text by referencing with page number
                            print(converted_text)
                            print('\n')
                            print(PyPDF2.__version__)
                            print(googletrans.__version__)
                            # print(pyttsx3.__version__)
                            break
                    break
            else:
                print('\nPlease enter values as provided in option!!\n')
            break
    else:
        print('\nyou have entered a wrong input, Please check and confirm once more\n')
        print('\n')
    break






'''''Translated contents can also be heard using configuring pyttsx3 module in python . We can either save the final output as 
a file and can adjust translation sound volume, voice and speed'''

# speaker = pyttsx3.init()
# voices = speaker.getProperty('voices')
# speaker.setProperty('voice', voices[1].id)
# rate = speaker.getProperty('rate')
# speaker.setProperty('rate', 100)
# speaker.save_to_file(converted_text, "test.txt")
# speaker.runAndWait()
