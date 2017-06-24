from PIL import Image.open()
from PIL import ImageEnhance, ImageFilter

gym_view_ext = Image.open("far corner gym view_ext.jpg")
gym_view = Image.open("far corner gym view.jpg")

box = (50, 250, 450, 500)
region = gym_view_ext.crop(box)
region = region.convert(mode="L")
gym_view_ext_2 = gym_view_ext.copy()
gym_view_ext_2.paste(region, box)
gym_view_ext_2.show()


gym_view_1 = ImageEnhance.Color(gym_view).enhance(.5)
gym_view_1.show()

gym_view_1_blurred = gym_view_1.filter(ImageFilter.GaussianBlur(radius=2))
gym_view_1_blurred.show()






