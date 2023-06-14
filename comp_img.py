#img compression command line

#import neccessary libraries
from PIL import Image
import os

#get file size in bytes
def get_filesize(filepath):
    filesize = os.path.getsize(filepath)
    return filesize

#convert bytes to Kilobytes
def b_to_kb(bytes_value):
    kilobytes_value = bytes_value / 1024
    return kilobytes_value


#convert bytes to megabytes
def b_to_mb(bytes_value):
    megabytes_value = bytes_value / 1048576
    return megabytes_value

#naming the output file
def name_output_file(filename):
    output_file = "compressed_" + filename
    return output_file

#finding the type of extension (jpg,jpeg or png)
def find_img_extension(filename):
    extension = filename.split(".")[1]
    return extension

#compression
def compress(image_file,compress_lvl=50):
    filepath = os.path.join(os.getcwd(), image_file)
    
    #file output name
    compressed_image_file = name_output_file(image_file)
    
    #find the extentsion type
    extension = find_img_extension(image_file)
    
    #filesize in kb and mb
    initial_filesize_kb = round(b_to_kb(get_filesize(image_file)),3)
    initial_filesize_mb = round(b_to_mb(get_filesize(image_file)),3)
    
   
    print(f"Initial image file size: {initial_filesize_kb} kb")
    if initial_filesize_mb != 0:
        print(f"Initial image file size: {initial_filesize_mb} mb")
    else:
        pass
    
    if extension == "jpg" or extension == "jpeg":
        print("compressing [JPG,JPEG] ....")
        image = Image.open(filepath)
       
    
        # Save the image as a compressed JPG/JPEG file
        image.save(compressed_image_file,
                   "JPEG",
                   optimize=True,
                   compress_level=compress_lvl)
        
        print("JPG/JPEG compression completed ")
        
        #filesize in kb and mb
        final_filesize_kb = round(b_to_kb(get_filesize(compressed_image_file)),3)
        final_filesize_mb = round(b_to_mb(get_filesize(compressed_image_file)),3)
    
        print(f"Final image file size: {final_filesize_kb} kb")
        if initial_filesize_mb != 0:
            print(f"Final image file size: {final_filesize_mb} mb")
        else:
            pass
        
        #difference in filesize
        reduced_filesize_kb = round((initial_filesize_kb - final_filesize_kb),3)
        reduced_filesize_mb = round((initial_filesize_mb - final_filesize_mb),3)
        print(f"image file size reduced : {reduced_filesize_kb} kb")
        print(f"image file size reduced : {reduced_filesize_mb} mb")
        
         #percentage of reduction in filesize
        percentage_reduction_filesize = round((reduced_filesize_kb/initial_filesize_kb) * 100,2)
        print(f"percentage of image file size reduced : {percentage_reduction_filesize} %")
       
        
    elif extension == "png":
        print("still developing :>")

print("[welcome to image compressor]")
while True:
    fname = input("Enter image filename --$ ")
    try:
        compress(fname)
    except:
        print("[error occured]")
    