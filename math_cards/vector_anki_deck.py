import genanki as ga
import os

#  Unique ID's
math_vector_deck_id  = 5103388589
math_vector_model_id = 2052455201

# Deck structure
math_vector_deck = ga.Deck(
    math_vector_deck_id,
    'Math Vectors - PyGen')

math_vector_package = ga.Package(math_vector_deck)

# Model structure
math_vector_model = ga.Model(
    math_vector_model_id,
    'PyGen Image Card',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Image Card',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

def create_card_from_images(image_front, image_back):
    note = ga.Note(
        model=math_vector_model,
        fields=[f'<img src="{image_front}">', f'<img src="{image_back}">'])
    return note

# creates anki package file
def create_apkg_file(package):
    package.write_to_file('./output/output.apkg')


math_vector_package.media_files = list(
    map(lambda x: f'./result/{x}', os.listdir('./result')))
