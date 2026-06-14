def get_gif_dimensions(gif_path):
    """Read GIF dimensions without external libraries"""
    try:
        with open(gif_path, 'rb') as f:
            # GIF header is 6 bytes, then logical screen descriptor starts
            f.seek(6)
            # Read width and height (little-endian)
            width_bytes = f.read(2)
            height_bytes = f.read(2)
            width = int.from_bytes(width_bytes, byteorder='little')
            height = int.from_bytes(height_bytes, byteorder='little')
            return width, height
    except:
        print("Couldn't read dimensions from GIF file")
        return None, None