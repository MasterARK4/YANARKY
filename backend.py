import openai
from PyPDF2 import PdfReader
import re
from tkinter import filedialog
# Set up OpenAI API key
openai.api_key = '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'


#Upload Subroutine
def markscheme_content_upload():
    MS = """
    Writing assessment grids
    AO5:
    • Communicate clearly, effectively and imaginatively, selecting and adapting tone, style and register for different forms, purposes and audiences
    • Organise information and ideas, using structural and grammatical features to support coherence and cohesion of texts
    Level Mark The candidate:
    0 • Provides no rewardable material.
    Level 1 1–4 • Offers a basic response, with audience and/or purpose not fully established.
    • Expresses information and ideas, with limited use of structural and grammatical features.
    Level 2 5–9 • Shows an awareness of audience and purpose, with straightforward use of tone, style and register.
    • Expresses and orders information and ideas; uses paragraphs and a range of structural and grammatical features.
    Level 3 10–14 • Selects material and stylistic or rhetorical devices to suit audience and purpose, with appropriate use of tone, style and register.        
    • Develops and connects appropriate information and ideas; structural and grammatical features and paragraphing make meaning clear.
    Level 4 15–19 • Organises material for particular effect, with effective use of tone, style and register.
    • Manages information and ideas, with structural and grammatical features used cohesively and deliberately across the text.
    Level 5 20–24 • Shapes audience response with subtlety, with sophisticated and sustained use of tone, style and register.
    • Manipulates complex ideas, utilising a range of structural and grammatical features to support coherence and cohesion.
    """
    upload = int(input("If you would like to use your own CONTENT markscheme, Type 1\n"))
    if upload == 1:
        pdf_path = 'Content.pdf'
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            reader = PdfReader(pdf_file)
            
            # Initialize an empty string to store text
            MS = ''
            
            # Loop through each page in the PDF
            for page in reader.pages:
                # Extract text from the current page
                MS += page.extract_text()
        remove = r'\(40 marks \)'
        MS = re.sub(remove, '', MS)
    return MS

def markscheme_SPAG_upload():
    MS = """
    AO6:
    Candidates must use a range of vocabulary and sentence structures for
    clarity, purpose and effect, with accurate spelling and punctuation
    Level Mark The candidate:
    0 • Provides no rewardable material.
    Level 1 1–3 • Uses basic vocabulary, often misspelled.
    • Uses punctuation with basic control, creating undeveloped, often repetitive, sentence structures.
    Level 2 4–6 • Writes with a range of correctly spelt vocabulary, e.g. words with regular patterns such as prefixes, suffixes, double consonants.
    • Uses punctuation with control, creating a range of sentence structures, including coordination and ubordination.
    Level 3 7–9 • Uses a varied vocabulary and spells words containing rregular patterns correctly.
    • Uses accurate and varied punctuation, adapting sentence structure to contribute positively to purpose and effect.
    Level 4 10–12 • Uses a wide, selective vocabulary with only occasional spelling errors.
    • Positions a range of punctuation for clarity, managing entence structures for deliberate effect.
    Level 5 13–16 • Uses an extensive vocabulary strategically; rare spelling errors do not detract from overall meaning.
    • Punctuates writing with accuracy to aid emphasis and precision, using a range of sentence structures accurately and selectively to achieve particular effects. 
    """
    upload = int(input("If you would like to use your SPAG markscheme, Type 1\n"))
    if upload == 1:
        pdf_path = 'SPAG.pdf'
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            reader = PdfReader(pdf_file)
            
            # Initialize an empty string to store text
            MS = ''
            
            # Loop through each page in the PDF
            for page in reader.pages:
                # Extract text from the current page
                MS += page.extract_text()
    return MS

