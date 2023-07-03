import lief
import argparse
import constants

class HolesDetection:
	
	#constant
	size_MS_DOS_HEADER = 60 #bytes
	size_FILE_HEADER = 24 #bytes (contain 4bytes signature PE\0\0)

	def __init__(self, file):
		self.file = file
		if lief.is_pe(file):
			self.peFile = lief.parse(file)
			with open(file, 'rb') as f:
				self.fileContent = f.read()
		else:
			self.peFile = None
			self.fileContent = None
		self.strings = None

	# Function to check if a byte is printable
	def is_printable(self,byte):
		return byte >= 32 and byte <= 126
	
	def bytes_to_hexdump(self, bytes):
		# Iterate over the byte string and form the table
		for i in range(0, len(bytes), 16):
			line = bytes[i:i+16]
			hex_line = ' '.join(f'{b:02x}' for b in line)
			char_line = ''.join(chr(b) if self.is_printable(b) else '.' for b in line)
			print(f'{hex_line.ljust(47)} | {char_line}')
		print("--------------------")


	def to_bytes(self,memory):
		bytes=b''
		for i in range(len(memory)):
			bytes += memory[i].to_bytes(1, byteorder='big')
		return bytes

	# Take "size" number of bytes before a "position" in file
	def from_file_to_bytes(self, position, size):
		message = b''
		for bytes in self.fileContent[position-size:position]:
			message += bytes.to_bytes(1, byteorder='big')

		if_is_zero = all(byte == 0 for byte in message)
		return message, if_is_zero
	
	def printHolesInformation(self):

		# Dos_stub
		print(constants.GREEN+"Dos stub: %s bytes" %len(self.peFile.dos_stub)+constants.RESET)
		self.bytes_to_hexdump(self.peFile.dos_stub)
		
		# Rich header
		if self.peFile.has_rich_header:
			print(constants.RED+"Rich header: %s bytes\n" %len(self.peFile.rich_header)+constants.RESET)
			print(self.bytes_to_hexdump(self.peFile.rich_header))
		else:
			print(constants.GREEN+"Rich header: None"+constants.RESET)
			print("--------------------")
		

		#H ole  between section table and 1st section

		"""   
		Offset of File header is store in dos header: addressof_new_exeheader
		Size of File header is 24 bytes (contain 4 bytes signature PE\0\0)
		Size of Optional header store in File header
		Size of one section table is 40 bytes; number of section is store in file header
		Offset of first section is store in section table: sections[0].offset
		"""
		sections = self.peFile.sections
		gap = \
			sections[0].offset - self.peFile.dos_header.addressof_new_exeheader \
			- (24 + self.peFile.header.sizeof_optional_header + self.peFile.header.numberof_sections * 40)

		if gap != 0:
			print("Hole between section table and 1st section: %s bytes" %gap)
			bytes, if_is_zero = self.from_file_to_bytes(sections[0].offset, gap)
			if not if_is_zero:
				print(constants.RED+"Non-zero padding"+constants.RESET)
				self.bytes_to_hexdump(bytes)
			else:
				print(constants.GREEN+"Ze-ro padding"+constants.RESET)

		# Overlay
		if self.peFile.dos_header.overlay_number == 0:
			print(constants.GREEN+"Number of Overlay: %s numbers" %self.peFile.dos_header.overlay_number+constants.RESET)
		else:
			print(constants.RED+"Number of Overlay: %s numbers" %self.peFile.dos_header.overlay_number+constants.RESET)
		print("--------------------")


		# After last section
		end_last_section = sections[len(sections)-1].offset + sections[len(sections)-1].size
		print("After last section: There are %s bytes" %(len(self.fileContent) - end_last_section))

		if end_last_section == len(self.fileContent):
			print(constants.GREEN+"No bytes after last section"+constants.RESET)
		else:
			print(constants.RED+"Bytes after last section:"+constants.RESET)
			self.bytes_to_hexdump(self.fileContent[end_last_section:])



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='pe file analyzer')
	parser.add_argument("-f", "--file", help="The file to analyze", required=True, dest="file")
	args = parser.parse_args()
	
	holesDetection = HolesDetection(args.file)
	holesDetection.printHolesInformation()