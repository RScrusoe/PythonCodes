# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
import cv2
import math
 
def select_image():
	# grab a reference to the image panels
	global panelImage, panelGrayImage, path, updated_path
 
	# open a file chooser dialog and allow the user to select an input
	# image
	path = filedialog.askopenfilename()
	updated_path = path
	# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale
		image = cv2.imread(path)
		image = image_resize(image)

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
		# convert the images to PIL format...
		image = Image.fromarray(image)
		gray = Image.fromarray(gray)
		
		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		gray = ImageTk.PhotoImage(gray)
		
		# if the panels are None, initialize them
		if panelImage is None or panelGrayImage is None:
			# the first panel will store our original image
			panelImage = Label(image=image)
			panelImage.image = image
			panelImage.grid(row=0, column=1, columnspan=1, rowspan=12, sticky=W+E+N+S, padx=10, pady=10)
 
			# while the second panel will store the edge map
			panelGrayImage = Label(image=gray)
			panelGrayImage.image = gray
			panelGrayImage.grid(row=12, column=1, columnspan=1, rowspan=12, sticky=W+E+N+S, padx=10, pady=10)
 
		# otherwise, update the image panels
		else:
			# update the pannels
			panelImage.configure(image=image)
			panelGrayImage.configure(image=gray)
			panelImage.image = image
			panelGrayImage.image = gray
# initialize the window toolkit along with the two image panels

def image_resize(image):
	r = 330.0 / image.shape[1]
	dim = (330, int(image.shape[0] * r))
	return cv2.resize(image, dim)

def save_image():
	global updated_path
	new_img=img = cv2.imread(updated_path)
	cv2.imwrite('Output.jpg', new_img)

def fft_mag():
	global updated_path
	img = cv2.imread(updated_path,0)
	img_FFT = np.fft.fft2(img)
	img_FFT = np.fft.fftshift(img_FFT)   #shift to get origin at the centre of image 
	img_FFT = 20*np.log(np.abs(img_FFT))
	plt.imshow(img_FFT, cmap = 'gray' )
	plt.show()

def fft_phase():
	global updated_path
	img = cv2.imread(updated_path,0)
	img_FFT = np.fft.fft2(img)
	img_FFT = np.fft.fftshift(img_FFT)		#shift to get origin at the centre of image    
	plt.imshow(np.angle(img_FFT), cmap = 'gray')
	plt.show()

def image_histogram():
	cv2.destroyAllWindows()
	global pannelHistogram, updated_path
	pathHistogram = 'Histogram.jpg'

	img = cv2.imread(updated_path)
	
	m = img.shape[0]
	n = img.shape[1]
	#print (m,n)
	blank = np.zeros(256)
	for i in range(m):
		for j in range(n):
			blank[img[i,j]] = blank[img[i,j]] + 1
	#print(blank)
	plt.plot(blank, color = 'r')
	plt.show()

def equalized_histogram():
	cv2.destroyAllWindows()
	global pannelEqHistogram, path, updated_path
	img = cv2.imread(updated_path,0)

	pathEqHistogram = 'EqHistogram.jpg'
	updated_path = pathEqHistogram

	img = image_resize(img)

	m = img.shape[0]
	n = img.shape[1]

	hist = np.zeros(256)

	for i in range(m):
		for j in range(n):
			hist[img[i,j]] += 1

	hist = hist/(m*n)
	cdf = np.cumsum(hist)
	cdf_normalized = cdf

	newImg = np.zeros((m,n))

	for i in range(m):
		for j in range(n):
			newImg[i,j] = int(np.floor(255*cdf_normalized[img[i,j]]))

	# Write the image
	cv2.imwrite(pathEqHistogram, newImg)

	new = cv2.imread(pathEqHistogram)
	new = Image.fromarray(new)
	new = ImageTk.PhotoImage(new)

	pannelEqHistogram = Label(image=new)
	pannelEqHistogram.image = new
	pannelEqHistogram.grid(row=0, column=2, columnspan=2, rowspan=24, sticky=W+E+N+S, padx=150, pady=10)

