import fitz  # PyMuPDF
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

def convert_pdf_to_image(pdf_path: str, zoom: float = 2.0) -> list[str]:
    """
    Converts a PDF into high-quality images.
    
    Args:
        pdf_path (str): Path to the input PDF file.
        zoom (float): Scale factor for resolution (default: 2.0).
        
    Returns:
        list[str]: List of saved image file paths.
    """
    saved_images = []
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]

        # Increase resolution using a transformation matrix
        matrix = fitz.Matrix(zoom, zoom)  # Scaling for higher DPI
        pixmap = page.get_pixmap(matrix=matrix) 
        img_array = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(pixmap.h, pixmap.w, -1)
        
        
        saved_images.append(img_array)

    return saved_images
