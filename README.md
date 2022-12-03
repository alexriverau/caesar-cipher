# Lab: 18 - Cryptography

---

### Project: Caesar Cipher
### Author: Alejandro Rivera

---

### Feature Tasks and Requirements
* Create an encrypt function that takes in a plain text phrase and a numeric shift.
  * the phrase will then be shifted that many letters.
    * e.g. encrypt(‘abc’,1) would return ‘bcd’. = e.g. encrypt(‘abc’, 10) would return ‘klm’.
  * shifts that exceed 26 should wrap around.
    * e.g. encrypt(‘abc’,27) would return ‘bcd’.
  * shifts that push a letter out or range should wrap around.
    * e.g. encrypt(‘zzz’,1) would return ‘aaa’.
  * Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
  * Create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
  * Devise a method for the computer to determine if code was broken with minimal human guidance.

### How to initialize/run your application

* python3 caesar_cipher.py

### Tests
