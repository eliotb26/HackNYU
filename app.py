from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    ans = detect_document_with_newLine()
    return "<p1>%s</p1>"%(ans)


def detect_document_with_newLine():
    import os,io
    from google.cloud import vision
    from google.cloud.vision import types
    import pandas as pd

    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'Hand write code-1f0460a79a72.json'
    client = vision.ImageAnnotatorClient()

    file_name = '04.jpg'
    image_path = file_name

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

    return df['description'][0]


if __name__ == '__main__':
    app.debug = True
    app.run()
