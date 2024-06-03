def _init_(self, name):
       self.name = name
       self.content = ""
 
def write(self, data):
       self.content += data
 
def read(self):
       return self.content
 
class FileSystem:
   def _init_(self):
       self.files = {}
 
   def create_file(self, name):
       if name in self.files:
           raise Exception("File already exists.")
       self.files[name] = File(name)
       print(f"File '{name}' created.")
 
   def write_to_file(self, name, data):
       if name not in self.files:
           raise Exception("File does not exist.")
       self.files[name].write(data)
       print(f"Data written to file '{name}'.")
 
   def read_from_file(self, name):
       if name not in self.files:
           raise Exception("File does not exist.")
       content = self.files[name].read()
       print(f"Reading from file '{name}': {content}")
       return content
 
   def list_files(self):
       print("Listing files:")
       for file_name in self.files:
           print(file_name)

# Exemplo de uso do sistema de arquivos
 
fs = FileSystem()
 
# Criação de arquivos
fs.create_file("file1.txt")
fs.create_file("file2.txt")
 
# Escrita em arquivos
fs.write_to_file("file1.txt", "Hello, World!")
fs.write_to_file("file2.txt", "Python é incrível!")
 
# Leitura de arquivos
fs.read_from_file("file1.txt")
fs.read_from_file("file2.txt")
# Listar arquivos
fs.list_files()
#Explicação do código:
#Classe File:
#Representa um arquivo no sistema de arquivos.
#Possui um nome (name) e conteúdo (content).
#Métodos write e read para escrever e ler dados do arquivo.
#Classe FileSystem:
#Representa o sistema de arquivos.
#Utiliza um dicionário (self.files) para armazenar arquivos.
#Métodos para criar arquivos (create_file), escrever dados em arquivos (write_to_file), 
#ler dados de arquivos (read_from_file) e listar todos os arquivos (list_files).
#Exemplo de uso:
#Cria uma instância do sistema de arquivos (fs).
#Cria dois arquivos (file1.txt e file2.txt).
#Escreve dados nesses arquivos.
#Lê os dados desses arquivos.
#Lista todos os arquivos criados.
#Este é um exemplo simples e básico, mas mostra os conceitos fundamentais de um 
#sistema de arquivos em memória. Em um sistema de arquivos real, você teria que 
#lidar com muito mais complexidade, como permissões de arquivos, estrutura de diretórios, persistência em disco, entre outros.