def gamma_correction():
	cv2.destroyAllWindows()
	global pannelGammaCorrection, path, updated_path, gammaValue
	gamma = float(gammaValue.get())
	img = cv2.imread(updated_path,0)

	pathGammaCorr = 'Gamma Corrected.jpg'
	updated_path = pathGammaCorr

	img = image_resize(img)
	img = img/255.0
	img = cv2.pow(img, (1.0/gamma))
	
	# Write the image
	cv2.imwrite(pathGammaCorr, img*255)

	new = cv2.imread(pathGammaCorr)
	new = Image.fromarray(new)
	new = ImageTk.PhotoImage(new)

	pannelGammaCorrection = Label(image=new)
	pannelGammaCorrection.image = new
	pannelGammaCorrection.grid(row=0, column=2, columnspan=2, rowspan=24, sticky=W+E+N+S, padx=150, pady=10)

def log_correction():
	cv2.destroyAllWindows()
	global pannelLogCorrection, path, updated_path
	img = cv2.imread(updated_path,0)

	pathLogCorr = 'Log Corrected.jpg'
	updated_path = pathLogCorr

	img = image_resize(img)

	log_img = np.log10(1+img);
	log_img = log_img*(255/np.log10(256))
	log_img = np.asarray(log_img,dtype= "uint8")

	cv2.imwrite(pathLogCorr, log_img)

	new = cv2.imread(pathLogCorr)
	new = Image.fromarray(new)
	new = ImageTk.PhotoImage(new)

	pannelLogCorrection = Label(image=new)
	pannelLogCorrection.image = new
	pannelLogCorrection.grid(row=0, column=2, columnspan=2, rowspan=24, sticky=W+E+N+S, padx=150, pady=10)

def butterworth_sharp():
	cv2.destroyAllWindows()
	global pannelButterSharp, path, updated_path
	img = cv2.imread(updated_path,0)
	N0 = float(BSorder.get())
	D_0 = float(BSDo.get())

	pathButterSharp = 'Butterworth Sharpning.jpg'
	updated_path = pathButterSharp

	img = image_resize(img)
	m = img.shape[0]
	n = img.shape[1]
	butter_img = img.copy()
	imgFFT = np.fft.fftshift(np.fft.fft2(img))

	centerX = m/2
	centerY = n/2

	for x in range(m):
		for y in range(n):
			D = (x-centerX)**2 + (y-centerY)**2
			if(D == 0):
				pass
			else:
				imgFFT[x,y] = imgFFT[x,y] * (1 / (1 + pow( ((D_0 ** 2)/(D)),N0) ))

	butter_img = np.abs(np.fft.ifft2(np.fft.ifftshift(imgFFT)))

	butter_img = ((butter_img)/np.amax(butter_img))
	
	cv2.imwrite(pathButterSharp, 255*butter_img)

	new = cv2.imread(pathButterSharp)
	new = Image.fromarray(new)
	new = ImageTk.PhotoImage(new)

	pannelButterSharp = Label(image=new)
	pannelButterSharp.image = new
	pannelButterSharp.grid(row=0, column=2, columnspan=2, rowspan=24, sticky=W+E+N+S, padx=150, pady=10)


def gaussian_blurr():
	cv2.destroyAllWindows()
	global pannelGaussianBlurr, path, updated_path
	img = cv2.imread(updated_path,0)
	D0 = int(GaussBlWidth.get())

	pathGaussianBlurr = 'Gaussian Blurr.jpg'
	updated_path = pathGaussianBlurr

	img = image_resize(img)

	m = img.shape[0]
	n = img.shape[1]
	new_img = img.copy()

	img1 = np.zeros((m+4*D0, n+4*D0), dtype=np.float)
	img1[2*D0:2*D0+m, 2*D0:2*D0+n] = img[:,:]
	# Taking contribution from the next 2*D0 elements to be significant, the window size is (4*D0+1) X (4*D0+1)                          

	gauss = np.zeros(((4*D0)+1,(4*D0)+1))

	for k in range(4*D0+1):
		for l in range(4*D0+1):
			gauss[k][l] = 1000*math.exp(-((k-2*D0)**2+(l-2*D0)**2)/(2*(D0**2)))

	for i in range(m):
		for j in range(n):
			# if((i-k+2*D0)>=0 and (i-k+2*D0)<m and (j-l+2*D0)>=0 and (j-l+2*D0)<n):
			subImage = img1[i:i+(4*D0)+1,j:j+(4*D0)+1]
			dotProd = np.sum(np.sum(np.multiply(gauss, subImage)))
			new_img[i,j] = dotProd/(2000*math.pi*(D0**2))

	cv2.imwrite(pathGaussianBlurr, new_img)
	new = cv2.imread(pathGaussianBlurr)
	new = Image.fromarray(new)
	new = ImageTk.PhotoImage(new)

	pannelGaussianBlurr = Label(image=new)
	pannelGaussianBlurr.image = new
	pannelGaussianBlurr.grid(row=0, column=2, columnspan=2, rowspan=24, sticky=W+E+N+S, padx=150, pady=10)

