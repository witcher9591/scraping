import subprocess
import random
from test import scrape_and_save

def generate_otp():
    return random.randint(100, 999)

def main():
    name = input("Enter your name: ")
    otp = generate_otp()
    print(f"Hello, {name}! Your OTP is: {otp}")
    
    entered_otp = int(input("Enter the OTP you received: "))
    
    if entered_otp == otp:
        print("Success! OTP matched.")
        try:
            subprocess.run(["python", "test.py"]) 
            # scrape_and_save("https://webscraper.io/test-sites/e-commerce/allinone")

        except FileNotFoundError:
            print("test.py not found.")
    else:
        print("Sorry, OTP did not match. Please try again.")

if __name__ == "__main__":
    main()
