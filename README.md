## Phishing Maker
A simple phishing maker that converts the website source into a phishing website

### How to use
1. Go to the website
2. Get the form index
- Go to Console and execute ``document.getElementsByTagName("form");``

![image](https://user-images.githubusercontent.com/104715127/186502861-7236c7bd-6615-4675-b171-40cf3314ff75.png)

And see that number ``0`` that is our **form index**, some website may have more than 1 forms

3. Get the **username** and **password** input ID

![image](https://user-images.githubusercontent.com/104715127/186503163-209093db-5f29-479b-a5e1-b9348d049d33.png)

4. Copy the page source and paste into output.html
5. Run the program ``main.py`` and insert the **form index**; username; and password ID.
6. Done!