def reset():
	global path, updated_path
	global panelImage, panelGrayImage, pannelHistogram, pannelEqHistogram, pannelGammaCorrection, pannelLogCorrection, pannelButterSharp, pannelGaussianBlurr
	updated_path = path
	if pannelEqHistogram:
		pannelEqHistogram.config(image = '')
	if pannelGammaCorrection:
		pannelGammaCorrection.config(image = '')
	if pannelLogCorrection:
		pannelLogCorrection.config(image = '')
	if pannelButterSharp:
		pannelButterSharp.config(image = '')
	if pannelGaussianBlurr:
		pannelGaussianBlurr.config(image = '')


root = Tk()
root.title("GUI")
root.geometry("1279x799")

global gammaValue, panelImage, panelGrayImage, pannelHistogram, pannelEqHistogram, pannelGammaCorrection, pannelLogCorrection, pannelButterSharp, pannelGaussianBlurr
panelImage = None
panelGrayImage = None
pannelHistogram = None
pannelEqHistogram = None
pannelGammaCorrection = None
pannelLogCorrection = None
pannelButterSharp = None
pannelGaussianBlurr = None

# sets the default values
gammaValue = StringVar()
gammaValue.set('2.0')
BSorder = StringVar()
BSorder.set('2.0')
BSDo = StringVar()
BSDo.set('3.0')
GaussBlWidth = StringVar()
GaussBlWidth.set('3')
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
img_select_button = Button(root, text="Select an image", command=select_image)
img_select_button.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

histogram_button = Button(root, text="Histogram", command=image_histogram)
histogram_button.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

eq_histogram_button = Button(root, text="Equalized Image", command=equalized_histogram)
eq_histogram_button.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

gamma_lable = Label(root, text='Please enter gamma value').grid(row=3, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)
gamma_entry = Entry(root, textvariable=gammaValue).grid(row=4, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

gamma_corr_button = Button(root, text="Gamma Correction", command=gamma_correction)
gamma_corr_button.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

lgo_corr_button = Button(root, text="Log Correction", command=log_correction)
lgo_corr_button.grid(row=6, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

ButterSharp_lable1 = Label(root, text='Give order of filter').grid(row=7, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)
ButterSharp_entry1 = Entry(root, textvariable=BSorder).grid(row=8, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

ButterSharp_lable2 = Label(root, text='Give the cutoff width(Do)').grid(row=9, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)
ButterSharp_entry2 = Entry(root, textvariable=BSDo).grid(row=10, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

butter_sharp_button = Button(root, text="Butterworth Sharpening", command=butterworth_sharp)
butter_sharp_button.grid(row=11, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

GaussBl_lable = Label(root, text='Please enter the width for gaussian blurring').grid(row=12, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)
GaussBl_entry = Entry(root, textvariable=GaussBlWidth).grid(row=13, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

gauss_blurr_buttom = Button(root, text="Gaussian Blurr", command=gaussian_blurr)
gauss_blurr_buttom.grid(row=14, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

FFT_mag_buttom = Button(root, text="FFT Magnitude", command=fft_mag)
FFT_mag_buttom.grid(row=15, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

FFT_phase_button = Button(root, text="FFT Phase", command=fft_phase)
FFT_phase_button.grid(row=16, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

save_button = Button(root, text="Save Image", command=save_image)
save_button.grid(row=17, column=0, columnspan=1, rowspan=1, sticky=W, padx=10, pady=1)

undo_button = Button(root, text="Undo", command=reset)
undo_button.grid(row=18, column=0, columnspan=1, rowspan=3, sticky=N, padx=10, pady=1)

 
# kick off the GUI
root.mainloop()
