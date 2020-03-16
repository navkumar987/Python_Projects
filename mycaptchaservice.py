from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random

numbers_to_display = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowercase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

uppercase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']


# i have set the character length to 5
def create_random_captcha(captcha__size=5):
    captcha_list = []

    random_char = lowercase_char + uppercase_char + numbers_to_display

    for i in range(captcha__size):
        # One Random Character would be selected by using random module
        # it will run until the loop ends
        char = random.choice(random_char)

        # each character would be appended to list
        captcha_list.append(char)

    captcha_string = ''

    # convert the list into a string
    for characters in captcha_list:
        captcha_string += str(characters)

    return captcha_string


# image saving is optional
def create_image_captcha(captcha_text):
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(captcha_text)
    image_file = "./captcha_" + captcha_text + ".png"
    image_captcha.write(captcha_text, image_file)
    plt.imshow(image)
    plt.show()
    user_input = input("Enter the Captcha Displayed above:\n")
    # print(user_input)
    # print(captcha_text)
    if user_input == captcha_text:
        print("Pass")
    else:
        print("False")




if __name__ == '__main__':
    # Create random text.
    captcha_text = create_random_captcha()

    # Create image captcha.
    create_image_captcha(captcha_text)
