import complex_pb2

complex_message = complex_pb2.ComplexMessage()
complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "Hello"

first_message = complex_message.multiple_dummy.add()
first_message.id = 2345
first_message.name = "ssds"

complex_message.multiple_dummy.add(id=4545, name="Second dummy")

print (complex_message)
