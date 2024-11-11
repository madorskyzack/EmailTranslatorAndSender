
# Email Translator and Sender

Prompts user through the terminal to enter an the sender's email, the email's app password (to bypass two factor authentication) and the recipients email. Gives the option to translate the message into another language and then sends the email. Does not allow any errors in inputs from the user.


## Author

Zachary Madorsky
## Acknowledgements

 - [Guide on the Email Sender by CodeWithTomi](https://www.youtube.com/watch?v=zxFXnLEmnb4)
 


## Usage/Examples

Terminal after running assuming all inputs are correct:
```
Enter the sender email (ex. "example@gmail.com"): test@test.test 
Enter the app password of the sender email (ex: "abcd efgh ijkl mnop"): test test test test 
Enter the receiver email (ex. "example@gmail.com"): receiver@email.com
Enter the subject of the email: Testing
Enter the body: Hello World!
Would you like to translate the email into another language? (y/Y for Yes, n/N for No): y
What language would you like to translate to? (s for Spanish, r for Russian, f for French, c for Chinese, t for Tagalog): s
Sending email...
Email sent from madorskyzack@gmail.com to madorskyzack@gmail.com translated from English to Spanish!
```
Terminal after running with wrong inputs:

```
Enter the sender email (ex. "example@gmail.com"): wronginput@12.    
Invalid format. Enter the sender email (ex. "example@gmail.com"): right@input.com
Enter the app password of the sender email (ex: "abcd efgh ijkl mnop"): wronginput
Invalid format. Enter the app password of the sender email (ex: "abcd efgh ijkl mnop"): abcd efgh ijkl mnop 
Enter the receiver email (ex. "example@gmail.com"): wrong    
Invalid format. Enter the receiver email (ex. "example@gmail.com"): correct@format.com
Enter the subject of the email: can be any string 
Enter the body: also can be any string
Would you like to translate the email into another language? (y/Y for Yes, n/N for No): wronginput
Invalid input. Would you like to translate the email into another language? (y/Y for Yes, n/N for No): y
What language would you like to translate to? (s for Spanish, r for Russian, f for French, c for Chinese, t for Tagalog): wrong
Invalid input. What language would you like to translate to? (s for Spanish, r for Russian, f for French, c for Chinese, t for Tagalog): s
Sending email...
The email or app password is incorrect and the email failed to send. 
```


## Questions/Support

For questions or support, email madorskyzack@gmail.com.
