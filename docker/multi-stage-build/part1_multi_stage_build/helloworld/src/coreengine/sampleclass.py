import cv2

class SampleClass:

    def __init__(self):

        pass

    def test(self):

        

        overlay = cv2.imread("/Users/chiawei.lim/Downloads/buffer/technical-posts/metadata/banner.png")
        
        overlay = cv2.resize(overlay, (150,150))

        print(overlay.shape)