def user_essay_upload():
    MS = """
    Title: A Night of Enigma: A Puzzling Encounter
    One evening, under the embrace of the night, an extraordinary incident unfolded, blurring the lines between reality and imagination. Recalling this peculiar event brings forth a cascade of thoughts, transporting me back to a time when the ordinary gave way to the inexplicable.
    The night commenced unassumingly, with me nestled at home, engrossed in the pages of a book. A sudden rap at the door shattered the tranquility, beckoning me to investigate the source of interruption. To my astonishment, there stood Emily, a longtime friend, her eyes alight with intrigue and her demeanor animated.
    Without preamble, she delved into a narrative so fantastical that it defied rational explanation. Earlier that evening, she recounted, she ventured into the nearby woods in pursuit of inspiration for her latest artistic endeavor. As she traversed deeper into the forest's depths, she stumbled upon a clearing bathed in an ethereal glow, where a mysterious figure stood shrouded in enigma.
    Despite an undercurrent of trepidation, Emily found herself drawn to the enigmatic stranger. As she approached, an inexplicable chill ran down her spine, signaling the presence of the otherworldly. In hushed tones, the figure imparted cryptic revelations, weaving tales of forgotten lore and hidden treasures concealed beneath the earth's surface.
    But as swiftly as the encounter transpired, it dissolved into the night, leaving Emily to ponder the implications of her inexplicable rendezvous. She returned home, her mind abuzz with questions, her heart heavy with the weight of the unknown.
    As I absorbed Emily's account, a sense of bewilderment engulfed me. Was it conceivable that such mysteries lurked beyond the confines of human understanding? Or was Emily's tale a manifestation of her imagination, fueled by the eerie ambiance of the nocturnal realm?
    Through the passage of time, as dawn chased away the shadows of night, Emily and I lingered in contemplative silence. Though the enigma of that night may forever elude comprehension, one certainty prevails: it was an evening of intrigue, a testament to the boundless mysteries that lie beyond the realm of ordinary perception.
    """
    upload = int(input("Please type 1 to import your essay\n"))
    if upload == 1:
        pdf_path = 'Essay.pdf'
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            reader = PdfReader(pdf_file)
            
            # Initialize an empty string to store text
            MS = ''
            
            # Loop through each page in the PDF
            for page in reader.pages:
                # Extract text from the current page
                MS += page.extract_text()
    return MS

def essay_prompt_upload():
    MS = """
    Write about a time when something strange or unusual happened to you or someone
    you know.
    Your response could be real or imagined.
    *Your response will be marked for the accurate and appropriate use of vocabulary, spelling,
    punctuation and grammar.
    """
    upload = int(input("Please type 1 to import your the essay prompt\n"))
    if upload == 1:
        pdf_path = 'Prompt.pdf'
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            reader = PdfReader(pdf_file)
            
            # Initialize an empty string to store text
            MS = ''
            
            # Loop through each page in the PDF
            for page in reader.pages:
                # Extract text from the current page
                MS += page.extract_text()
    return MS



#Analysis Subroutines- Choising what feedback to output to the user and structuring the necessary Queries to send to the API
def making_choice(essay, essay_prompt, markscheme_spag, markscheme_content):
    options = int(input('''
        1. Mark only Content
        2. Mark only SPAG
        3. Marking Both
    '''))
    format_content = structure_individual_API_query(essay, essay_prompt, markscheme_content)
    format_spag = structure_individual_API_query(essay, essay_prompt, markscheme_spag)

    if options == 1:
        print('You have decided to only mark content')
        comparison_result = compare_essay_and_markscheme(format_content)
        return comparison_result

    elif options ==2:
        print('you have decided to only mark SPAG')
        comparison_result = compare_essay_and_markscheme(format_spag)
        return comparison_result

    elif options ==3:
        print('you have decided to mark both')
        content_feedback_result = compare_essay_and_markscheme(format_content)

        print('The feedback of your content has been processed.\n Your spag feedback is being processed.....')
        spag_feedback_result = compare_essay_and_markscheme(format_spag)

        print('Your SPAG and content feedback has been processed!!!! \n Your combined feedback is being processed')
        format_combined_feedback = structure_combined_API_query(content_feedback_result, spag_feedback_result)
        combined_feedback = compare_essay_and_markscheme(format_combined_feedback)

        return combined_feedback

def structure_individual_API_query(text, text_prompt, rubric):
    formating_request = """
        Hello API,
        I have an essay, the essay prompt, and the markscheme attached. Analyse the markscheme (total marks avalile, and highest level achievable), and the Essay.
        Based on this provide concise, 200-word feedback on the essay, considering the prompt and markscheme? 
        Ensure relevance to the prompt. Include strengths, areas for improvement, and give feedback on how the essay can attain the highest level avalible. 
        Additionally, match the essay to the designated level in the markscheme, avoiding bias. Format the response with the appropriate subheadings. 
        Make sure to correctly identify the highest level and score in the markscheme. Also give the essay a score out of the total marks avalible.
        Format the response in the following way:
        1. Prompt Relevence
        2. Strength
        3. Weaknesses
        4. Score and Level
        5. Achieving the Highest Level


    """
    messege = f"Essay: {text}\n\n Markscheme: {rubric}\n\n Comparison Request {formating_request}"
    return messege

