import genanki as ga
import os

deck_id = 5103388589
model_id = 2052455201

# import random
# def generate_random_id():
#     return random.randint(1000000000, 9999999999)

my_deck = ga.Deck(
    deck_id,
    'Mathe Abitur Zusammenfassung - Python Generiert')

my_model = ga.Model(
    model_id,
    'Bimage Card',
    fields=[
        {'name': 'QuestionImage'},
        {'name': 'AnswerImage'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{QuestionImage}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{AnswerImage}}',
        },
    ])

my_package = ga.Package(my_deck)


def create_card_from_images(image_front, image_back):
    note = ga.Note(
        model=my_model,
        fields=[f'<img src="{image_front}">', f'<img src="{image_back}">'])
    return note


def create_apkg_file(package=my_package):
    my_package.write_to_file('./output/output.apkg')


my_package.media_files = list(
    map(lambda x: f'./result/{x}', os.listdir('./result')))
