from PIL import Image

# Open the product design image
img = Image.open('product-design.png')

# Generate a mockup by resizing the image
mockup = img.resize((500, 500))

# Save the mockup
mockup.save('product-mockup.png')