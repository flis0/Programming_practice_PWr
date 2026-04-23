class Encoder:
    def __init__(self, encoding_type):
        self.encoding_type = encoding_type

    def encode(self, data):
        return f"{self.encoding_type} encoded ({data})"
    
    def decode(self, data):
        return data[len(f"{self.encoding_type} encoded ("):-1]
    
class Compressor:
    def __init__(self, compression_type):
        self.compression_type = compression_type

    def compress(self, data):
        return f"{self.compression_type} compressed ({data})"
    
    def decompress(self, data):
        return data[len(f"{self.compression_type} compressed ("):-1]
    
class Storage:
    def send(self, data):
        self.data =  f"Stored data ({data})"
    
    def receive(self):
        return self.data[len("Stored data ("):-1]

class DataStorageFacade:
    def __init__(self, encoding_type, compression_type):
        self.encoder = Encoder(encoding_type)
        self.compressor = Compressor(compression_type)
        self.storage = Storage()

    
    def store_data(self, data):
        encoded_data = self.encoder.encode(data)
        compressed_data = self.compressor.compress(encoded_data)
        self.storage.send(compressed_data)
    
    def get_data(self):
        received_data = self.storage.receive()
        decompressed_data = self.compressor.decompress(received_data)
        decoded_data = self.encoder.decode(decompressed_data)
        return decoded_data
    
    def peek_storage(self):
        return self.storage.data
    

if __name__ == "__main__":
    facade = DataStorageFacade("UTF8", "Gzip")
    facade.store_data(input('Data to store: '))

    print('\nData in storage:')
    print(facade.peek_storage())

    retrieved_data = facade.get_data()
    print('\nRetrieved data:')
    print(retrieved_data)