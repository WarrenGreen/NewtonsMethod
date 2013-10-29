from PIL import Image
import math

def f(z):
	return z**3 - 1.0

def g(z):
	return z**3 - 2.0*z + 2.0

def h(z):
	return z**8 +15*z**4 - 16

def newton(f, convErr, iterLimit):
	imgX = 512
	imgY = 512
	a = -1.0
	b =  1.0
	step = 1e-6
	image = Image.new("RGB", (imgX,imgY))

	for y in range(0,512):
		zy = y * (b - a) / (imgY - 1) + a
		for x in range(0,512):
			zx = x * (b - a) / (imgX - 1) + a
			z = complex(zx,zy)
			for k in range(iterLimit):
				dz = (f(z + complex(step, step)) - f(z)) / complex(step, step)
				z1 = z - f(z)/dz
				if(abs(z1-z) <= convErr):
					zz = round(z.real,2)+ round(z.imag,2)
					image.putpixel((x,y), ((int)(zz*100) % 4 * 64, (int)(zz*100) % 8 * 32, (int)(zz*100) % 16* 16))
					break
				z = z1
	image.save("frac.png", "PNG")

convErr = 1e-3
iterLimit = 25
newton(h,convErr, iterLimit)




