from compress import Compressor

class exceptions:
	class MethodNotFound(Exception):
		pass

def initialize_compressor(compression_method):
	if not compression_method:
		compression_method = "bz2"
	compressor = Compressor()
	if not hasattr(compressor, f"use_{compression_method}"):
		raise exceptions.MethodNotFound(f"Compression method {compression_method} wasn't found")
	getattr(compressor, f"use_{compression_method}")()
	return compressor

def compress(binary_data, compression_method = None):
	compressor = initialize_compressor(compression_method)
	return compressor.compress(binary_data)

def decompress(binary_data, compression_method = None):
	compressor = initialize_compressor(compression_method)
	return compressor.decompress(binary_data)
