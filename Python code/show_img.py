def show(doc_id):
    from PIL import Image
    import requests
    url="http://localhost/show_img.php"
    im = Image.open(requests.post(url,data={"doc_id":doc_id}, stream=True).raw)
    import matplotlib.pyplot as plt
    imgplot = plt.imshow(im)
    plt.show()
# n=input("doc id : ")
# show(n)