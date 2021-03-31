import genanki as ga
import os

en_de_deck_id        = 6793587463
en_de_model_id       = 2507387169

en_de_deck = ga.Deck(
    en_de_deck_id,
    'English Vocabulary Context Book (to German) - PyGen')


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

en_de_package = ga.Package(en_de_deck)


def create_card_from_images(image_front, image_back):
    note = ga.Note(
        model=en_de_model,
        fields=[f'<img src="{image_front}">', f'<img src="{image_back}">'])
    return note


def create_apkg_file(package):
    package.write_to_file('./output/output.apkg')


en_de_package.media_files = list(
    map(lambda x: f'./result/{x}', os.listdir('../result')))