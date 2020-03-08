from flask import Flask
from flask import request
from flask import render_template
from main.py import detect_document_with_newLine

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("Test.html") # this should be the name of your html file
                                        #want this to return the updated website 

@app.route('/', methods=['POST'])
def my_form_post():
<<<<<<< HEAD
    return(detect_document_with_newLine())

    # text1 = request.form['text1']
    #text2 = request.form['text2']
    #if text1>text2 :
    #    return "<h1>text1 larger</h1>"
    #else :
    #    return "<h1>text2 larger</h1>"

=======
    ans = detect_document_with_newLine()
    return "<h1>Testing</h1><p1>%s</p1>"%(ans)


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

    # construct an image instance
    image = vision.types.Image(content=content)

    """
    # or we can pass the image url
    image = vision.types.Image()
    image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
    """
    image = vision.types.Image()
    image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
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
>>>>>>> 4442f6bf07c27d900b2cac65adc7e44c9ec3f152


if __name__ == '__main__':
    app.debug = True
    app.run()

<<<<<<< HEAD
=======
#dsfs
>>>>>>> 4442f6bf07c27d900b2cac65adc7e44c9ec3f152
