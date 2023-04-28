from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What programming language did you first use?"
my_survey = AnonymousSurvey(question)

# Show the question and store responses to the question
my_survey.show_question()
print("Enter q at any time to quit\n")
while True:
    response = input("\nhat programming language did you first use? : ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("Thank you to everyone that took part in the survey")
my_survey.show_results()