def structure_combined_API_query(content_feedback, spag_feedback):
    formating_request = """
        Hello API,
        This query is for essay feedback on content and SPAG. Merge these two feedbacks into a single comprehensive feedback covering both SPAG and content.
        The feedback should include strengths and areas for improvement for both SPAG and content. Additionally, suggest how the essay can reach the highest level available for both aspects.
        The response should have a structure of:
        1. Relevence to Prompt
        2. Level of SPAG and Level of Content
        3. Overall Strengths of both content and SPAG
        4. Overall weaknesses for both content and SPAG
        5. Overall Feedback to reach the highest level in the markscheme
        6. Approximate mark for content out of the total avalible mark for content
        7. Approximate mark for SPAG out of the total avalible mark for SPAG
        8. Total mark for both content and SPAG out of total marks avalible
        """
    messege = f"Content feedback: {content_feedback}\n\n SPAG feedback: {spag_feedback}\n\n Processing Request {formating_request}"
    return messege
    

#Subroutines for Creating the practice Excercises
def generating_practice_questions(Feedback):
    questions = int(input("Type '1' if you would like to generate practice questions to help\n"))
    if questions == 1:
        format_questions = structure_practice_question(Feedback)
        print('generating question')
        Question_generated = compare_essay_and_markscheme(format_questions)
        return Question_generated
    else:
        return 'Thank you for using the program'

def structure_practice_question(Feedback):
    formating_request = """
        Hello API,
        This messege contains some feedback from the essay that the student has writen. 
        Please analyse this feedback and generate 2 to 3 practice excercises to help the user improve their weak skills in their essay.
        These excercises should help the user address the weaknesses in the essay feedback. The excercises should not take more than 10 mins each. 
    """
    messege = f"Essay Feedback: {Feedback}\n\n Practice Question Request: {formating_request}"
    return messege


#Subroutine that sends and recieves content from API
def compare_essay_and_markscheme(query):
    try:
 #       print("Essay:", essay)
 #       print("Markscheme:", markscheme)

        # Use OpenAI API to compare essay and markscheme 
        comparison = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
            max_tokens=1000,
            temperature=0.5
        )

        # print("API Response:", comparison)  # Print API response

        if 'choices' in comparison and len(comparison.choices) > 0 and 'message' in comparison.choices[0] and 'content' in comparison.choices[0].message:
            return comparison.choices[0].message.content.strip()
        else:
            return "Error comparing essay and markscheme: Text not found in API response"

    except Exception as e:
        return f"Error comparing essay and markscheme: {str(e)}"


# Getting the Necessary data for the code
markscheme_content = markscheme_content_upload()
markscheme_spag = markscheme_SPAG_upload()
essay = user_essay_upload()
essay_prompt = essay_prompt_upload()

print('\n The Necessary Files have been uploaded\n')

# Performing the actual functions of the code To give Feedback
Feedback_output = making_choice(essay, essay_prompt, markscheme_spag, markscheme_content)

Extra_Questions = generating_practice_questions(Feedback_output)

if Extra_Questions == 'Thank you for using the program':
    print(f'This is Your Feedback:\n{Feedback_output}')
else:
    print(f'This is Your Feedback:\n{Feedback_output}\n')
    print(f'These are some practice questions:\n{Extra_Questions}\n')


#Creating a file that contains the output
print('The Response Is now being saved to a file called feedback.txt\n')

with open('feedback.html', 'w') as file:
    file.write("<style>")
    file.write("body {")
    file.write("    font-family: Arial, sans-serif;")  # Use a commonly available font for better compatibility
    file.write("}")
    file.write(".container {")
    file.write("    max-width: 800px;")  # Adjust the max-width value as needed
    file.write("    margin: 10px auto;")    # Center the container horizontally with reduced margin
    file.write("    padding: 10px;")     # Add reduced padding for better readability
    file.write("    overflow-x: auto;")  # Enable horizontal scrolling if content overflows horizontally
    file.write("}")
    file.write("</style>")

    file.write("<div class='container'>")
    file.write("<p><strong>This is the Essay Prompt you Entered:</strong></p>")
    file.write(f"<p>{essay_prompt.replace('\n', '<br>')}</p>")
    file.write("<br>")
    file.write("<p><strong>This is the Essay you Entered:</strong></p>")
    file.write(f"<p>{essay.replace('\n', '<br>')}</p>")
    file.write("<br>")
    file.write("<p><strong>Here is the Feedback for your Essay:</strong></p>")
    file.write(f"<p>{Feedback_output.replace('\n', '<br>')}</p>")
    file.write("<br>")
    if Extra_Questions == 'Thank you for using the program':
        file.write("<p><strong>You did not ask for any practice exercises</strong></p>")
    else:
        file.write("<p><strong>Here are some practice exercises to work on your Weaknesses:</strong></p>")
        file.write(f"<p>{Extra_Questions.replace('\n', '<br>')}</p>")
    file.write("</div>")
