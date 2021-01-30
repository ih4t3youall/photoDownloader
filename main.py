from selenium import webdriver
import shutil
import requests
import os




def load_url(url):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    content_blocks = driver.find_elements_by_class_name("comicimg")
    a_elements = []
    for block in content_blocks:
        elements = block.find_elements_by_tag_name("img")
        for el in elements:
            a_elements.append(el.get_attribute('src'))

    global cont_path
    cont_path = cont_path +1
    #path = 'fotos' + str(cont_path) + '/'
    path = url.rsplit('/', 1)[1] + '/'
    print('path: '+path)
    global foto_number
    foto_number = 0

    if not os.path.isdir(path):
        os.mkdir(path)
    for image_url in a_elements:
        get_image(image_url, path)


def get_image(image_url, path):
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)
    filename = image_url.split("/")[-1]
    global foto_number
    filename = str(foto_number)+'_'+ filename
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        fullpath = path + filename
        # Open a local file with wb ( write binary ) permission.
        with open(fullpath, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')

    foto_number = foto_number +1


urls =[]
cont_path = 0
foto_number = 0
while True:
    print('ingrese url , y go para finalizar')
    url = input()
    if url == 'go':
        break
    urls.append(url)

for url in urls:
    load_url(url)




