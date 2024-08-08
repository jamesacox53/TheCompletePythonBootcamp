# My final Capstone Project will be implementing the Encryption and Decryption
# of a Caesar Cipher

class CeasarCipherEncrypter():
    def encrypt(self, text, shift):
        sanitized_text = self._sanitize_text(text)
        encode_dict = self._get_encode_dict(shift)
    
        return self._encrypt_text(sanitized_text, encode_dict)

    def _sanitize_text(self, text):
        return text.strip().lower()

    def _get_encode_dict(self, shift):
        encode_dict = {}

        for c in "abcdefghijklmnopqrstuvwxyz":
            encoded_c = self._encode_char(c, shift)

            encode_dict[c] = encoded_c

        return encode_dict

    def _encode_char(self, c, shift):
        if shift == 0:
            return c

        c_ascii_code = ord(c)
        c_pos = c_ascii_code - 97

        enc_pos = (c_pos + shift) % 26
        enc_ascii_code = enc_pos + 97

        return chr(enc_ascii_code)

    def _encrypt_text(self, text, encode_dict):
        encrypted_text = ""

        for c in text:
            if c == ' ':
                encrypted_text += ' '
            
            else:
                encoded_c = encode_dict[c]

                encrypted_text += encoded_c

        return encrypted_text

class CeasarCipherDecrypter():
    def decrypt(self, text, shift):
        sanitized_text = self._sanitize_text(text)
        decode_dict = self._get_decode_dict(shift)
    
        return self._decrypt_text(sanitized_text, decode_dict)

    def _sanitize_text(self, text):
        return text.strip().lower()

    def _get_decode_dict(self, shift):
        decode_dict = {}

        for c in "abcdefghijklmnopqrstuvwxyz":
            decoded_c = self._decode_char(c, shift)

            decode_dict[c] = decoded_c

        return decode_dict

    def _decode_char(self, c, shift):
        if shift == 0:
            return c

        c_ascii_code = ord(c)
        c_pos = c_ascii_code - 97

        dec_pos = (c_pos + 26 - shift) % 26
        dec_ascii_code = dec_pos + 97

        return chr(dec_ascii_code)

    def _decrypt_text(self, text, decode_dict):
        decrypted_text = ""

        for c in text:
            if c == ' ':
                decrypted_text += ' '
            
            else:
                decoded_c = decode_dict[c]

                decrypted_text += decoded_c

        return decrypted_text
    

if __name__ == '__main__':
    shift = 5
    text = "this text will be encrypted and decrypted with a ceasar cipher"
    print("The original text: \n" + text)
    print("The shift: \n" + str(shift))
    print("")

    encrypter = CeasarCipherEncrypter()
    enc_text = encrypter.encrypt(text, shift)
    print("The encoded text: \n" + enc_text)
    print("")

    decrypter = CeasarCipherDecrypter()
    dec_text = decrypter.decrypt(enc_text, shift)
    print("The decoded text: \n" + dec_text)
    print("")