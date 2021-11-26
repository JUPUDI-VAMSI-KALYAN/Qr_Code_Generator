import qrcode
import matplotlib.pyplot as plt
import matplotlib.image as mping
data = "Please pay $500 to purchase"

img = qrcode.make(data)
#img = mping.imread(img)
plt.imshow(img)
plt.show()
