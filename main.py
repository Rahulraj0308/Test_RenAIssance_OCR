import tensorflow as tf
if __name__ == '__main__':
    image_path=str(input("Enter the file Path(JPG/PNG/PDF): "))
    print(tf.config.list_physical_devices('GPU'))
    print(image_path)
    pass