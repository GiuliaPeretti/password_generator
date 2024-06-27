import gradio as gr
import random
import ast

def algo1(lenght, uppercase_letters, lowercas_letters, digit, symbols):
    s=""
    for i in range(lenght):
        match(random.randint(0,3)):
            case 0:
                s=s+random.choice(uppercase_letters)
            case 1:
                s=s+random.choice(lowercas_letters)
            case 2:
                s=s+random.choice(digit)
            case 3:
                s=s+random.choice(symbols)
    return(s)

def algo2(lenght, uppercase_letters, lowercas_letters, digit, symbols):
    s=""
    for i in range(lenght):
        print(i%3)
        match(i%4):
            case 0:
                s=s+random.choice(uppercase_letters)
            case 1:
                s=s+random.choice(lowercas_letters)
            case 2:
                s=s+random.choice(digit)
            case 3:
                s=s+random.choice(symbols)
    return(s) 

def algo3(lenght, uppercase_letters, lowercas_letters, digit, symbols):
    s=""
    new_list=uppercase_letters+lowercas_letters+digit+symbols
    l = list(new_list)
    random.shuffle(l)
    new_list = ''.join(l)
    index=random.randint(0, len(new_list)-lenght)
    s=new_list[index:index+lenght]
    return s

def algo4(lenght, uppercase_letters, lowercas_letters, digit, symbols):
    uppercase_letters=shuffle_string(uppercase_letters)
    lowercas_letters=shuffle_string(lowercas_letters)
    digit=shuffle_string(digit)
    symbols=shuffle_string(symbols)

    s=""
    chunck_size=random.randint(2,5)
    for i in range (0, lenght, 1):
        match(random.randint(0,3)):
            case 0:
                index=random.randint(0,len(uppercase_letters))
                s=s+uppercase_letters[index:index+chunck_size]
            case 1:
                index=random.randint(0,len(lowercas_letters))
                s=s+lowercas_letters[index:index+chunck_size]
            case 2:
                index=random.randint(0,len(digit))
                s=s+digit[index:index+chunck_size]
            case 3:
                index=random.randint(0,len(symbols))
                s=s+symbols[index:index+chunck_size]
    s=shuffle_string(s)
    index=random.randint(0,len(symbols))
    s=s[index:index+lenght]
    return(s)


def shuffle_string(string):
    string = list(string)
    random.shuffle(string)
    string = ''.join(string)
    return(string)




def generate_password():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercas_letters = uppercase_letters.lower()
    digit = "0123456789"
    symbols = "(){}[]*$,;.:-_/\\&%?^*#@<>"
    match(random.randint(0,3)):
        case 0:
            return(algo4(20,uppercase_letters, lowercas_letters, digit, symbols))
        case 1:
            return(algo4(20,uppercase_letters, lowercas_letters, digit, symbols))
        case 2:
            return(algo4(20,uppercase_letters, lowercas_letters, digit, symbols))
        case 3:
            return(algo4(20,uppercase_letters, lowercas_letters, digit, symbols))

def store(service, username, password):
    if(service==''):
        return('','','','please write the service where you would use your password')
    if(username==''):
        return('','','','please write the username')
    if (password==""):
        return('','','','please write or generate a password')
    data=open('passwords.json', 'r').read()
    data=ast.literal_eval(data)
    data.append({"service": service, "username": username, "password": password})
    data=str(data)
    data=data.replace("'",'"')
    with open('passwords.json', 'w') as f:
        f.write(str(data))
    return('','','','Done!')

def get_password(service_get):
    data=open('passwords.json', 'r').read()
    data=ast.literal_eval(data)
    result=None
    for r in data:
        if r["service"].lower()==service_get.lower():
            result=r
    if result is None:
        return('','','',"Can't find a password stored for this service")
    return(result['username'], result['password'], 'Done!')




if __name__=='__main__':
    with gr.Blocks() as demo:
        gr.Markdown("# Password manager")
        with gr.Row():
            with gr.Column():
                service=gr.Textbox(label="What is this password for?")
                username=gr.Textbox(label="Username/E-mail")
                password=gr.Textbox(label="Password")
                result=gr.Textbox(label="Result")
                with gr.Row():
                    generate=gr.Button("Generate password")
                    update_data=gr.Button("Store pssword")
            with gr.Column():
                service_get=gr.Textbox(label="What is this password for?")
                username_get=gr.Textbox(label="Username/E-mail")
                password_get=gr.Textbox(label="Password")
                result_get=gr.Textbox(label="Result")
                with gr.Row():
                    get_data=gr.Button("Get password")
                    update=gr.Button("Update")
                    remove=gr.Button("Remove")
        generate.click(fn=generate_password, inputs=[], outputs=[password])
        update_data.click(fn=store, inputs=[service, username, password], outputs=[service, username, password, result])
        get_data.click(fn=get_password, inputs=[service_get], outputs=[username_get, password_get, result_get])
    
    
    
    demo.launch(share=False)
