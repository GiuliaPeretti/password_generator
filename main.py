import gradio as gr
import random

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
    return(algo4(20,uppercase_letters, lowercas_letters, digit, symbols))



if __name__=='__main__':
    with gr.Blocks() as demo:

        gr.Markdown("# Password manager")
        result=gr.Textbox(label="Result")
        generate=gr.Button("Generate password")
        
        generate.click(fn=generate_password, inputs=[], outputs=[result])
    demo.launch(share=False)
