from __future__ import division
import numpy as np
from Tkinter import *             # GUI used for displaying drawings
from PIL import Image, ImageDraw  # depends on Pillow, used for drawing images

from sklearn.preprocessing import normalize
from scipy.ndimage.interpolation import shift
from scipy.ndimage.measurements import center_of_mass
from scipy.misc import imresize, imshow, imsave

# convert to numpy matrix (load image)
# sklearn model.predict

d_size = 500  # draw image size, 500x500 canvas
f_size = 28   # final image size, want 28x28

class Paint:
    def __init__(self):
        self.click_held = False
        self.click_coord = None
        self.root = Tk()
        self.im = Image.new('L', (d_size, d_size), 0)
        self.d = ImageDraw.Draw(self.im)

    def get_digit(self):
        drawing_area = Canvas(self.root, background='#FFF', width=d_size, height=d_size)
        drawing_area.pack()
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.click_press)
        drawing_area.bind("<ButtonRelease-1>", self.click_release)
        drawing_area.bind("<Return>", lambda _ : self.root.quit())
        drawing_area.focus_set()
        self.root.mainloop()
        final = self.post_process(self.im)
        return final

    def click_press(self, event):
        self.click_held = True

    def click_release(self, event):
        self.click_held = False
        self.click_coord = None

    def motion(self, event):
        if self.click_held:
            if self.click_coord:
                event.widget.create_line(self.click_coord[0], self.click_coord[1], event.x, event.y, width=8, smooth=True)
                self.d.line([self.click_coord, (event.x, event.y)], width=8, fill='#FFF')
            self.click_coord = event.x, event.y

    @staticmethod
    def post_process(img):
        im_arr = (np.array(img)/255)
        im_arr = Paint.bbox(im_arr)

        print im_arr.shape
        print f_size/max(*im_arr.shape)
        im_arr = imresize(im_arr, size=f_size/max(*im_arr.shape), interp='bicubic')
        im_arr = normalize(im_arr)  # bicubic messes with our normalized values

        extra = np.subtract((f_size, f_size), im_arr.shape)
        pad1 = np.floor_divide(extra, 2)
        pad2 = np.subtract(extra, pad1)
        top, left  = pad1
        bottom, right = pad2
        im_arr = np.pad(im_arr, ((top,bottom), (left,right)), mode='constant')

        return np.ceil(im_arr*16)

    @staticmethod
    def bbox(img):
        """find bounding box for an array, stripping surrounding zero elements"""
        rows = np.any(img, axis=1)
        cols = np.any(img, axis=0)
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        return img[rmin:rmax, cmin:cmax]

if __name__ == "__main__":
    p = Paint()
    imsave('img.png', p.get_digit())
