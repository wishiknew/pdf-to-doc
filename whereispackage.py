import site

# Get the paths to site-packages directories
site_packages = site.getsitepackages()

# Print the paths
print("Site-packages directories:")
for path in site_packages:
    print(path)

# You can also search for the specific location of python-docx
import pdf2docx


print("\nLocation of python-docx module:")
print(pdf2docx.__file__)
