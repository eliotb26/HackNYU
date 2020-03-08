def label():
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types

    # Instantiates a client
    client = vision.ImageAnnotatorClient.from_service_account_json("/Users/kwzhang/Documents/key.json")


    # The name of the image file to annotate
    file_name = os.path.abspath('02.png')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)



def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient.from_service_account_json("/Users/kwzhang/Documents/key.json")

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
def detect_document_with_newLine(path):
    import os,io
    from google.cloud import vision
    from google.cloud.vision import types
    import pandas as pd

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'/Users/kwzhang/Documents/key.json'
    client = vision.ImageAnnotatorClient()

    file_name = 'IMG_0028.jpg'
    image_path = path

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # construct an iamge instance
    image = vision.types.Image(content=content)

    """
    # or we can pass the image url
    image = vision.types.Image()
    image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
    """

    # annotate Image Response
    response = client.document_text_detection(image=image)  # returns TextAnnotation
    df = pd.DataFrame(columns=['locale', 'description'])

    texts = response.text_annotations
    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )

    print(df['description'][0])


def main():
    detect_document_with_newLine("04.png")

main()
