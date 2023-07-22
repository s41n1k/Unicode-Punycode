import idna
import unicodedata

def unicode_to_punycode(text):
    try:
        punycode = idna.encode(text).decode('ascii')
        return punycode
    except idna.IDNAError as e:
        print("Error converting text to Punycode:", e)
        return None
def unicode_to_normal(text):
    # Use the NFKD normalization form to convert Unicode to normal text
    normalized_text = unicodedata.normalize('NFKD', text)
    # Remove any characters that are not in the ASCII range
    normal_text = normalized_text.encode('ascii', 'ignore').decode('ascii')
    return normal_text

if __name__ == "__main__":
    unicode_text = input("[=] Unicode Character subdomain Name(example: ǎpoc): ")
    maindomain_text = input("[=] Enter your Main-Domain: ")
    punycode_text = unicode_to_punycode(unicode_text + "." + maindomain_text)
    normal_text = unicode_to_normal(unicode_text)
    if punycode_text:
        print("[!] Unicode Subdomain :", punycode_text)
        print("[!] Original Subdomain :", normal_text + "." + maindomain_text)
