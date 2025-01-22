import sqlite3
from datetime import datetime


def populate_database():
    conn = sqlite3.connect('instance/quiz.db')
    cursor = conn.cursor()


    # Insert System Quizzes (Math and Biology) as if created by a system user (user_id = NULL)
    cursor.execute("INSERT INTO quiz (title, description, user_id, is_system_quiz, status) VALUES (?, ?, ?, ?, ?)",
                   ('Basic Math Quiz', 'Test your basic math skills', None, True, 'active'))
    cursor.execute("INSERT INTO quiz (title, description, user_id, is_system_quiz, status) VALUES (?, ?, ?, ?, ?)",
                   ('Introduction to Biology', 'A quiz covering basic biology concepts', None, True, 'active'))

    # Insert System Quizzes (Programming and History) as if created by a system user (user_id = NULL)
    cursor.execute("INSERT INTO quiz (title, description, user_id, is_system_quiz, status) VALUES (?, ?, ?, ?, ?)",
                   ('Python Programming Basics', 'Test your basic Python programming knowledge', None, True, 'active'))
    cursor.execute("INSERT INTO quiz (title, description, user_id, is_system_quiz, status) VALUES (?, ?, ?, ?, ?)",
                   ('World History - Ancient Civilizations', 'A quiz on ancient civilizations', None, True, 'active'))


    # Insert Questions for the 'Basic Math Quiz' (quiz_id = 1)
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (1, 'What is 5 + 7?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (1, 'What is 12 - 3?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (1, 'What is 4 * 6?'))

    # Insert Question Choices for 'What is 5+7?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (1, '10', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (1, '12', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (1, '14', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (1, '11', False))

    # Insert Question Choices for 'What is 12 - 3?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (2, '8', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (2, '9', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (2, '10', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (2, '11', False))

    # Insert Question Choices for 'What is 4 * 6?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (3, '20', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (3, '22', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (3, '24', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (3, '26', False))

    # Insert Questions for 'Introduction to Biology' (quiz_id = 2)
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (2, 'What is the powerhouse of the cell?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (2, 'What is the process by which plants make food?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (2, 'Which of these is a mammal?'))

    # Insert Question Choices for 'What is the powerhouse of the cell?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (4, 'Nucleus', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (4, 'Mitochondria', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (4, 'Endoplasmic Reticulum', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (4, 'Golgi Apparatus', False))

    # Insert Question Choices for 'What is the process by which plants make food?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (5, 'Respiration', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (5, 'Photosynthesis', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (5, 'Transpiration', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (5, 'Digestion', False))

    # Insert Question Choices for 'Which of these is a mammal?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (6, 'Lizard', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (6, 'Eagle', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (6, 'Dolphin', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (6, 'Snake', False))


    # Insert Questions for 'Python Programming Basics' (quiz_id = 3)
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (3, 'What is the output of print(2 + 2)?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (3, 'Which keyword is used to define a function?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (3, 'What is a list in Python?'))

    # Insert Question Choices for 'What is the output of print(2 + 2)?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (7, '2', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (7, '4', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (7, '22', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (7, 'Error', False))

    # Insert Question Choices for 'Which keyword is used to define a function?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (8, 'function', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (8, 'def', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (8, 'func', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (8, 'define', False))

    # Insert Question Choices for 'What is a list in Python?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (9, 'A variable type', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (9, 'An ordered sequence of items', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (9, 'A loop construct', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (9, 'A conditional statement', False))


    # Insert Questions for 'World History - Ancient Civilizations' (quiz_id = 4)
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (4, 'Which civilization built the pyramids of Giza?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (4, 'What was the name of the writing system used in Mesopotamia?'))
    cursor.execute("INSERT INTO question (quiz_id, text) VALUES (?, ?)", (4, 'Who was the first emperor of China?'))

    # Insert Question Choices for 'Which civilization built the pyramids of Giza?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (10, 'Greek', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (10, 'Roman', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (10, 'Egyptian', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (10, 'Persian', False))

    # Insert Question Choices for 'What was the name of the writing system used in Mesopotamia?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (11, 'Hieroglyphics', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (11, 'Cuneiform', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (11, 'Alphabet', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (11, 'Sanskrit', False))

    # Insert Question Choices for 'Who was the first emperor of China?'
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (12, 'Confucius', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (12, 'Qin Shi Huang', True))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (12, 'Han Wudi', False))
    cursor.execute("INSERT INTO question_choice (question_id, text, is_correct) VALUES (?, ?, ?)", (12, 'Mao Zedong', False))




    conn.commit()
    conn.close()
    print("Database populated with system quizzes successfully!")


# if __name__ == "__main__":
#     populate_database()