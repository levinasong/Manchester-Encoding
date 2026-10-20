# Manchester Encoding Program
# 0 = High to Low (10)
# 1 = Low to High (01)

def manchester_encoding(binary):
    encoded = ""

    for bit in binary:
        if bit == "0":
            encoded += "10"
        else:
            encoded += "01"

    return encoded


def show_waveform(encoded):
    high = ""
    low = ""

    for signal in encoded:
        if signal == "1":
            high += "---"
            low += "   "
        else:
            high += "   "
            low += "___"

    print("High: " + high)
    print("Low:  " + low)


print("=== Manchester Encoding Program ===")
print("0 = High to Low")
print("1 = Low to High")

while True:
    binary = input("\nEnter binary data: ").strip()

    if binary == "":
        print("Please enter binary data.")
    elif any(bit != "0" and bit != "1" for bit in binary):
        print("Invalid input. Please enter only 0 and 1.")
    else:
        break

encoded = manchester_encoding(binary)

print("\nOriginal binary: " + binary)
print("Manchester encoded: " + encoded)
print("\nWaveform (each group of 3 characters represents half a bit):")
show_waveform(encoded)
print("\nEncoding completed successfully!")
