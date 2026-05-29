greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string" #concatenate

name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format("Akshat") #format function replaces the {} with the value of name

print(intrupution, formatted)

print(greet.lower(), extened_grt.upper())

print(extened_grt.replace("long", "short")) 
