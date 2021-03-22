import genanki as ga
import os

math_vector_deck_id  = 5103388589
math_vector_model_id = 2052455201

en_de_deck_id        = 6793587463
en_de_model_id       = 2507387169

math_vector_deck = ga.Deck(
    math_vector_deck_id,
    'Math Vectors - PyGen')

en_de_deck = ga.Deck(
    en_de_deck_id,
    'English Vocabulary Context Book (to German) - PyGen')


math_vector_model = ga.Model(
    en_de_model_id,
    'Image Card',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

en_de_model = ga.Model(
    en_de_model_id,
    'Image Card',
    fields=[
        {'name': 'English'},
        {'name': 'German'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{English}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{German}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{German}}',
            'afmt': '{{FromtSide}}<hr id="answer">{{English}}',
        }
    ])

math_vector_package = ga.Package(math_vector_deck)
en_de_package = ga.Package(en_de_deck)


def create_card_from_images(image_front, image_back):
    note = ga.Note(
        model=math_vector_model,
        fields=[f'<img src="{image_front}">', f'<img src="{image_back}">'])
    return note


def create_apkg_file(package):
    package.write_to_file('./output/output.apkg')


math_vector_package.media_files = list(
    map(lambda x: f'./result/{x}', os.listdir('./result')))

en_de_package.media_files = list(
    map(lambda x: f'./result/{x}', os.listdir('./result')))